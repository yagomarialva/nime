# === EVENTO PLACEHOLDER / MINIGAMES ===
# Quando o jogador visita um local sem nenhum evento disponível.

label local_sem_evento(local_nome):
    if local_nome == "biblioteca":
        jump minigame_biblioteca
    elif local_nome == "cinema":
        jump minigame_cinema
    elif local_nome == "quadra":
        jump minigame_quadra
    else:
        scene black with dissolve
        mc "Nada pra fazer aqui agora."
        return
