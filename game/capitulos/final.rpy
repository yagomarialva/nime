label epilogo:
    if "epilogo" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("epilogo")
    
    scene bg carta_manha with fade
    narrator "Meses se passaram desde o último dia na república. A vida seguiu, lenta e inevitável. Mas em uma manhã cinzenta, uma carta chega. Papel reciclado. Caligrafia familiar."
    
    # Momento emocional de recebimento da carta
    call emotional_moment("letter_arrival", None, "Chegada da carta após meses de separação") from _call_emotional_moment_epilogo_1
    
    narrator "Era um momento de reencontro, onde os corações se preparavam para se reconectar após meses de separação."

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
    
    # Momento emocional com Samantha
    call emotional_moment("letter_samantha", None, "Carta especial de Samantha") from _call_emotional_moment_epilogo_2
    
    $ add_shared_memory("epilogue_letter_samantha", ["samantha"], "Carta de reencontro de Samantha")
    $ add_affinity_points("samantha", 8, "Carta de reencontro romântica")
    
    jump epilogo_final

# Epílogo para Nicole
label epilogo_nicole:
    show carta_nicole at center
    narrator "A carta é de Nicole."
    nicole "Preciso de você para revisar uma nova planilha. Mas é confidencial... envolve datas de encontros futuros, probabilidades de beijos e projeções de felicidade."
    nicole "E sim, essa é minha maneira esquisita de dizer: Sinto sua falta."
    nicole "Me deixa saber se... você ainda me escolhe."
    narrator "🖊 Com racionalidade afetuosa, Nicole."
    
    # Momento emocional com Nicole
    call emotional_moment("letter_nicole", None, "Carta especial de Nicole") from _call_emotional_moment_epilogo_3
    
    $ add_shared_memory("epilogue_letter_nicole", ["nicole"], "Carta de reencontro de Nicole")
    $ add_affinity_points("nicole", 8, "Carta de reencontro romântica")
    
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
    
    # Momento emocional com Katia
    call emotional_moment("letter_katia", None, "Carta especial de Katia") from _call_emotional_moment_epilogo_4
    
    $ add_shared_memory("epilogue_letter_katia", ["katia"], "Carta de reencontro de Katia")
    $ add_affinity_points("katia", 8, "Carta de reencontro romântica")
    
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
    
    # Momento emocional com Camille
    call emotional_moment("letter_camille", None, "Carta especial de Camille") from _call_emotional_moment_epilogo_5
    
    $ add_shared_memory("epilogue_letter_camille", ["camille"], "Carta de reencontro de Camille")
    $ add_affinity_points("camille", 8, "Carta de reencontro romântica")
    
    jump epilogo_final

# Epílogo para Larissa
label epilogo_larissa:
    show carta_larissa at center
    narrator "A carta é de Larissa."
    larissa "O treino hoje foi puxado, mas acho que o que mais me cansou foi a saudade."
    larissa "Você me faz querer vencer as provas do coração — e olha que isso eu não aprendi na pista."
    larissa "Topa correr comigo na próxima etapa da vida?"
    narrator "🖊 Com suor e sorrisos, Lari."
    
    # Momento emocional com Larissa
    call emotional_moment("letter_larissa", None, "Carta especial de Larissa") from _call_emotional_moment_epilogo_6
    
    $ add_shared_memory("epilogue_letter_larissa", ["larissa"], "Carta de reencontro de Larissa")
    $ add_affinity_points("larissa", 8, "Carta de reencontro romântica")
    
    jump epilogo_final

# Epílogo para Huey
label epilogo_huey:
    show carta_huey at center
    narrator "A carta é de Huey."
    huey "Pintei um quadro com cor nova. Chamei de 'Sentimento que ainda não entendo'."
    huey "Acho que você é minha paleta favorita."
    huey "Se quiser… posso deixar um espaço em branco só pra você terminar."
    narrator "🖊 Com tinta e ternura, Huey."
    
    # Momento emocional com Huey
    call emotional_moment("letter_huey", None, "Carta especial de Huey") from _call_emotional_moment_epilogo_7
    
    $ add_shared_memory("epilogue_letter_huey", ["huey"], "Carta de reencontro de Huey")
    $ add_affinity_points("huey", 8, "Carta de reencontro romântica")
    
    jump epilogo_final

