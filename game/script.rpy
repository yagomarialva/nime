# script.rpy

# Cenários
image bg room = "images/cenarios/room.jpg"
image bg city = "images/cenarios/city.png"
image bg cinema = "images/cenarios/cinema.png"
image bg cinema_katia_samantha = "images/cenarios/scene/cinema_katia_samantha.png"
image bg cinema_exhibition = "images/cenarios/scene/amostra_filmes_katia_samantha.png"
image bg cinema_cafe = "images/cenarios/scene/cinema_lobby.png"
image bg cinema_cafeteria = "images/cenarios/Cafeteria.png"
image bg cinema_lobby_empty = "images/cenarios/cinema_lobby.png"
image bg cinema_arcade = "images/cenarios/Arcade.jpg"
image bg quadra_volei = "images/cenarios/QUADRA.png"
# Adicione outros cenários conforme necessário
# image bg park = "images/cenarios/park.jpg"

# Definição dos personagens
define narrator = Character(None)  # Narrador sem nome
define nicole = Character("Nicole", color="#FF69B4")  # Cor opcional para o nome
define katia = Character("Katia", color="#8A2BE2")
define larissa = Character("Larissa", color="#FFD700")
define Huey = Character("Aline (Huey)", color="#00CED1")
define samantha = Character("Samantha", color="#FF4500")
define camille = Character("Camille", color="#32CD32")


# Personagens
image samantha happy = "images/characters/samantha/samantha 382x395.png"
image nicole neutral = "images/characters/nicole/Nicole_neutra.png"
image katia neutral = "images/characters/katia/katia_neutral.png"
image larissa happy = "images/characters/larissa/Larissa_feliz.png"
image huey neutral = "images/characters/huey/Huey_neutra.png"
image camille neutral = "images/characters/camille/Camille_neutra.png"

# Pontos de afinidade
default points_samantha = 0
default points_katia = 0
default points_nicole = 0
default points_larissa = 0
default points_huey = 0
default points_camille = 0

label start:
    show screen affinity_points
    # Sua história começa aqui
    jump prologo  # ou o label inicial da sua VN


