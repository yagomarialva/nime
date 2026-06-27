label capitulo15:
    if "capitulo15" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo15")
        
    scene black with fade
    
    narrator "A faculdade era um microcosmo."
    narrator "Um pequeno mundo com leis próprias, onde o maior problema da nossa vida poderia ser uma prova de anatomia ou uma conta de luz atrasada."
    
    narrator "Mas a bolha estourou. Nós fomos lançados na vida adulta."
    narrator "Cinco longos anos se passaram desde que a chave da casa na Rua Aurora foi entregue."
    
    narrator "Muitas coisas mudaram. As promessas feitas na juventude foram testadas pela distância, pelo trabalho e pela realidade pragmática dos adultos."
    
    if escolha_fogos == "larissa":
        jump capitulo15_larissa
    elif escolha_fogos == "camille":
        jump capitulo15_camille
    elif escolha_fogos == "samantha":
        jump capitulo15_samantha
    elif escolha_fogos == "katia":
        jump capitulo15_katia
    elif escolha_fogos == "nicole":
        jump capitulo15_nicole
    elif escolha_fogos == "huey":
        jump capitulo15_huey
    elif escolha_fogos == "harem" or escolha_fogos == "grupo":
        jump capitulo15_harem
