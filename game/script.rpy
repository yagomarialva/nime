# script.rpy
default persistent.unlocked_chapters = []  # Lista de capítulos desbloqueados
# Pontos de afinidade
default points_samantha = 0
default points_katia = 0
default points_nicole = 0
default points_larissa = 0
default points_huey = 0
default points_camille = 0

default romance_samantha = False
default romance_nicole = False
default romance_huey = False
default romance_camille = False
default romance_larissa = False
default romance_katia = False

label start:
    show screen affinity_points
    # Sua história começa aqui
    jump prologo  # ou o label inicial da sua VN


