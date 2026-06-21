# === SISTEMA DE TEMPO ===
default dia_atual = 1
default periodo_atual = 1  # 1 = Manhã, 2 = Tarde, 3 = Noite

# === SISTEMA DE STATS (Tales of Home style) ===
default player_stats = {
    "fitness": 0,
    "intelligence": 0,
    "energy": 100,
    "money": 0
}

define STAT_CAPS = {
    "fitness": 100,
    "intelligence": 100,
    "energy": 100,
    "money": 999999
}

init python:
    # Retorna o nome do período formatado para a UI (com suporte a i18n)
    def get_nome_periodo(periodo_num):
        if periodo_num == 1:
            return _("Manhã")
        elif periodo_num == 2:
            return _("Tarde")
        elif periodo_num == 3:
            return _("Noite")
        return _("Desconhecido")

    def _validate_player_stats():
        """Valida e corrige os status do jogador após carregar um save.
        Garante que as chaves existem com os valores corretos e aplica limites."""
        
        # Cria player_stats se não existir
        if not hasattr(store, 'player_stats') or store.player_stats is None:
            store.player_stats = {
                "fitness": 0,
                "intelligence": 0,
                "energy": 100,
                "money": 0
            }
            return
        
        # Garante que seja um dicionário
        if not isinstance(store.player_stats, dict):
            store.player_stats = {
                "fitness": 0,
                "intelligence": 0,
                "energy": 100,
                "money": 0
            }
            return
        
        # Adiciona chaves faltando
        defaults = {"fitness": 0, "intelligence": 0, "energy": 100, "money": 0}
        for key, default_value in defaults.items():
            if key not in store.player_stats:
                store.player_stats[key] = default_value
        
        # Aplica limites para prevenir valores inválidos (bugs de saves velhos)
        store.player_stats["fitness"] = max(0, min(store.player_stats["fitness"], STAT_CAPS["fitness"]))
        store.player_stats["intelligence"] = max(0, min(store.player_stats["intelligence"], STAT_CAPS["intelligence"]))
        store.player_stats["energy"] = max(0, min(store.player_stats["energy"], STAT_CAPS["energy"]))
        store.player_stats["money"] = max(0, min(store.player_stats["money"], STAT_CAPS["money"]))

    # Registra callback de pós-carregamento de saves
    config.after_load_callbacks.append(_validate_player_stats)

    def update_player_stat(stat_name, amount):
        """Atualiza os status do jogador respeitando limites, e pode notificar"""
        if stat_name in store.player_stats:
            current_value = store.player_stats[stat_name]
            max_value = STAT_CAPS.get(stat_name, 100)
            
            # Limites
            new_value = max(0, min(current_value + amount, max_value))
            change = new_value - current_value
            
            if change != 0:
                store.player_stats[stat_name] = new_value
                # Notificação visual similar a Tales of Home
                if change > 0:
                    renpy.notify(_(f"{stat_name.capitalize()} +{change}"))
                else:
                    renpy.notify(_(f"{stat_name.capitalize()} {change}"))
                return True
        return False

# Label chamada ao final de cada evento executado
label avancar_tempo(custo_energia=0):
    if custo_energia > 0:
        $ update_player_stat("energy", -custo_energia)
        
    $ periodo_atual += 1
    if periodo_atual > 3:
        $ periodo_atual = 1
        $ dia_atual += 1
        # O sono reseta a energia pro próximo dia
        $ player_stats["energy"] = STAT_CAPS["energy"]
        $ renpy.notify(_("Um novo dia começa! Energia restaurada."))
        
    return

# === GERENCIADOR DE EVENTOS ===
init python:
    class EventManager:
        def __init__(self):
            # Formato do dicionário: { "local_id": [ {"label": "nome_da_label", "dia": 1, "periodo": [1, 2, 3], "reqs": []} ] }
            self.events = {}
            # Rastreia os eventos já disparados pelo nome da label
            self.completed_events = []

        def add_event(self, location, label, valid_days, valid_periods):
            """
            Registra um evento para um local
            - location: String identificadora do local (ex: "biblioteca")
            - label: A label Ren'Py do evento
            - valid_days: Lista ou Int dos dias aceitos
            - valid_periods: Lista de períodos do dia aceitos [1,2,3]
            """
            if location not in self.events:
                self.events[location] = []
            
            if isinstance(valid_days, int):
                valid_days = [valid_days]
            if isinstance(valid_periods, int):
                valid_periods = [valid_periods]
                
            self.events[location].append({
                "label": label,
                "days": valid_days,
                "periods": valid_periods
            })

        def get_pending_event(self, location, current_day, current_period):
            """
            Retorna a label do evento se um estiver válido para aquele lugar e tempo, 
            e ainda não tiver sido completado. Caso contrário, retorna None.
            """
            if location not in self.events:
                return None
                
            for event in self.events[location]:
                if event["label"] in self.completed_events:
                    continue # Já fez este evento
                    
                if current_day in event["days"] and current_period in event["periods"]:
                    return event["label"]
                    
            return None
            
        def mark_completed(self, label):
            """
            Marca a label como concluída
            """
            if label not in self.completed_events:
                self.completed_events.append(label)

# Instância global do EventManager, associada a uma default var para o save state.
# Precisamos garantir persistência, então usamos as facilidades do Ren'Py
default game_events = EventManager()
