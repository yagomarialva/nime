# script.rpy - MELHORADO baseado em sucessos do gênero
default persistent.unlocked_chapters = []  # Lista de capítulos desbloqueados

# === SISTEMA DE AFINIDADE APRIMORADO ===
# Pontos de afinidade (0-100 para maior precisão)
default points_samantha = 0
default points_katia = 0
default points_nicole = 0
default points_larissa = 0
default points_huey = 0
default points_camille = 0

# Sistema de níveis de relacionamento
default relationship_samantha = "stranger"  # stranger -> acquaintance -> friend -> close_friend -> romantic
default relationship_katia = "stranger"
default relationship_nicole = "stranger"  
default relationship_larissa = "stranger"
default relationship_huey = "stranger"
default relationship_camille = "stranger"

# Flags de romance (agora com desenvolvimento orgânico)
default romance_samantha = False
default romance_nicole = False
default romance_huey = False
default romance_camille = False
default romance_larissa = False
default romance_katia = False

default status_samantha = "none"
default status_nicole = "none"
default status_huey = "none"
default status_camille = "none"
default status_larissa = "none"
default status_katia = "none"
default status_harem = "none"

# === SISTEMA NAKIGE (MOMENTOS EMOCIONAIS) ===
default emotional_moments_unlocked = []  # Lista de momentos emocionais desbloqueados
default player_empathy_level = 0  # Nível de empatia do jogador (afeta diálogos)

# === SISTEMA DE CRESCIMENTO MÚTUO ===
default character_growth_samantha = 0  # Crescimento pessoal de cada personagem
default character_growth_katia = 0
default character_growth_nicole = 0
default character_growth_larissa = 0
default character_growth_huey = 0
default character_growth_camille = 0

# === SISTEMA DE MEMÓRIAS COMPARTILHADAS ===
default shared_memories = []  # Lista de memórias especiais criadas com personagens

label start:
    # Inicializar o idioma salvo
    python:
        if hasattr(persistent, 'language') and persistent.language:
            lang = persistent.language
            if lang == "pt":
                renpy.change_language("portuguese")
            else:
                renpy.change_language("english")
        else:
            persistent.language = "en"
            renpy.change_language("english")
    
    # Pergunta o nome do jogador antes de abrir a UI do Flowchart
    scene black
    $ nome = renpy.input("Digite seu nome (ou deixe em branco para 'Jogador'):", length=20).strip()
    if nome == "":
        $ nome = "Jogador"
        
    # Sua história começa aqui (pelo Flowchart)
    jump flowchart_demo


