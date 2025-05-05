label epilogo:
    scene bg carta_manha with fade
    narrator "Meses se passaram desde o último dia na república. A vida seguiu, lenta e inevitável. Mas em uma manhã cinzenta, uma carta chega. Papel reciclado. Caligrafia familiar."

    # Verifica se o protagonista terminou o jogo romanticamente com alguém
    if romance_samantha:
        jump epilogo_samantha
    elif romance_nicole:
        jump epilogo_nicole
    elif romance_katia:
        jump epilogo_katia
    elif romance_camille:
        jump epilogo_camille
    elif romance_larissa:
        jump epilogo_larissa
    elif romance_huey:
        jump epilogo_huey
    else:
        jump epilogo_coletivo

# Epílogo para Samantha
label epilogo_samantha:
    show carta_samantha at center
    narrator "A carta é de Samantha."
    samantha "Ei! Você não imagina a fase nova da minha campanha. Baseei um NPC em você… espero que não fique bravo com o carisma 20."
    samantha "Sinto saudade do nosso último chefe juntos — aquele chamado 'despedida'."
    samantha "Vamos marcar uma nova missão logo, ok?"
    samantha "E... se ainda quiser ser meu player 2, sua ficha tá reservada."
    narrator "🖊 Com carinho (e crítica de acerto), Sam."
    jump epilogo_final

# Epílogo para Nicole
label epilogo_nicole:
    show carta_nicole at center
    narrator "A carta é de Nicole."
    nicole "Preciso de você para revisar uma nova planilha. Mas é confidencial... envolve datas de encontros futuros, probabilidades de beijos e projeções de felicidade."
    nicole "E sim, essa é minha maneira esquisita de dizer: Sinto sua falta."
    nicole "Me deixa saber se... você ainda me escolhe."
    narrator "🖊 Com racionalidade afetuosa, Nicole."
    jump epilogo_final

# Epílogo para Katia
label epilogo_katia:
    show carta_katia at center
    narrator "A carta é de Katia."
    katia "Você deixou seu carregador aqui. E um monte de lembranças irritantes."
    katia "Toda vez que vejo um roteiro bem escrito, lembro das nossas conversas idiotas."
    katia "Me odeie por isso. Ou me escreva de volta. Tanto faz."
    katia "(Mas se escrever... assina com seu nome. Gosto de ler ele no final.)"
    narrator "🖊 Katia."
    jump epilogo_final

# Epílogo para Camille
label epilogo_camille:
    show carta_camille at center
    narrator "A carta é de Camille."
    camille "Meu novo cristal vibrou quando ouvi seu nome no vento."
    camille "Sim, ainda sinto você."
    camille "Espero que o tempo esteja sendo gentil aí… aqui ele dança comigo."
    camille "Se um dia quiser dançar também, você sabe onde me encontrar."
    narrator "🖊 Energeticamente, Camille."
    jump epilogo_final

# Epílogo para Larissa
label epilogo_larissa:
    show carta_larissa at center
    narrator "A carta é de Larissa."
    larissa "O treino hoje foi puxado, mas acho que o que mais me cansou foi a saudade."
    larissa "Você me faz querer vencer as provas do coração — e olha que isso eu não aprendi na pista."
    larissa "Topa correr comigo na próxima etapa da vida?"
    narrator "🖊 Com suor e sorrisos, Lari."
    jump epilogo_final

# Epílogo para Huey
label epilogo_huey:
    show carta_huey at center
    narrator "A carta é de Huey."
    huey "Pintei um quadro com cor nova. Chamei de 'Sentimento que ainda não entendo'."
    huey "Acho que você é minha paleta favorita."
    huey "Se quiser… posso deixar um espaço em branco só pra você terminar."
    narrator "🖊 Com tinta e ternura, Huey."
    jump epilogo_final

# Epílogo coletivo (sem romance)
label epilogo_coletivo:
    show carta_coletiva at center
    narrator "A carta é de todos os moradores, escrita coletivamente."
    narrator "Ei, desaparecido! A gente tá bem. A saudade existe, mas ela virou combustível."
    narrator "Estamos planejando um reencontro. Pode ser um café. Pode ser uma maratona de filmes. Pode ser só um silêncio confortável."
    narrator "O que importa é que você esteja lá."
    narrator "🖊 Com carinho (e gritaria), A república toda."
    jump epilogo_final

# Cena final
label epilogo_final:
    scene bg republica_foto with fade
    narrator "O tempo passou, mas o que foi vivido permanece."
    narrator "A Rua Aurora pode ter deixado de ser endereço…"
    narrator "…mas virou um lugar eterno dentro de cada um deles."

    show foto_republica at center
    narrator "📷 Uma imagem da república — todos rindo, de pijama, segurando travesseiros ou tintas, com a legenda:"
    narrator "\"Obrigado por jogar. Rua Aurora para sempre.\""

    return

