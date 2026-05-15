# === EVENTO GALERIA: HUEY E CAMILLE ===
# Tema: O sangramento caótico das tintas contra a energia etérea

label evento_huey_camille:
    scene bg gallery with fade
    
    narrator "O corredor da galeria de exposição da Faculdade Solária cheirava a terebintina e gesso úmido. As janelas abertas traziam a promessa doentia e instável do entardecer."
    
    show huey sad at left
    show camille neutral at right
    
    narrator "Huey encarava os próprios dedos borrados de vermelho vivo e ocre. Seus ombros estavam tensos. À sua frente, no chão, havia uma tela destruída de formas abruptas."
    narrator "A alguns passos meticulosamente medidos dela, Camille mantinha as palmas das mãos abertas na altura da cintura, como quem tentasse evitar que fumaça subisse ao teto."
    
    camille "Sua frequência exposta nesta tela corta a aura do recinto. É tão dolorosa... tão ancorada na carne."
    
    huey "A carne dói. Tentar varrer ela pro cosmos com musiquinha de meditação e energia branca não vai curar o sangramento debaixo da pele, Camille."
    
    narrator "As sobrancelhas de Camille oscilaram levemente, um lapso de perturbação no verniz da santidade serena dela."
    
    camille "Você emula a dor porque tem medo da cura. Você não gosta das formas tortas do quadro, gosta do fato de que todo mundo afasta o olhar ao ver."
    
    narrator "A artista mordeu o polegar até clarear a unha."
    huey "Você nunca teve sujeira de verdade nas unhas e tenta curar as manchas dos outros. Ignorância limpa é quase hipocrisia transcendental."
    
    narrator "As sombras no teto alongavam as distâncias do recinto. Um microcosmo da frustração espiritual versus a angústia física."
    
    mc "Acho que nem o quadro, nem os incensos cósmicos resolvem nada quando vocês só não querem olhar para o próprio reflexo vazio."
    
    narrator "A voz morta cortando o debate não gerou raiva espalhafatosa. Deixou apenas o atrito silenciado latejando. Ninguém piscou as pálpebras por dez segundos absolutos."
    
    menu:
        "Validar a mancha da vida (Huey)":
            $ points_huey += 3
            mc "Pelo menos a tela suja é honesta com a feiura do que está aqui em baixo. O cosmos não sangra."
            huey "Finalmente."
            camille "Honestidade presa num abismo só machuca quem decide ficar lá de companhia com ela."
            
        "Ancorar a calmaria falsa (Camille)":
            $ points_camille += 3
            mc "A mancha é desgastante. Expirar sem tentar lamber a própria ferida pode ser menos ridículo."
            camille "A energia se dissipa se não a alimentarmos."
            huey "Covardes que fogem da sujeira do sangue com desculpas estelares."
            
    narrator "Huey recolheu bruscamente um pano grosso e começou a esfregar a tinta no tecido até a fricção queimar sua pele."
    narrator "Camille andou em silêncio até a janela, exalando bruscamente, provando que sua energia estava muito menos alinhada que supunha."
    narrator "Tentei acreditar que o entardecer não tinha as mesmas cores das feridas na tela da Huey. Eu falhei dolorosamente."
    
    return
