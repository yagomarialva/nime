## screens_map.rpy — Sistema de Navegação por Modal (Location Navigator)
## Substituição do antigo mapa_interativo por um modal elegante com thumbnails.

# ==============================================================================
# DADOS DOS LOCAIS NAVEGÁVEIS
# ==============================================================================
# Lista centralizada de todos os locais disponíveis no mapa.
# Para adicionar um novo local, basta incluir um novo dicionário nesta lista.
# NOTA: "nome" e "descricao" são chaves de tradução. O _() é aplicado
# na screen em tempo de renderização para respeitar mudanças de idioma.

init python:
    mapa_locais = [
        {
            "id": "biblioteca",
            "nome": "Biblioteca",
            "descricao": "Um refúgio de conhecimento e silêncio",
            "imagem": "images/cenarios/biblioteca.png",
            "categoria": "campus"
        },
        {
            "id": "quadra",
            "nome": "Quadra de Esportes",
            "descricao": "Onde a energia e a competição se encontram",
            "imagem": "images/cenarios/QUADRA.png",
            "categoria": "campus"
        },
        {
            "id": "cinema",
            "nome": "Cinema Universitário",
            "descricao": "Filmes, debates e encontros inesperados",
            "imagem": "images/cenarios/cinema.png",
            "categoria": "campus"
        },
        {
            "id": "galeria",
            "nome": "Galeria de Arte",
            "descricao": "Expressão artística e sensibilidade",
            "imagem": "images/cenarios/sala_arte.png",
            "categoria": "campus"
        },
        {
            "id": "laboratorio",
            "nome": "Laboratório de Dados",
            "descricao": "Tecnologia, código e descobertas",
            "imagem": "images/cenarios/lab.png",
            "categoria": "campus"
        },
        {
            "id": "ginasio",
            "nome": "Ginásio do Festival",
            "descricao": "Tendas de jogos e eventos físicos",
            "imagem": "images/cenarios/QUADRA.png",
            "categoria": "campus"
        },
        {
            "id": "jardim_campus",
            "nome": "Jardins do Campus",
            "descricao": "Tendas místicas e contato com a natureza",
            "imagem": "images/cenarios/jardim_universidade.png",
            "categoria": "campus"
        },
        {
            "id": "estacionamento",
            "nome": "Estacionamento (Palco)",
            "descricao": "Palco de desfiles e eventos abertos",
            "imagem": "images/cenarios/campus_sunset.png",
            "categoria": "campus"
        },
        {
            "id": "corredor_salas",
            "nome": "Corredor das Salas",
            "descricao": "Exposições acadêmicas e de arte",
            "imagem": "images/cenarios/classroom.png",
            "categoria": "campus"
        },
        {
            "id": "jogos",
            "nome": "Centro de Jogos",
            "descricao": "Diversão, estratégia e camaradagem",
            "imagem": "images/cenarios/Arcade.jpg",
            "categoria": "campus"
        },
        {
            "id": "predio_adm",
            "nome": "Prédio da Administração",
            "descricao": "Burocracia, editais e professores",
            "imagem": "images/cenarios/auditorium.png",
            "categoria": "campus"
        },
        {
            "id": "quarto",
            "nome": "Seu Quarto",
            "descricao": "Descanso e uso do PC",
            "imagem": "images/cenarios/casa_interior.png",
            "categoria": "casa"
        },
        {
            "id": "sala_jantar",
            "nome": "Sala de Jantar",
            "descricao": "Área de convívio",
            "imagem": "images/cenarios/sala_jantar.png",
            "categoria": "casa"
        },
        {
            "id": "cozinha_escura",
            "nome": "Cozinha",
            "descricao": "Refeições e conversas na madrugada",
            "imagem": "images/cenarios/cozinha_escura.png",
            "categoria": "casa"
        },
        {
            "id": "quintal",
            "nome": "Quintal",
            "descricao": "Ar livre e reformas necessárias",
            "imagem": "images/cenarios/quintal.png",
            "categoria": "casa"
        },
        {
            "id": "praia_cabana",
            "nome": "Cabana",
            "descricao": "Nossa morada improvisada",
            "imagem": "images/cenarios/fogueira_noite.png",
            "categoria": "praia"
        },
        {
            "id": "praia_areia",
            "nome": "Faixa de Areia",
            "descricao": "Bronzeado e castelos de areia",
            "imagem": "images/cenarios/Praia.png",
            "categoria": "praia"
        },
        {
            "id": "praia_mar",
            "nome": "Mar",
            "descricao": "Ondas e água salgada",
            "imagem": "images/cenarios/praia_amanhecer.png",
            "categoria": "praia"
        },
        {
            "id": "praia_quiosque",
            "nome": "Quiosque",
            "descricao": "Calçadão, água de coco e turistas",
            "imagem": "images/cenarios/praia_chegada.png",
            "categoria": "praia"
        },
    ]

    def local_tem_evento(local_id):
        """Verifica se um local tem evento pendente no dia/periodo atual."""
        try:
            evt = game_events.get_pending_event(local_id, store.dia_atual, store.periodo_atual)
            return evt is not None
        except:
            return False


# ==============================================================================
# SCREEN: MAPA MODAL (Location Navigator)
# ==============================================================================
# Modal principal de navegação. Chamado via "call screen mapa_modal".
# Retorna o id do local selecionado via Return(), ou None se fechado com X.

