# script.rpy
image bg room = "images/cenarios/room.jpg"
image bg city = "images/cenarios/city.png"
image p happy = "images/characters/samantha/Samantha_falando_olho_aberto.png"
# image bg park 

#pontos
default points_samantha = 0
default points_katia = 0
default points_nicole = 0
default points_larissa = 0
default points_huey = 0
default points_camille = 0

label start:
    show screen affinity_points
    # sua história começa aqui
    jump prologo  # ou o label inicial da sua VN