# Epílogo coletivo (sem romance)
label epilogo_coletivo:
    show carta_coletiva at center
    narrator "A carta é de todos os moradores, escrita coletivamente."
    narrator "Ei, desaparecido! A gente tá bem. A saudade existe, mas ela virou combustível."
    narrator "Estamos planejando um reencontro. Pode ser um café. Pode ser uma maratona de filmes. Pode ser só um silêncio confortável."
    narrator "O que importa é que você esteja lá."
    narrator "🖊 Com carinho (e gritaria), A república toda."
    
    # Momento emocional coletivo
    call emotional_moment("letter_collective", None, "Carta coletiva de reencontro") from _call_emotional_moment_epilogo_8
    
    $ add_shared_memory("epilogue_letter_collective", ["samantha", "nicole", "katia", "camille", "larissa", "huey"], "Carta coletiva de reencontro")
    $ add_affinity_points("samantha", 4, "Carta coletiva de reencontro")
    $ add_affinity_points("nicole", 4, "Carta coletiva de reencontro")
    $ add_affinity_points("katia", 4, "Carta coletiva de reencontro")
    $ add_affinity_points("camille", 4, "Carta coletiva de reencontro")
    $ add_affinity_points("larissa", 4, "Carta coletiva de reencontro")
    $ add_affinity_points("huey", 4, "Carta coletiva de reencontro")
    
    jump epilogo_final

# === EPÍLOGO MELHORADO - FINAL EMOCIONALMENTE SATISFATÓRIO ===
label epilogo_final:
    
    # === CENA FINAL COM TÉCNICAS DOS SUCESSOS ===
    scene bg sunset with dissolve
    # play music "nostalgic_theme.ogg" fadein 3.0  # Arquivo de música opcional
    
    narrator "Seis meses depois..."
    
    # Momento emocional de reencontro
    call emotional_moment("six_months_later", None, "Reencontro após seis meses") from _call_emotional_moment_epilogo_9
    
    scene bg campus_autumn with dissolve
    narrator "As folhas douradas do outono dançavam pelo campus quando nos encontramos novamente."
    narrator "Não por acaso - mas por escolha. Por amor. Por saudade."
    
    # Retrospectiva dos relacionamentos
    narrator "Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o final
    $ can_progress, progress_message = check_chapter_progression_requirement(11)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("final_achievement", None, "Realização de ter criado conexões suficientes para o final") from _call_emotional_moment_epilogo_10
        
        narrator "[progress_message]"
        narrator "A jornada havia sido mais do que uma experiência de moradia. Foi um momento de transformação, onde os laços se fortaleceram e os corações se abriram."
        
        show samantha happy at left
        samantha "Parece que nossa república realmente nos uniu de uma forma especial, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. A república havia sido mais que um lugar para morar - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump epilogo_reunion
    else:
        # Momento emocional de crescimento
        call emotional_moment("final_growth_opportunity", None, "Oportunidade de crescimento através da reflexão final") from _call_emotional_moment_epilogo_11
        
        narrator "[progress_message]"
        narrator "A jornada havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. A república foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. A república havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump epilogo_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump epilogo_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Epílogo novamente":
                jump epilogo

