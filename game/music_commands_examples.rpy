# === EXEMPLOS DE COMANDOS DE MÚSICA ===
# Este arquivo contém exemplos de como usar música no Ren'Py
# Você pode copiar e colar estes comandos em seus arquivos .rpy

# === COMANDOS BÁSICOS DE MÚSICA ===

# Tocar música (substitui a música atual)
play music "nome_da_musica.ogg"

# Tocar música com fade in (entrada suave)
play music "nome_da_musica.ogg" fadein 2.0

# Parar música
stop music

# Parar música com fade out (saída suave)
stop music fadeout 3.0

# Tocar música em loop (padrão)
play music "nome_da_musica.ogg" loop

# Tocar música uma vez só (não loop)
play music "nome_da_musica.ogg" noloop

# === COMANDOS DE EFEITOS SONOROS ===

# Tocar efeito sonoro
play sound "nome_do_som.ogg"

# Tocar efeito sonoro com fade in
play sound "nome_do_som.ogg" fadein 1.0

# Parar efeito sonoro
stop sound

# === EXEMPLOS PRÁTICOS ===

# Música de menu principal
play music main_menu fadein 2.0

# Música de ambiente do campus
play music campus_ambient fadein 3.0

# Música de festa
play music party fadein 2.0

# Música romântica
play music romantic_moment fadein 2.0

# Música triste
play music sad_moment fadein 2.0

# Música misteriosa
play music mysterious_moment fadein 2.0

# Tema de personagem
play music nicole_theme fadein 2.0

# Transição entre cenas
play music scene_transition fadein 1.0

# Parar música atual e tocar nova
stop music fadeout 2.0
play music happy_moment fadein 2.0

# === EXEMPLOS DE USO EM CENÁRIOS ===

# Biblioteca (ambiente silencioso)
play music library_ambient fadein 2.0

# Cinema (ambiente cultural)
play music cinema_ambient fadein 2.0

# Quadra esportiva (ambiente energético)
play music sports_ambient fadein 2.0

# Sessão de estudo
play music study_session fadein 2.0

# Festival
play music festival fadein 2.0

# === EXEMPLOS DE USO EM MOMENTOS ESPECÍFICOS ===

# Momento emocional
play music emotional_moment fadein 2.0

# Momento de descoberta
play music discovery_moment fadein 2.0

# Momento de tensão
play music tension_moment fadein 2.0

# Momento de alívio
play music relief_moment fadein 2.0

# === EXEMPLOS DE USO COM PERSONAGENS ===

# Aparecimento da Nicole
play music nicole_theme fadein 2.0

# Aparecimento da Camille
play music camille_theme fadein 2.0

# Aparecimento da Katia
play music katia_theme fadein 2.0

# Aparecimento da Huey
play music huey_theme fadein 2.0

# Aparecimento da Samantha
play music samantha_theme fadein 2.0

# Aparecimento da Larissa
play music larissa_theme fadein 2.0

# === EXEMPLOS DE TRANSIÇÕES ===

# Transição entre capítulos
stop music fadeout 3.0
play music chapter_transition fadein 2.0

# Transição entre cenas
play music scene_transition fadein 1.0

# Final do jogo
play music ending_theme fadein 3.0

# Créditos
play music credits fadein 2.0
