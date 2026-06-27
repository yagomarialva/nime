label capitulo12:
    if "capitulo12" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo12")
        
    scene bg faculdade with fade
    
    narrator "As férias de inverno acabaram tão rápido quanto começaram."
    
    narrator "A neve derreteu, os casacos grossos voltaram para os armários, e o campus da universidade voltou a fervilhar com o barulho dos alunos."
    
    narrator "Este era o último semestre. A reta final. O momento em que o futuro deixava de ser uma ideia distante e passava a ser uma realidade ameaçadora."
    
    narrator "Para alguns, era apenas uma questão de colar grau. Mas para nós, moradores da Rua Aurora..."
    
    scene bg casa_interior with dissolve
    
    narrator "O universo parecia ter guardado o pior obstáculo exatamente para o final."
    
    if escolha_fogos == "larissa":
        jump capitulo12_larissa
    elif escolha_fogos == "camille":
        jump capitulo12_camille
    elif escolha_fogos == "samantha":
        jump capitulo12_samantha
    elif escolha_fogos == "katia":
        jump capitulo12_katia
    elif escolha_fogos == "nicole":
        jump capitulo12_nicole
    elif escolha_fogos == "huey":
        jump capitulo12_huey
    elif escolha_fogos == "harem" or escolha_fogos == "grupo":
        jump capitulo12_harem
