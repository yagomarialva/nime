# Definição dos personagens
define narrator = Character(None)  # Narrador sem nome
define nicole = Character("Nicole", color="#FF69B4")  # Cor opcional para o nome
define katia = Character("Katia", color="#8A2BE2")
define larissa = Character("Larissa", color="#FFD700")
define huey = Character("Aline (Huey)", color="#00CED1")
define samantha = Character("Samantha", color="#FF4500")
define camille = Character("Camille", color="#32CD32")
define professor_wendell = Character("Professor Wendell", color="#6202bbff")
define ex_camille = Character("Ex de Camille", color="#6A5ACD")
define ex_samantha = Character("Ex de Samantha", color="#FFD700")
define ex_nicole = Character("Ex de Nicole", color="#00CED1")
define ex_katia = Character("Ex de Katia", color="#FF4500")
define ex_huey = Character("Ex de Huey", color="#32CD32")
define ex_larissa = Character("Ex de Larissa", color="#FF5733")
# Imagem de sombra genérica para emoções ausentes
image shadow = "images/characters/shadow.png"

# Personagens e emoções
image samantha happy = "images/characters/samantha/samantha_happy.png" if renpy.exists("images/characters/samantha/samantha_happy.png") else "images/characters/shadow.png"
image samantha neutral = "images/characters/samantha/samantha_neutral.png" if renpy.exists("images/characters/samantha/samantha_neutral.png") else "images/characters/shadow.png"
image samantha angry = "images/characters/samantha/samantha_angry.png" if renpy.exists("images/characters/samantha/samantha_angry.png") else "images/characters/shadow.png"
image samantha sad = "images/characters/samantha/samantha_sad.png" if renpy.exists("images/characters/samantha/samantha_sad.png") else "images/characters/shadow.png"
image samantha blush = "images/characters/samantha/samantha_blush.png" if renpy.exists("images/characters/samantha/samantha_blush.png") else "images/characters/shadow.png"

image nicole neutral = "images/characters/nicole/nicole_neutral.png" if renpy.exists("images/characters/nicole/nicole_neutral.png") else "images/characters/shadow.png"
image nicole happy = "images/characters/nicole/nicole_happy.png" if renpy.exists("images/characters/nicole/nicole_happy.png") else "images/characters/shadow.png"
image nicole angry = "images/characters/nicole/nicole_angry.png" if renpy.exists("images/characters/nicole/nicole_angry.png") else "images/characters/shadow.png"
image nicole sad = "images/characters/nicole/nicole_sad.png" if renpy.exists("images/characters/nicole/nicole_sad.png") else "images/characters/shadow.png"
image nicole blush = "images/characters/nicole/nicole_blush.png" if renpy.exists("images/characters/nicole/nicole_blush.png") else "images/characters/shadow.png"

image katia neutral = "images/characters/katia/katia_neutral.png" if renpy.exists("images/characters/katia/katia_neutral.png") else "images/characters/shadow.png"
image katia blush = "images/characters/katia/katia_blush.png" if renpy.exists("images/characters/katia/katia_blush.png") else "images/characters/shadow.png"
image katia angry = "images/characters/katia/katia_angry.png" if renpy.exists("images/characters/katia/katia_angry.png") else "images/characters/shadow.png"
image katia sad = "images/characters/katia/katia_sad.png" if renpy.exists("images/characters/katia/katia_sad.png") else "images/characters/shadow.png"
image katia happy = "images/characters/katia/katia_happy.png" if renpy.exists("images/characters/katia/katia_happy.png") else "images/characters/shadow.png"

image larissa neutral = "images/characters/larissa/larissa_neutral.png" if renpy.exists("images/characters/larissa/larissa_neutral.png") else "images/characters/shadow.png"
image larissa happy = "images/characters/larissa/larissa_happy.png" if renpy.exists("images/characters/larissa/larissa_happy.png") else "images/characters/shadow.png"
image larissa voley = "images/characters/larissa/larissa_volei.png" if renpy.exists("images/characters/larissa/larissa_volei.png") else "images/characters/shadow.png"
image larissa angry = "images/characters/larissa/larissa_angry.png" if renpy.exists("images/characters/larissa/larissa_angry.png") else "images/characters/shadow.png"
image larissa sad = "images/characters/larissa/larissa_sad.png" if renpy.exists("images/characters/larissa/larissa_sad.png") else "images/characters/shadow.png"
image larissa blush = "images/characters/larissa/larissa_blush.png" if renpy.exists("images/characters/larissa/larissa_blush.png") else "images/characters/shadow.png"

image huey neutral = "images/characters/hu_wei/hu_wei_neutral.png" if renpy.exists("images/characters/hu_wei/hu_wei_neutral.png") else "images/characters/shadow.png"
image huey happy = "images/characters/hu_wei/hu_wei_happy.png" if renpy.exists("images/characters/hu_wei/hu_wei_happy.png") else "images/characters/shadow.png"
image huey angry = "images/characters/hu_wei/hu_wei_angry.png" if renpy.exists("images/characters/hu_wei/hu_wei_angry.png") else "images/characters/shadow.png"
image huey sad = "images/characters/hu_wei/hu_wei_sad.png" if renpy.exists("images/characters/hu_wei/hu_wei_sad.png") else "images/characters/shadow.png"
image huey voley = "images/characters/hu_wei/hu_wei_volei.png" if renpy.exists("images/characters/hu_wei/hu_wei_volei.png") else "images/characters/shadow.png"
image huey blush = "images/characters/hu_wei/hu_wei_blush.png" if renpy.exists("images/characters/hu_wei/hu_wei_blush.png") else "images/characters/shadow.png" 

image camille neutral = "images/characters/camille/camille_neutral.png" if renpy.exists("images/characters/camille/camille_neutral.png") else "images/characters/shadow.png"
image camille happy = "images/characters/camille/camille_happy.png" if renpy.exists("images/characters/camille/camille_happy.png") else "images/characters/shadow.png"
image camille angry = "images/characters/camille/camille_angry.png" if renpy.exists("images/characters/camille/camille_angry.png") else "images/characters/shadow.png"
image camille sad = "images/characters/camille/camille_sad.png" if renpy.exists("images/characters/camille/camille_sad.png") else "images/characters/shadow.png"
image camille blush = "images/characters/camille/camille_blush.png" if renpy.exists("images/characters/camille/camille_blush.png") else "images/characters/shadow.png"

image professor_wendell neutral = "images/characters/professor_wendell/professor_wendell.png" if renpy.exists("images/characters/professor_wendell/professor_wendell.png") else "images/characters/shadow.png"
image professor_wendell happy = "images/characters/professor_wendell/professor_wendell_happy.png" if renpy.exists("images/characters/professor_wendell/professor_wendell_happy.png") else "images/characters/shadow.png"
image professor_wendell angry = "images/characters/professor_wendell/professor_wendell_angry.png" if renpy.exists("images/characters/professor_wendell/professor_wendell_angry.png") else "images/characters/shadow.png"
image professor_wendell sad = "images/characters/professor_wendell/professor_wendell_sad.png" if renpy.exists("images/characters/professor_wendell/professor_wendell_sad.png") else "images/characters/shadow.png"