label epilogo_reunion:
    
    # Reunião emocional - cada personagem cresceu
    scene bg cafeteria with dissolve
    show nicole happy at left
    show camille gentle at right
    
    nicole "Consegui! O projeto de apoio aos artistas foi aprovado pela universidade!"
    camille "E meu centro de bem-estar criativo abriu semana passada. As energias estão fluindo perfeitamente."
    
    $ add_affinity_points("nicole", 5, "Sucesso no projeto de apoio aos artistas")
    $ add_affinity_points("camille", 5, "Abertura do centro de bem-estar criativo")
    
    show katia happy at center
    katia "Meu filme sobre nossa república ganhou o festival estudantil. Acho que vocês me inspiraram a fazer algo... menos sombrio."
    
    $ add_affinity_points("katia", 5, "Sucesso no festival estudantil")
    
    show samantha happy at left
    samantha "E meu canal explodiu! Quem diria que compartilhar nossas aventuras de RPG seria tão popular?"
    
    $ add_affinity_points("samantha", 5, "Sucesso no canal de RPG")
    
    show larissa happy at right
    larissa "Estou capitã do time de vôlei agora! E sabe o que é mais legal? Ensino meditação pós-treino. Aprendi com alguém especial..."
    
    $ add_affinity_points("larissa", 5, "Liderança no time de vôlei")
    
    show huey gentle at center
    huey "Minha primeira exposição individual é no próximo mês. E todas vocês estão no convite como 'musas inspiradoras'."
    
    $ add_affinity_points("huey", 5, "Primeira exposição individual")
    
    # === MOMENTO FINAL NAKIGE - REALIZAÇÃO DO CRESCIMENTO ===
    call emotional_moment("realization", None, "Consciência de como todos cresceram através do amor compartilhado") from _call_emotional_moment_epilogo_12
    
    narrator "Olhando para cada uma delas, não pude deixar de sorrir."
    narrator "Não eram mais as mesmas pessoas que conheci naquele primeiro dia na faculdade."
    narrator "Cada uma havia encontrado sua força através das outras."
    narrator "Cada uma havia se tornado mais autêntica, mais corajosa, mais plena."
    
    # Momento emocional de realização
    call emotional_moment("growth_realization", None, "Realização do crescimento coletivo") from _call_emotional_moment_epilogo_13
    
    # Revelação final baseada nos relacionamentos construídos
    $ total_growth = character_growth_samantha + character_growth_katia + character_growth_nicole + character_growth_larissa + character_growth_huey + character_growth_camille
    $ total_memories = len(shared_memories)
    $ total_emotional_moments = len(emotional_moments_unlocked)
    
    if total_growth >= 300 and total_memories >= 5:
        narrator "E eu? Eu havia aprendido que o amor verdadeiro não se limita a uma pessoa."
        narrator "Que a família que escolhemos pode ser mais forte que qualquer laço sanguíneo."
        narrator "Que crescer significa ajudar outros a crescerem também."
    else:
        narrator "E eu? Eu havia aprendido que as conexões humanas são complexas e preciosas."
        narrator "Que cada pessoa que passa por nossa vida deixa uma marca."
        narrator "Que algumas marcas se tornam cicatrizes bonitas."
    
    # === FINAL BASEADO NOS RELACIONAMENTOS CONSTRUÍDOS ===
    $ personagem_mais_proxima = max(afinidades, key=afinidades.get)
    $ relacionamento_final = globals()[f"relationship_{personagem_mais_proxima}"]
    
    if relacionamento_final == "romantic" and afinidades[personagem_mais_proxima] >= 70:
        narrator "E havia algo mais... algo especial com [personagem_mais_proxima.title()]."
        narrator "Não era apenas amizade. Era algo que cresceu devagar, naturalmente."
        narrator "Como uma planta que você rega todos os dias até que, um dia, ela floresce."
        jump final_romantico
    else:
        narrator "Mais importante que qualquer romance, havíamos construído algo eterno:"
        narrator "Uma irmandade que transcenderia tempo e distância."
        jump final_familiar
    
