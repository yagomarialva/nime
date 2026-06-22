# === FUNDOS TEMPORÁRIOS DA PRAIA ===
init:
    image bg ceu_azul = Solid("#87CEFA")
    image bg praia_areia = Solid("#F4A460")
    image bg praia_mar = Solid("#00CED1")
    image bg praia_cabana = Solid("#D2B48C")
    image bg praia_quiosque = Solid("#FFD700")

label capitulo7:
    if "capitulo7" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo7")
        
    scene black with fade
    
    narrator "A equipe de fumigação da prefeitura chegou cedo. Tivemos que pegar o que restou de nossas coisas limpas e jogar no bagageiro de uma van caindo aos pedaços."
    narrator "Quatro horas de viagem pelo litoral sul depois..."
    
    scene bg ceu_azul with fade
    
    narrator "O cheiro de maresia substituiu o de borracha queimada. A 'casa caindo aos pedaços' da tia da Larissa era uma cabana de madeira simples, mas ficava literalmente com o pé na areia."
    
    show huey bikini at center
    
    huey "O oceano... é um quadro azul cinético que nunca seca."
    
    narrator "A tensão dos últimos dias derreteu instantaneamente."
    
    mc "Certo, pessoal. Três dias de refúgio. Vamos esquecer o edital, a mãe da Nicole, e focar em tirar a fuligem dos pulmões."
    
    # === LOOP DO MAPA CAP 7 (PRAIA) ===
    $ dia_atual = 7
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Mapeando os 6 eventos para os dias de praia (Dias 7, 8 e 9).
    # Usando os novos cenários da praia.
    $ game_events.add_event("praia_areia", "evento_cap7_huey", 7, [1, 2, 3])
    $ game_events.add_event("praia_mar", "evento_cap7_camille", 7, [1, 2, 3])
    $ game_events.add_event("praia_cabana", "evento_cap7_samantha", 7, [1, 2, 3])
    $ game_events.add_event("praia_mar", "evento_cap7_larissa", 8, [1, 2, 3])
    $ game_events.add_event("praia_quiosque", "evento_cap7_nicole", 8, [1, 2, 3])
    $ game_events.add_event("praia_areia", "evento_cap7_katia", 8, [1, 2, 3])

label loop_mapa_cap7:
    if dia_atual >= 10:
        mc "O sol já está caindo. Larissa acendeu uma fogueira perto da água."
        jump capitulo7_luau

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap7
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_cap7_huey":
            $ add_shared_memory("huey_castelo", ["huey"], "Construí um castelo de areia com a Huey.")
        elif evt_label == "evento_cap7_camille":
            $ add_shared_memory("camille_paz", ["camille"], "Usei lábia para espantar os turistas de perto da Camille.")
        elif evt_label == "evento_cap7_samantha":
            $ add_shared_memory("samantha_praia", ["samantha"], "Ajudei Samantha com agorafobia sob as estrelas.")
        elif evt_label == "evento_cap7_larissa":
            $ add_shared_memory("larissa_praia", ["larissa"], "Fisioterapia noturna no mar com Larissa.")
        elif evt_label == "evento_cap7_nicole":
            $ add_shared_memory("nicole_praia", ["nicole"], "Nicole finalmente conheceu o gosto do caldo de cana e liberdade.")
        elif evt_label == "evento_cap7_katia":
            $ add_shared_memory("katia_praia", ["katia"], "Prometi uma nova fechadura blindada para a durona da Katia.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        mc "Estou apenas curtindo a brisa do mar."
        call avancar_tempo(15)
        
    jump loop_mapa_cap7