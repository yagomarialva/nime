label capitulo13:
    if "capitulo13" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo13")
        
    scene bg faculdade with fade
    
    narrator "O fim de semana passou voando."
    
    narrator "A tempestade emocional do nosso último encontro ainda pairava no ar. Eu sabia que as consequências das minhas palavras daquele dia iriam ditar o resto do semestre."
    
    if escolha_fogos == "larissa":
        jump capitulo13_larissa
    elif escolha_fogos == "camille":
        jump capitulo13_camille
    elif escolha_fogos == "samantha":
        jump capitulo13_samantha
    elif escolha_fogos == "katia":
        jump capitulo13_katia
    elif escolha_fogos == "nicole":
        jump capitulo13_nicole
    elif escolha_fogos == "huey":
        jump capitulo13_huey
    elif escolha_fogos == "harem" or escolha_fogos == "grupo":
        jump capitulo13_harem