label final_romantico:
    scene bg sunset with dissolve
    $ personagem = personagem_mais_proxima
    if personagem == "camille":
        show camille happy at center
    elif personagem == "nicole":
        show nicole happy at center
    elif personagem == "samantha":
        show samantha happy at center
    elif personagem == "katia":
        show katia happy at center
    elif personagem == "huey":
        show huey happy at center
    elif personagem == "larissa":
        show larissa happy at center
    
    narrator "Quando todos se despediram, [personagem.title()] ficou."
    narrator "Não precisamos de palavras. O silêncio disse tudo."
    narrator "Havíamos encontrado algo raro: amor que cresceu da amizade."
    narrator "Amor que não precisou ser forçado, mas simplesmente... floresceu."
    
    # Momento emocional romântico
    call emotional_moment("romantic_final", None, "Final romântico com a personagem escolhida") from _call_emotional_moment_epilogo_14
    
    $ add_shared_memory("romantic_final", [personagem], "Final romântico com " + personagem.title())
    $ add_affinity_points(personagem, 15, "Final romântico")
    
    show screen emotional_moment_notification("💖 O amor verdadeiro às vezes chega silenciosamente, como o amanhecer...")
    pause 4.0
    hide screen emotional_moment_notification
    
    jump cena_foto_final

label final_familiar:
    scene bg casa_sala with dissolve
    show nicole happy at left
    show katia happy at center
    show samantha happy at right
    
    hide nicole
    hide katia
    hide samantha
    
    show larissa happy at left
    show huey happy at center
    show camille gentle at right
    
    narrator "Todas voltaram à casa uma última vez antes da demolição."
    narrator "Não para se despedir da casa - mas para celebrar o que ela representava."
    narrator "O lugar onde aprendemos que 'família' é uma escolha, não um acidente."
    
    # Momento emocional familiar
    call emotional_moment("family_final", None, "Final familiar com todos os personagens") from _call_emotional_moment_epilogo_15
    
    $ add_shared_memory("family_final", ["samantha", "nicole", "katia", "camille", "larissa", "huey"], "Final familiar com todos")
    $ add_affinity_points("samantha", 8, "Final familiar")
    $ add_affinity_points("nicole", 8, "Final familiar")
    $ add_affinity_points("katia", 8, "Final familiar")
    $ add_affinity_points("camille", 8, "Final familiar")
    $ add_affinity_points("larissa", 8, "Final familiar")
    $ add_affinity_points("huey", 8, "Final familiar")
    
    show screen emotional_moment_notification("🏠 Um lar não é feito de paredes, mas de corações conectados...")
    pause 4.0
    hide screen emotional_moment_notification
    
    jump cena_foto_final

label cena_foto_final:
    scene bg republica_foto with fade
    narrator "A última foto que tiramos não foi posada."
    narrator "Foi um momento espontâneo de riso, de abraços, de lágrimas felizes."
    narrator "Foi a imagem perfeita de pessoas que se amam de verdade."
    
    # Momento emocional da foto final
    call emotional_moment("final_photo", None, "Foto final da república") from _call_emotional_moment_epilogo_16
    
    show foto_republica at center with dissolve
    narrator "\"Rua Aurora, 57 - Onde descobrimos que o amor tem muitas formas, e todas são válidas.\""
    
    # === MENSAGEM FINAL INSPIRADA NOS SUCESSOS ===
    scene black with fade
    centered "{color=#FFD700}🌟{/color}"
    centered "{color=#FFFFFF}Obrigado por viver esta jornada conosco.{/color}"
    centered "{color=#FFFFFF}Que vocês também encontrem sua 'Rua Aurora' -{/color}"
    centered "{color=#FFFFFF}um lugar onde possam ser autenticamente vocês mesmos.{/color}"
    centered "{color=#FFD700}🌟{/color}"
    
    pause 2.0
    
    # Estatísticas finais (feedback do jogador)
    centered "✨ ESTATÍSTICAS DA SUA JORNADA ✨"
    centered "Memórias criadas: [total_memories]"
    centered "Momentos emocionais vividos: [total_emotional_moments]"
    centered "Nível de empatia desenvolvido: [player_empathy_level]"
    centered "Crescimento total dos personagens: [total_growth]"
    
    pause 3.0
    
    centered "{color=#FF69B4}Todas as conexões que você criou permanecerão para sempre...{/color}"
    
    return

