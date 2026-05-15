# === O REFÚGIO DA ESTÁTICA COM CAMILLE ===
label capitulo1_caminhada_camille:
    scene bg campus_night with fade
    show camille sad at center
    
    narrator "A transição do calor esmagador da festa para a umidade congelante da rua foi como um choque elétrico. Camille abraçou os próprios ombros com força."
    
    camille "Pensei que perderia completamente o sinal."
    narrator "A voz dela, antes etérea e imponente, não passava de um sussurro rouco e cansado."
    
    mc "O sinal não sumiu. Só tinha muito ruído rasgando por cima."
    
    narrator "Caminhamos sobre a linha do meio-fio molhado. Sem contato. Apenas duas órbitas tristes rodando a mesma placa de rua no escuro."
    
    camille "Eles bebem para adormecer as incertezas, gritam para abafar a voz de dentro... tudo isso reverbera no espaço como uma unha num quadro negro cósmico."
    
    menu:
        "Tirar o peso dela":
            $ points_camille += 3
            mc "O peso não é seu, Camille. Pare de absorver os estilhaços de gente que não se importa."
            camille "..."
            narrator "Ela fechou os olhos fortemente, ofegando. Pela primeira vez percebeu que precisava blindar a si mesma antes do resto."
            
        "Mero observador prático":
            $ points_camille += 1
            mc "Eles só querem festejar porque as aulas estão prestes a massacrar eles em alguns meses."
            camille "Talvez sua lógica terrena faça a gravidade funcionar."
            
        "Ficar sem falar nada":
            $ points_camille += 2
            narrator "Engoli a teoria do porquê o ser humano é tão destrutivo quando socializa. O silêncio me pareceu um filtro melhor para nós dois."
            camille "O vazio que você projeta ao seu redor... é libertador."
            
    scene bg house_exterior_night with fade
    narrator "Paramos a cinco degraus da entrada de seu alojamento estufado de samambaias e bicicletas antigas."
    
    camille "Sua presença estancou o delírio elétrico que eu estava sentindo na mente."
    narrator "Por um instante, o aspecto de 'sábia milenar' desabou completamente, revelando uma garota amedrontada pelo mundo social bruto da faculdade."
    camille "Obrigada por notar que eu ia colapsar e criar uma desculpa fácil num mundo de mentiras fáceis."
    
    narrator "A porta bateu lentamente sobre a tranca. O silêncio retornou espesso, pesando ainda mais sabendo das rachaduras nas fundações mentais dela."
    jump capitulo1_quarta_escolha
