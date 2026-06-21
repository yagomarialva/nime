label capitulo1:
    # Desbloqueia o capítulo na galeria
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === ABERTURA: A CASA DA RUA AURORA ===
    play music campus_ambient fadein 2.0
    
    scene bg auditorium with fade

    narrator "O zumbido do ar condicionado era constante, quase como o som de uma respiração metálica tentando manter vivas as poucas pessoas na sala."
    narrator "Éramos apenas três. Três estranhos convocados para a última reunião do 'Edital de Moradia Cultural'."
    
    mc "Primavera... a estação em que o desespero financeiro nos faz assinar contratos que nem lemos direito."
    
    narrator "Apoiei o rosto na mão. A bolsa do Edital era a minha única chance de me manter na Faculdade Solária sem precisar de três empregos."
    
    # Apresentando apenas Nicole e Katia
    narrator "Duas fileiras à frente, uma garota loira lia o edital impresso com uma postura tão rígida que parecia usar os papéis como um escudo contra o mundo. O nome dela era Nicole."
    narrator "Longe dela, na última fileira, uma garota de cabelos escuros rabiscava algo furiosamente em um caderno. Ela mastigava chiclete ruidosamente, ignorando a tensão no ar. Essa era a Katia."
    
    mc "Três pessoas lutando por um teto grátis..."

    # === O DISCURSO DO PROFESSOR WENDELL ===
    show professor_wendell neutral at center
    
    narrator "O Professor Wendell Garcez subiu ao palco. Ele caminhava com o equilíbrio de quem conhecia todos os segredos do campus."
    
    professor_wendell "Bem-vindos. Vocês são os três primeiros selecionados do Edital da Rua Aurora, 57."
    
    narrator "A garota loira, Nicole, levantou a mão quase imediatamente."
    
    nicole "Com licença, Professor. O edital mencionava seis vagas. Onde estão os outros?"
    
    professor_wendell "Uma excelente observação, Nicole. Os outros três desistiram quando leram as letras miúdas. As vagas remanescentes serão preenchidas nas próximas semanas."
    
    narrator "Katia estourou uma bola de chiclete. O som ecoou pelo auditório vazio."
    
    katia "Letras miúdas? Você quer dizer a parte em que a casa tá caindo aos pedaços e nós somos a mão de obra escrava pra restaurar?"
    
    professor_wendell "Eu prefiro o termo 'Projeto de Restauração Colaborativa', Katia."
    
    narrator "Ele deu um passo à frente. Os olhos dele eram afiados."
    
    professor_wendell "A casa é antiga. O teto vaza. A pintura está descascando. Vocês têm moradia gratuita, mas precisam consertá-la e manter uma média acadêmica excelente. Falhem em qualquer um dos dois, e o edital é cancelado para todos."
    professor_wendell "Vocês precisam uns dos outros. Estão dispensados. As chaves estão na portaria."
    
    hide professor_wendell
    
    # === PREPARAÇÃO DO MAPA E EVENTOS ===
    narrator "O discurso foi curto e ameaçador. A sobrevivência na Solária dependia da nossa capacidade de não nos matarmos."
    
    mc "Bom, acho que é hora de explorar um pouco antes de ir para o desastre em que me meti."
    
    # Inicializando stats
    $ dia_atual = 1
    $ periodo_atual = 1
    
    # Registrando eventos do Capítulo 1 no EventManager
    $ game_events.events = {}
    
    $ game_events.add_event("biblioteca", "evento_nicole_limpeza", 1, [1, 2, 3])
    $ game_events.add_event("cinema", "evento_katia_caixas", 1, [1, 2, 3])

    # Dia 2 
    $ game_events.add_event("laboratorio", "evento_nicole_bolsa", 2, [1, 2, 3])
    $ game_events.add_event("cinema", "evento_katia_filme", 2, [1, 2, 3])

# === LOOP PRINCIPAL DO MAPA ===
label loop_mapa_cap1:
    if dia_atual >= 3:
        mc "O tempo livre acabou. Preciso voltar para a casa da Rua Aurora para o nosso primeiro jantar juntos."
        
        call capitulo1_terceira_escolha from _call_capitulo1_terceira_map
        jump capitulo1_final

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap1
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_nicole_limpeza":
            $ add_shared_memory("nicole_library", ["nicole"], "Nicole pesquisando furiosamente sobre restauração")
        elif evt_label == "evento_katia_caixas":
            $ add_shared_memory("katia_cinema", ["katia"], "Katia fugindo das caixas no escuro do cinema")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(10)
        
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(10)
        
    jump loop_mapa_cap1
            
# === FINAL DO CAPÍTULO 1 - CLIFFHANGER ===
label capitulo1_final:
    scene bg quarto_protagonista_noite with fade
    
    narrator "A primeira semana na Rua Aurora foi exaustiva. Me joguei na cama, sentindo cada músculo do corpo reclamar."
    
    mc "Sobrevivemos... Pelo menos por agora."
    
    narrator "Fechei os olhos, deixando o cansaço me levar."
    narrator "..."
    narrator "..."
    
    # Tentativa de tocar um som se existir. Evitamos crash usando condicional ou omitindo o arquivo físico e deixando só a narração
    # play sound "glass_shatter.ogg"
    narrator "CRASH!"
    
    narrator "O barulho foi agudo e violento. Vidro quebrando no andar de baixo. Seguido por um silêncio mortal."
    
    mc "Que merda foi essa?"
    
    narrator "Desci as escadas correndo, tateando no escuro da velha casa."
    
    scene bg sala_jantar with dissolve
    
    narrator "A luz pálida da rua iluminava a cozinha através da janela. Havia cacos de um prato espalhados pelo chão."
    narrator "E no canto, encolhida nas sombras, estava a garota que eu achava ser a mais forte e sarcástica de nós."
    narrator "Ela estava chorando silenciosamente, abraçada aos próprios joelhos, sussurrando para o vazio."
    
    "???" "Eles me acharam... Eu não posso... Eles me acharam..."
    
    mc "Ei... o que..."
    
    narrator "Ela levantou o rosto. O olhar dela cruzou com o meu. Puro terror."
    
    scene black with fade
    
    narrator "O Capítulo 1 chegou ao fim."
    
    if "capitulo2" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo2")
    
    jump capitulo2
