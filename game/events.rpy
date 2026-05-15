# === EVENTO PLACEHOLDER ===
# Quando o jogador visita um local sem nenhum evento disponível.

label local_sem_evento(local_nome):
    # Pode futuramente ter um if/elif para mostrar o background correto
    # dependendo do local_nome (ex: if local_nome == "biblioteca": scene bg library)
    # Por agora, escurece a tela para focar na mensagem
    scene black with dissolve
    
    mc "Nada pra fazer aqui agora."
    
    # Retorna IMEDIATAMENTE ao mapa
    return
