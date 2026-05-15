# === RETIRADA ESTRATÉGICA COM LARISSA ===
label capitulo1_caminhada_larissa:
    scene bg campus_night with fade
    show larissa sad at center
    
    narrator "Foi como soltar a válvula de uma panela de pressão. Assim que pisamos na rua vazia, Larissa sugou o ar noturno num fôlego quase doloroso."
    
    larissa "Muito cheiro de suor sujo. Muita gente trombando."
    
    narrator "As mãos dela, que antes esticavam o copo até quase arrebentá-lo, agora estavam enfiadas nos bolsos do casaco."
    
    larissa "Eu aguento bater cabeça num jogo, sofrer trombadas na quadra... Mas ali? Ali todo mundo esbarra sem querer. Ninguém tem uma posição certa."
    
    menu:
        "Entender a claustrofobia":
            $ points_larissa += 3
            mc "Todo o contato na festa parece um acidente sufocante. Não é um esporte, é um labirinto."
            larissa "Isso... Eu ia enlouquecer se ficasse parada mais dez segundos lá."
            
        "Tentar motivar":
            $ points_larissa += 1
            mc "Amanhã você corre na pista e esquece tudo isso."
            larissa "Pistas são boas. Elas têm linhas retas que a gente sabe para onde vão."
            
        "Silêncio solidário":
            $ points_larissa += 2
            narrator "Não falei nada. Caminhei arrastando os sapatos no asfalto molhado. O ritmo repetitivo dos meus passos pareceu acalmá-la."
            larissa "Gosto do ritmo que a gente tá andando."
            
    scene bg house_exterior_night with fade
    narrator "Chegamos ao muro de heras da república. Larissa parou e se encostou nele, desabando a postura perfeitamente atlética por uma fração de segundo."
    
    larissa "Eles acham que quem é do esporte adora gritaria em qualquer contexto."
    narrator "Ela chutou de leve uma pedrinha solta."
    larissa "Obrigada por notar que eu estava morrendo sem ar na porcaria daquele corredor."
    
    narrator "Com um aceno apressado, como se expor fraqueza fosse uma falta grave, ela sumiu para dentro de casa."
    jump capitulo1_quarta_escolha
