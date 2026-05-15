# === SISTEMA DE TEMPO ===
default dia_atual = 1
default periodo_atual = 1  # 1 = Manhã, 2 = Tarde, 3 = Noite

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

# Label chamada ao final de cada evento executado
label avancar_tempo:
    $ periodo_atual += 1
    if periodo_atual > 3:
        $ periodo_atual = 1
        $ dia_atual += 1
        # Para evitar loops infinitos caso a narrativa preveja coisas até o fim do dia
        # O MC pode comentar quando vai dormir, se formos incrementar o sistema, 
        # mas por enquanto avança invisível ou faz transição limpa.
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
