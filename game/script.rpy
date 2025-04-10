# script.rpy
image bg room = "images/cenarios/first_room.png"
image p happy = "images/characters/personagem_happy.png"

label start:
    scene bg room with fade
    show p happy at center

    p "Olá, seja bem-vindo ao meu jogo!"
    jump capitulo1
