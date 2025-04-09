# Declarações de personagens
define p = Character("Samantha", color="#c8ffc8")
define j = Character("Jogador", color="#ffffff")

# Imagens
image bg room = "images/cenarios/first_room.png"
image p happy = "images/characters/personagem_happy.png"

# Começo do jogo
label start:
    scene bg room with fade
    show p happy at center

    p "Olá, seja bem-vindo ao meu jogo!"
    
    j "Oi, tudo bem?"
    
    p "Sim! Vamos começar a aventura!"
    
    menu:
        "Vamos ao parque!":
            p "Ótimo! Vamos ao parque!"
            jump park

        "Vamos ao shopping!":
            p "Interessante, vamos ao shopping!"
            jump shopping

label park:
    scene bg room
    show p happy at center
    p "Aqui no parque é tão tranquilo..."
    return

label shopping:
    scene bg room
    show p happy at center
    p "Eu adoro o shopping, sempre tem muitas lojas legais!"
    return
