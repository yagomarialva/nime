label capitulo10:
    if "capitulo10" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo10")
        
    scene bg casa_interior with fade
    
    narrator "A magia do Festival de Primavera durou exatamente um fim de semana."
    
    narrator "Na segunda-feira de manhã, o Professor Wendell bateu na nossa porta recém-reformada com uma pilha de cronogramas impressos."
    
    show professor_wendell neutral at center
    
    professor_wendell "A reforma estonteante garantiu a casa. Mas as regras acadêmicas da Universidade continuam valendo."
    
    professor_wendell "A Semana de Provas Finais começa na segunda-feira que vem. Qualquer morador desta casa que fechar o semestre com média inferior a 7.0 terá a vaga na residência revogada."
    
    show katia angry at left
    show larissa sad at right
    
    katia "O quê?! Mas a gente perdeu semanas de estudo limpando fumaça e passando argamassa no teto!"
    
    professor_wendell "A burocracia é implacável, Srta. Katia. Sugiro que troquem os martelos por livros."
    
    narrator "Ele saiu, deixando um silêncio aterrorizante na sala."
    
    larissa "Eu... eu tenho três provas teóricas pra salvar minha bolsa de esportes."
    
    hide professor_wendell
    hide katia
    hide larissa
    
    narrator "O pânico se instaurou. A casa virou um acampamento de guerra de estudos. Pilhas de livros, garrafas de café e marca-textos dominaram a mesa de jantar."
    
    narrator "Mas, no meio desse caos absoluto, meus pensamentos acabavam voltando para o que aconteceu na noite do festival."
    
    narrator "O tempo no telhado, durante os fogos de artifício, mudou a dinâmica daqui pra sempre. E eu sabia exatamente em quem eu precisava focar agora."
    
    # Ramificação baseada na escolha do Capítulo 9
    if not hasattr(store, 'escolha_fogos'):
        $ escolha_fogos = "grupo" # Fallback de segurança
        
    if escolha_fogos == "larissa":
        jump capitulo10_larissa
    elif escolha_fogos == "camille":
        jump capitulo10_camille
    elif escolha_fogos == "samantha":
        jump capitulo10_samantha
    elif escolha_fogos == "katia":
        jump capitulo10_katia
    elif escolha_fogos == "nicole":
        jump capitulo10_nicole
    elif escolha_fogos == "huey":
        jump capitulo10_huey
    else:
        jump capitulo10_harem