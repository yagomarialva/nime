# === PINTANDO O SILÊNCIO COM HUEY ===
label capitulo1_caminhada_huey:
    scene bg campus_night with fade
    show huey sad at center
    
    narrator "A iluminação amarelada dos postes antigos do campus recaiu sobre nós. Huey parou de andar por um instante cruzando os braços, respirando devagar."
    
    huey "A paleta de cores lá dentro era muito agressiva. Eu podia sentir o neon riscando meus pensamentos."
    
    narrator "Eu não tinha certeza se ela estava usando uma metáfora visual profunda ou se estava apenas farta de lasers na cara."
    
    mc "Acho que as festas universitárias não são pensadas com o impressionismo em mente."
    
    narrator "Ela esboçou um sorriso fraco, os olhos varrendo os tijolos descascados dos corredores."
    
    huey "Obrigada por me guiar pra porta. Eu estava quase derretendo na escada."
    
    menu:
        "Frieza compassiva":
            $ points_huey += 3
            mc "Você parecia paralisada. Era a pior galeria que poderíamos visitar hoje. Só te dei uma saída."
            huey "A... pior galeria. Essa foi boa."
            
        "Silêncio observador":
            $ points_huey += 2
            narrator "Continuei de olhos focados no caminho a nossa frente, me recusando a forçá-la a falar mais do que queria."
            huey "Seu silêncio tem uma cor boa."
            
        "Mudar de assunto":
            $ points_huey += 1
            mc "Amanhã os blocos de arte vão ter obras muito mais brandas."
            huey "Sim. Formas que respiram com calma."
            
    scene bg house_exterior_night with fade
    narrator "Chegamos em frente ao pátio da fundação onde ela morava. Manchas de tinta pichada enfeitavam a calçada."
    
    huey "Acho que minha tela mental ficou suja pela estática musical."
    narrator "Ela agarrou a alça da bolsa com as duas mãos, desviando o olhar."
    huey "Eu estive prestes a chorar de irritação lá dentro. Foi muito bom não precisar explicar por quê te pedi para irmos embora."
    
    narrator "Ela desapareceu no pátio escuro, flutuando como um contorno aquarelado borrado na noite."
    jump capitulo1_quarta_escolha
