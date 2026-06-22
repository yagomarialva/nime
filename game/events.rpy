# === EVENTO PLACEHOLDER / MINIGAMES ===
# Quando o jogador visita um local sem nenhum evento disponível.

label local_sem_evento(local_nome):
    if local_nome == "biblioteca":
        jump minigame_biblioteca
    elif local_nome == "cinema":
        jump minigame_cinema
    elif local_nome == "quadra":
        jump minigame_quadra
    elif local_nome == "galeria":
        jump minigame_galeria
    elif local_nome == "laboratorio":
        jump minigame_laboratorio
    elif local_nome == "jogos":
        jump minigame_jogos
    elif local_nome == "quarto":
        jump quarto_protagonista
    elif local_nome in ["sala_jantar", "cozinha_escura", "quintal"]:
        if store.dia_atual >= 6 and store.dia_atual <= 7: # Estamos no capítulo 6 (reformas)
            if local_nome == "sala_jantar":
                jump minigame_reforma_sala
            elif local_nome == "cozinha_escura":
                jump minigame_reforma_cozinha
            elif local_nome == "quintal":
                jump minigame_reforma_quintal
        else:
            scene black with dissolve
            mc "A casa está tranquila por aqui. Sem reformas pendentes."
            return
    else:
        scene black with dissolve
        mc "Nada pra fazer aqui agora."
        return
