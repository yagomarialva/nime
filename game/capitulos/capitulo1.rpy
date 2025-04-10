label capitulo1:
    scene bg room with fade
    show p happy at center

    j "Oi, tudo bem?"
    p "Sim! Vamos começar a aventura!"

    menu:
        "Vamos ao parque!":
            p "Ótimo! Vamos ao parque!"
            # jump park
            jump capitulo2
        "Vamos ao shopping!":
            p "Interessante, vamos ao shopping!"
            # jump shopping
            jump capitulo2
        