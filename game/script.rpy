# script.rpy

# Cenários
image bg room = "images/cenarios/room.jpg"
image bg city = "images/cenarios/city.png"
# Adicione outros cenários conforme necessário
# image bg park = "images/cenarios/park.jpg"

# Definição dos personagens
define narrator = Character(None)  # Narrador sem nome
define nicole = Character("Nicole", color="#FF69B4")  # Cor opcional para o nome
define katia = Character("Katia", color="#8A2BE2")
define larissa = Character("Larissa", color="#FFD700")
define huey = Character("Aline (Huey)", color="#00CED1")
define samantha = Character("Samantha", color="#FF4500")
define camille = Character("Camille", color="#32CD32")


# Personagens
image samantha happy = "images/characters/samantha/Samantha_falando_olho_aberto.png"
image nicole neutral = "images/characters/samantha/Nicole_neutra.png"
image katia neutral = "images/characters/samantha/Katia_neutra.png"
image larissa happy = "images/characters/samantha/Larissa_feliz.png"
image huey neutral = "images/characters/samantha/Huey_neutra.png"
image camille neutral = "images/characters/samantha/Camille_neutra.png"

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


