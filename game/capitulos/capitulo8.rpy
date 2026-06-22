label capitulo8:
    if "capitulo8" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo8")
        
    scene bg casa_interior with fade
    
    narrator "O contraste entre a brisa da praia e o corredor escuro da Rua Aurora, 57 foi violento. A casa não cheirava mais à fumaça... mas cheirava fortemente a produtos químicos."
    
    show nicole sad at left
    show samantha neutral at right
    
    nicole "Pelo menos a prefeitura tirou a fuligem pesada. Mas olha o estado dessas paredes..."
    
    samantha "As texturas do teto estão corrompidas. O papel de parede tá descascando como um glitch horrível."
    
    narrator "Antes que pudéssemos sequer colocar as malas no chão, a porta da frente se abriu. O Professor Wendell entrou, segurando uma prancheta."
    
    show professor_wendell neutral at center
    
    professor_wendell "Boa tarde. Vejo que retornaram do litoral."
    
    mc "Professor Wendell? Veio dar as boas-vindas?"
    
    professor_wendell "Vim entregar a avaliação do Engenheiro da Universidade. A casa perdeu 30%% da integridade estética e parte do isolamento térmico."
    
    show katia angry at right
    
    katia "O que quer dizer 'estética'? A estrutura está firme, não tá?"
    
    professor_wendell "Estruturalmente, sim. Mas a Universidade tem padrões. Esta residência está temporariamente inabilitada para o programa de Edital de Moradia Estudantil."
    
    show larissa sad at left
    
    larissa "Isso significa... que nós fomos despejadas?"
    
    professor_wendell "Sinto muito, Larissa. Tenho que assinar a Notificação de Cancelamento amanhã à tarde."
    
    narrator "Um silêncio pesado caiu sobre o grupo. Tudo o que conquistamos... tirado por uma burocracia imobiliária."
    
    mc "Espera, Professor. E se nós consertarmos? O estrago estético. E se nós pintarmos, trocarmos os papéis de parede, consertarmos os móveis?"
    
    professor_wendell "Uma reforma dessas levaria semanas e custaria muito caro."
    
    mc "A gente não precisa de equipe! Nós temos a Huey que é da Arquitetura, a Larissa e a Katia pra força bruta. Nós conseguimos."
    
    narrator "Wendell olhou para o meu rosto determinado, e depois para as garotas."
    
    professor_wendell "A Universidade não tem verba para material..."
    
    nicole "Eu tenho economias da minha mesada e não ligo de gastar com o meu quarto."
    
    professor_wendell "Eu... Vocês têm três dias. Se na minha inspeção final a casa não estiver digna do padrão da universidade, eu assino o despejo."
    
    narrator "Ele virou as costas e saiu. As garotas olharam para mim."
    
    mc "Certo, pessoal. Operação Reforma Extrema começa agora! Vamos dividir as tarefas!"
    
    # Inicia os dias de reforma
    $ dia_atual = 11
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Eventos de comédia/slice of life do Capítulo 8
    $ game_events.add_event("biblioteca", "evento_cap8_biblioteca", 11, [1, 2, 3])
    $ game_events.add_event("cozinha_escura", "evento_cap8_cozinha", 11, [1, 2, 3])
    $ game_events.add_event("predio_adm", "evento_cap8_wendell", 12, [1, 2, 3])

label loop_mapa_cap8:
    if dia_atual >= 13:
        narrator "Chegou o dia da Inspeção. O Professor Wendell está batendo na porta."
        jump capitulo8_inspecao

    scene bg sala_jantar
    show screen hud_celular
    show screen player_hud
    
    $ ui_message = "Reforma da Casa - Dia " + str(dia_atual)
    
    call screen mapa_modal

    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap8
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    hide screen mapa_modal
    hide screen hud_celular
    hide screen player_hud
    
    if evt_label:
        if evt_label == "evento_cap8_biblioteca":
            $ add_shared_memory("cap8_obra", ["samantha", "huey"], "Planejamos a arquitetura da reforma na base de vídeos de tutorial do YouTube.")
        elif evt_label == "evento_cap8_wendell":
            $ add_shared_memory("cap8_wendell", ["nicole"], "Roubei a caneta do Wendell num ato de desespero cômico.")
        elif evt_label == "evento_cap8_cozinha":
            $ add_shared_memory("cap8_cozinha", ["camille", "larissa"], "Sobrevivi à grande guerra de farinha no meio do canteiro de obras.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
    else:
        narrator "Fui até [local_escolhido], peguei alguns baldes de tinta e varri o chão."
        $ update_player_stat("energy", -5)
        
    call avancar_tempo(15)
    jump loop_mapa_cap8