screen mapa_modal():
    modal True
    zorder 200
    
    # Define a aba inicial baseado no dia atual para conveniência
    default tab_atual = "praia" if (store.dia_atual >= 7 and store.dia_atual <= 9) else "campus"

    # --- Fundo escurecido semi-transparente ---
    add Solid("#000000cc")

    # --- Container principal centralizado ---
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 820
        padding (30, 20, 30, 20)
        background Solid("#1a1a2e")

        # ============================
        # HEADER DO MODAL (posição absoluta no topo do frame)
        # ============================
        frame:
            xalign 0.0
            yalign 0.0
            xfill True
            ysize 70
            padding (20, 12, 20, 12)
            background Solid("#16213e")

            hbox:
                yalign 0.5
                spacing 12

                # Ícone decorativo de mapa
                text "🗺️" size 32 yalign 0.5

                # Título e HUD de Tempo
                vbox:
                    spacing 2
                    text _("MAPA DE NAVEGAÇÃO"):
                        size 26
                        color "#ffffff"
                        bold True
                        kerning 2
                    python:
                        _hud_tempo = _("Dia ") + str(dia_atual) + " — " + get_nome_periodo(periodo_atual)
                    text _hud_tempo:
                        size 16
                        color "#66c1e0"
                        italic True

            # Botões de Abas (Campus / Casa / Praia)
            hbox:
                xalign 0.6
                yalign 0.5
                spacing 20
                
                # Se estamos na praia (capitulo 7), bloqueia campus e casa
                if store.dia_atual < 7 or store.dia_atual >= 10:
                    textbutton "Campus":
                        action SetScreenVariable("tab_atual", "campus")
                        text_size 24
                        text_color ("#ffffff" if tab_atual == "campus" else "#8899aa")
                        text_bold True
                        text_hover_color "#ffcc00"
                        
                    textbutton "Casa":
                        action SetScreenVariable("tab_atual", "casa")
                        text_size 24
                        text_color ("#ffffff" if tab_atual == "casa" else "#8899aa")
                        text_bold True
                        text_hover_color "#ffcc00"
                else:
                    textbutton "Campus (Bloqueado)":
                        action Notify(_("Estamos a 4 horas de viagem do campus. Impossível ir agora."))
                        text_size 24
                        text_color "#555555"
                        text_bold True
                        
                    textbutton "Casa (Bloqueado)":
                        action Notify(_("A casa está em quarentena pela prefeitura. Não podemos voltar."))
                        text_size 24
                        text_color "#555555"
                        text_bold True

                    textbutton "Praia":
                        action SetScreenVariable("tab_atual", "praia")
                        text_size 24
                        text_color ("#ffffff" if tab_atual == "praia" else "#8899aa")
                        text_bold True
                        text_hover_color "#ffcc00"

            # Botão fechar (X) no canto superior direito
            textbutton "✕":
                xalign 1.0
                yalign 0.0
                padding (12, 6, 12, 6)
                text_size 28
                text_color "#666666"
                text_hover_color "#ff4444"
                text_bold True
                action Return(None)

        # ============================
        # SEPARADOR VISUAL (accent line)
        # ============================
        add Solid("#0099cc"):
            ypos 70
            xsize 1140
            ysize 3

        # ============================
        # GRID DE LOCAIS - vpgrid com scroll embutido
        # ============================
        # Posicionamos abaixo do header (70 + 3 + 15 = 88)
        # e acima do footer (deixa 50px embaixo)
        vpgrid:
            cols 3
            spacing 20
            xalign 0.5
            ypos 90
            xsize 1120
            ysize 650
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_xalign 0.5

            for local in mapa_locais:
                if local["categoria"] == tab_atual:
                    # --- Card de cada local ---
                    button:
                        xsize 340
                        padding (10, 10, 10, 14)
                        background Solid("#0f3460")
                        hover_background Solid("#1a4a7a")
                        # Ação: Se tiver energia >= 10, deduz energia (ou não, quem gerencia pode ser o script de destino)
                        # Mas vamos checar pra não deixar viajar com pouca energia.
                        action If(
                            store.player_stats["energy"] >= 10,
                            true=Return(local["id"]),
                            false=Notify(_("Você está cansado demais. Energia insuficiente! (-10 necessários)"))
                        )
    
                        vbox:
                            spacing 8
                            xalign 0.5
    
                            # Container da thumbnail com borda condicional
                            frame:
                                xalign 0.5
                                padding (3, 3, 3, 3)
                                if local_tem_evento(local["id"]):
                                    background Solid("#0099cc55")
                                else:
                                    background Solid("#ffffff11")
    
                                # Thumbnail do background redimensionado (320x180)
                                add Transform(local["imagem"], size=(320, 180)):
                                    xalign 0.5
    
                            # Nome do local + indicador de evento
                            hbox:
                                xalign 0.5
                                spacing 6
    
                                text _(local["nome"]):
                                    size 18
                                    color "#ffffff"
                                    bold True
                                    xalign 0.5
                                    text_align 0.5
    
                                if local_tem_evento(local["id"]):
                                    text "❗":
                                        size 18
                                        yalign 0.5
                                        color "#FF4500"
    
                            # Descrição do local
                            text _(local["descricao"]):
                                size 13
                                color "#8899aa"
                                xalign 0.5
                                text_align 0.5
                                italic True

        # ============================
        # FOOTER COM LEGENDA (posição absoluta no fundo)
        # ============================
        frame:
            xalign 0.5
            yalign 1.0
            xfill True
            ysize 36
            padding (10, 6, 10, 6)
            background Solid("#16213e")

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 30

                hbox:
                    spacing 6
                    text "❗" size 14 yalign 0.5 color "#FF4500"
                    text _("Evento disponível") size 13 color "#8899aa" yalign 0.5

                hbox:
                    spacing 6
                    text "🗺️" size 14 yalign 0.5
                    text _("Clique para visitar") size 13 color "#8899aa" yalign 0.5
                    
                hbox:
                    spacing 6
                    text "⚡" size 14 yalign 0.5 color "#ffcc00"
                    text _("Custo de viagem: 10 Energia") size 13 color "#8899aa" yalign 0.5
