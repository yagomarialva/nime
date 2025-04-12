define sombra = Character("Narrador", color="#A9A9A9")  # Personagem misterioso e sombreado

label prologo:

    scene bg city with fade  # Substitua por sua imagem real

    sombra "Este jogo é recomendado para maiores de 18 anos."
    sombra "Você confirma que tem 18 anos ou mais?"

    menu:
        "Sim, tenho 18 anos ou mais.":
            jump nome_jogador

        "Não, sou menor de idade.":
            sombra "Infelizmente, você não poderá jogar este jogo. Obrigado pela compreensão!"
            return

label nome_jogador:
    scene bg city with fade

    $ nome = renpy.input("Digite seu nome:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Jogador"

    sombra "Olá, [nome]. Seja bem-vindo(a)!"

    jump aviso_jogo

label aviso_jogo:
    scene bg city with fade
    with dissolve

    sombra "Todos os personagens deste jogo possuem 18 anos ou mais."
    sombra "Apesar de abordar relacionamentos e temas maduros, este NÃO é um jogo pornográfico."
    sombra "Nosso foco está na construção de narrativa, romance e escolhas com consequências."
    sombra "Esperamos que aproveite sua jornada com responsabilidade e respeito."

    jump capitulo1
