label capitulo9:
    if "capitulo9" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo9")
    
    scene bg republica_manha with fade
    narrator "A manhã começa como qualquer outra... até que o e-mail chega. A caixa de entrada da república explode de notificações."
    
    # Momento emocional de expectativa
    call emotional_moment("email_anticipation", None, "Expectativa pelo resultado da defesa da república") from _call_emotional_moment_cap9_1
    
    narrator "Era o momento decisivo. Tudo o que havíamos construído juntos seria testado em uma única resposta."

    show nicole neutral at left
    nicole "É... chegou. O momento que vai definir nosso futuro."
    nicole "Mas independente do resultado, já construímos algo especial aqui."
    $ add_affinity_points("nicole", 3, "Liderança na expectativa do resultado")
    hide nicole

    show camille neutral at center
    camille "Que as energias estejam em fluxo…"
    camille "Sinto que algo especial está prestes a acontecer. A energia da casa está vibrando diferente."
    $ add_affinity_points("camille", 3, "Conexão espiritual com o momento")
    hide camille

    show katia blush at right
    katia "Se for negativa, eu me mudo pra uma caverna. Ou pro porão do cinema."
    katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim! É só que... esta casa se tornou importante para mim."
    $ add_affinity_points("katia", 3, "Vulnerabilidade sobre a casa")
    hide katia

    show larissa neutral at left
    larissa "Gente, lê logo! Meu sangue tá indo todo pro cérebro!"
    larissa "Esta casa é nossa família. Vamos descobrir se podemos continuar juntos!"
    $ add_affinity_points("larissa", 3, "Energia e determinação")
    hide larissa

    narrator "Você abre o e-mail e lê em voz alta."
    '[nome]' "Após revisão do material enviado e avaliação da relevância cultural e comunitária da residência, a reitoria... autoriza a manutenção da república Rua Aurora."

    show samantha happy at center
    samantha "MISSÃO COMPLETA!"
    samantha "Nossa defesa funcionou! Somos uma família de verdade agora!"
    $ add_affinity_points("samantha", 3, "Celebração da vitória")
    hide samantha

    show huey blush at right
    huey "Vamos continuar pintando as manhãs juntos..."
    huey "Cada dia será uma nova obra de arte, criada por todos nós."
    $ add_affinity_points("huey", 3, "Visão artística do futuro")
    hide huey

    narrator "Eles se abraçam. Alguns riem. Outros choram. O lar deles, construído com convivência, está salvo."
    
    # Momento emocional de celebração
    call emotional_moment("victory_celebration", None, "Celebração da vitória da defesa da república") from _call_emotional_moment_cap9_2
    
    narrator "Era um momento de pura alegria. A república havia sido salva, e os laços que havíamos construído se fortaleceram ainda mais."

    # Todos os personagens recebem pontos de afinidade
    $ add_affinity_points("samantha", 5, "Vitória da defesa da república")
    $ add_affinity_points("nicole", 5, "Vitória da defesa da república")
    $ add_affinity_points("huey", 5, "Vitória da defesa da república")
    $ add_affinity_points("camille", 5, "Vitória da defesa da república")
    $ add_affinity_points("larissa", 5, "Vitória da defesa da república")
    $ add_affinity_points("katia", 5, "Vitória da defesa da república")

    # Gesto carinhoso se em rota romântica
    if romance_samantha:
        narrator "Samantha segura sua mão por um momento, sorrindo."
    elif romance_nicole:
        narrator "Nicole olha para você, com um sorriso tímido e prolongado."
    elif romance_huey:
        narrator "Huey toca seu ombro, com um olhar cheio de significado."
    elif romance_camille:
        narrator "Camille fecha os olhos e murmura algo sobre conexões eternas."
    elif romance_larissa:
        narrator "Larissa dá um leve soco no seu braço, rindo."
    elif romance_katia:
        narrator "Katia desvia o olhar, mas você percebe um sorriso sincero."

    jump capitulo9_praia

label capitulo9_praia:
    scene bg praia_chegada with fade
    narrator "Para comemorar, Camille sugere uma escapada. Huey organiza, Larissa aluga uma van, e no sábado, todos partem para a Praia da Lua Clara — famosa por seu pôr do sol lilás."
    
    # Momento emocional da viagem
    call emotional_moment("beach_trip_celebration", None, "Viagem de comemoração para a praia") from _call_emotional_moment_cap9_3
    
    narrator "Era um momento de celebração, onde todos podiam relaxar e desfrutar da companhia uns dos outros."

    show camille bikini at left
    camille "O mar cura. E hoje... a gente merece mergulhar."
    camille "Esta é nossa recompensa por tudo o que conquistamos juntos."
    $ add_affinity_points("camille", 3, "Sugestão da viagem à praia")
    hide camille

    show nicole bikini at center
    nicole "Horário das refeições, revezamento do guarda-sol e tempo livre organizados."
    nicole "Mas hoje, vamos focar em nos divertir. Merecemos isso."
    $ add_affinity_points("nicole", 3, "Organização da viagem")
    hide nicole

    show samantha bikini at right
    samantha "Vai ter RPG na areia, sim!"
    samantha "Vamos criar aventuras épicas na praia!"
    $ add_affinity_points("samantha", 3, "Entusiasmo pela viagem")
    hide samantha

    show katia bikini at left
    katia "Sol, suor e sentimentalismo... ótimo roteiro para um drama de verão."
    katia "N-não é como se eu estivesse animada ou qualquer coisa assim! É só que... talvez seja bom sair da rotina."
    $ add_affinity_points("katia", 3, "Aceitação da viagem")
    hide katia

    show huey bikini at center
    huey "Vou pintar vocês no mar. Sem reclamar!"
    huey "Cada momento será uma obra de arte, capturada para sempre."
    $ add_affinity_points("huey", 3, "Visão artística da viagem")
    hide huey

    show larissa bikini at right
    larissa "E vai ter campeonato! Vamo ver quem aguenta a minha cortada!"
    larissa "Vamos mostrar que somos um time invencível!"
    $ add_affinity_points("larissa", 3, "Energia esportiva da viagem")
    hide larissa

    # Todos ganham pontos de afinidade
    $ add_affinity_points("samantha", 4, "Viagem de comemoração à praia")
    $ add_affinity_points("nicole", 4, "Viagem de comemoração à praia")
    $ add_affinity_points("huey", 4, "Viagem de comemoração à praia")
    $ add_affinity_points("camille", 4, "Viagem de comemoração à praia")
    $ add_affinity_points("larissa", 4, "Viagem de comemoração à praia")
    $ add_affinity_points("katia", 4, "Viagem de comemoração à praia")
    
    $ interacoes_realizadas = []
    jump capitulo9_tarde

label capitulo9_tarde:
    narrator "A tarde na praia se desenrola com momentos especiais. Cada pessoa tem algo único para compartilhar, e você pode escolher com quem deseja passar mais tempo."
    
    # Momento emocional da tarde
    call emotional_moment("beach_afternoon_moments", None, "Momentos especiais da tarde na praia") from _call_emotional_moment_cap9_4
    
    narrator "Era um momento de conexão, onde cada interação poderia se tornar uma memória especial."
    
    if len(interacoes_realizadas) == 6:
        jump capitulo9_fogueira

    # Exibe o menu com as opções restantes
    menu:
        "Caminhada nas pedras com Camille" if "camille" not in interacoes_realizadas:
            $ interacoes_realizadas.append("camille")
            jump capitulo9_camille
        "Aula de vôlei com Larissa" if "larissa" not in interacoes_realizadas:
            $ interacoes_realizadas.append("larissa")
            jump capitulo9_larissa
        "Aquarela na areia com Huey" if "huey" not in interacoes_realizadas:
            $ interacoes_realizadas.append("huey")
            jump capitulo9_huey
        "Construção de castelo com Samantha" if "samantha" not in interacoes_realizadas:
            $ interacoes_realizadas.append("samantha")
            jump capitulo9_samantha
        "Conversa estratégica na sombra com Nicole" if "nicole" not in interacoes_realizadas:
            $ interacoes_realizadas.append("nicole")
            jump capitulo9_nicole
        "Trilha até a falésia com Katia" if "katia" not in interacoes_realizadas:
            $ interacoes_realizadas.append("katia")
            jump capitulo9_katia

label capitulo9_camille:
    show camille bikini at center
    narrator "Você e Camille caminham pelas pedras, com o vento bagunçando os cabelos dela."
    camille "Às vezes me pergunto… se algumas almas se encontram vida após vida."
    '[nome]' "Você acha que a gente já se conheceu antes?"
    camille "Talvez. Ou talvez só tenha sido bom o bastante pra parecer eterno agora."

    if romance_camille:
        $ add_shared_memory("beach_walk_camille", ["camille"], "Caminhada nas pedras com Camille")
        $ add_affinity_points("camille", 8, "Momento romântico na praia")
        narrator "Camille segura sua mão e, por um momento, o mundo parece parar. Vocês compartilham um beijo suave."
    elif points_camille >= 5:
        $ add_shared_memory("beach_walk_camille", ["camille"], "Caminhada nas pedras com Camille")
        $ add_affinity_points("camille", 6, "Conexão espiritual na praia")
        narrator "Camille sorri e abraça você, um gesto cheio de significado."
    else:
        $ add_shared_memory("beach_walk_camille", ["camille"], "Caminhada nas pedras com Camille")
        $ add_affinity_points("camille", 4, "Conversa espiritual na praia")
        narrator "Camille fala sobre conexões espirituais, deixando você inspirado."

    jump capitulo9_tarde

label capitulo9_larissa:
    show larissa bikini at center
    narrator "Você e Larissa estão na quadra improvisada na areia, com uma bola de vôlei entre vocês."
    larissa "Vamos lá! Quero ver se você consegue bloquear minha cortada!"
    '[nome]' "Eu vou tentar, mas não prometo nada."
    larissa "Sem desculpas! Aqui é treino sério!"
    
    if romance_larissa:
        $ add_shared_memory("beach_volleyball_larissa", ["larissa"], "Aula de vôlei com Larissa")
        $ add_affinity_points("larissa", 8, "Momento romântico na praia")
        narrator "Depois de uma partida intensa, Larissa sorri e se aproxima. Ela toca seu braço e, por um momento, vocês compartilham algo mais profundo."
    elif points_larissa >= 5:
        $ add_shared_memory("beach_volleyball_larissa", ["larissa"], "Aula de vôlei com Larissa")
        $ add_affinity_points("larissa", 6, "Conexão esportiva na praia")
        narrator "Larissa ri e dá um leve soco no seu ombro. 'Você tá melhorando, hein!'"
    else:
        $ add_shared_memory("beach_volleyball_larissa", ["larissa"], "Aula de vôlei com Larissa")
        $ add_affinity_points("larissa", 4, "Aprendizado esportivo na praia")
        narrator "Larissa dá algumas dicas sobre vôlei, e vocês terminam a partida com risadas e aprendizado."

    jump capitulo9_tarde

label capitulo9_huey:
    show huey bikini at center
    narrator "Você e Huey estão sentados na areia, com pincéis e aquarelas espalhados ao redor."
    huey "Eu quero capturar o movimento das ondas... mas também o que elas fazem a gente sentir."
    '[nome]' "Isso é... profundo. Você sempre pensa assim?"
    huey "A arte é sobre sentir. E você me inspira a sentir mais."

    if romance_huey:
        $ add_shared_memory("beach_painting_huey", ["huey"], "Aquarela na areia com Huey")
        $ add_affinity_points("huey", 8, "Momento romântico na praia")
        narrator "Huey sorri timidamente e mostra um retrato que ele fez de você. 'Espero que goste... é como eu vejo você.'"
    elif points_huey >= 5:
        $ add_shared_memory("beach_painting_huey", ["huey"], "Aquarela na areia com Huey")
        $ add_affinity_points("huey", 6, "Conexão artística na praia")
        narrator "Huey mostra um desenho das ondas e explica como ele tentou capturar o momento. 'Obrigado por estar aqui comigo.'"
    else:
        $ add_shared_memory("beach_painting_huey", ["huey"], "Aquarela na areia com Huey")
        $ add_affinity_points("huey", 4, "Inspiração artística na praia")
        narrator "Huey fala sobre as cores e formas, e você se sente inspirado pela paixão dele pela arte."

    jump capitulo9_tarde

label capitulo9_samantha:
    show samantha bikini at center
    narrator "Você e Samantha estão na areia, construindo um castelo com torres e muralhas."
    samantha "Se isso fosse um jogo, a gente já teria desbloqueado o troféu de 'melhor castelo'."
    '[nome]' "Com certeza. Mas acho que precisamos de uma ponte levadiça."
    samantha "Boa ideia! E talvez um dragão pra proteger o tesouro."

    if romance_samantha:
        $ add_shared_memory("beach_castle_samantha", ["samantha"], "Construção de castelo com Samantha")
        $ add_affinity_points("samantha", 8, "Momento romântico na praia")
        narrator "Samantha olha para você e sorri. 'Você é o melhor parceiro de guilda que eu poderia ter.'"
    elif points_samantha >= 5:
        $ add_shared_memory("beach_castle_samantha", ["samantha"], "Construção de castelo com Samantha")
        $ add_affinity_points("samantha", 6, "Conexão criativa na praia")
        narrator "Samantha ri e dá um high-five em você. 'A gente arrasou nesse castelo!'"
    else:
        $ add_shared_memory("beach_castle_samantha", ["samantha"], "Construção de castelo com Samantha")
        $ add_affinity_points("samantha", 4, "Inspiração criativa na praia")
        narrator "Samantha fala sobre como jogos e criatividade ajudam a construir coisas incríveis, e você se sente inspirado."

    jump capitulo9_tarde

label capitulo9_nicole:
    show nicole bikini at center
    narrator "Você e Nicole estão sentados sob um guarda-sol, com uma brisa suave passando por vocês."
    nicole "Eu não gosto muito de areia... mas gosto da sua companhia."
    '[nome]' "Então, vou considerar isso um elogio."
    nicole "Considere. Mas não se acostume."

    if romance_nicole:
        $ add_shared_memory("beach_shade_nicole", ["nicole"], "Conversa estratégica na sombra com Nicole")
        $ add_affinity_points("nicole", 8, "Momento romântico na praia")
        narrator "Nicole olha para você, corando levemente. 'Obrigada por estar aqui. Isso significa muito pra mim.'"
    elif points_nicole >= 5:
        $ add_shared_memory("beach_shade_nicole", ["nicole"], "Conversa estratégica na sombra com Nicole")
        $ add_affinity_points("nicole", 6, "Conexão intelectual na praia")
        narrator "Nicole sorri e ajusta os óculos. 'Acho que você é a única pessoa com quem eu consigo relaxar assim.'"
    else:
        $ add_shared_memory("beach_shade_nicole", ["nicole"], "Conversa estratégica na sombra com Nicole")
        $ add_affinity_points("nicole", 4, "Conversa organizacional na praia")
        narrator "Nicole fala sobre como a organização do dia foi importante, e você percebe o quanto ela se importa com os detalhes."

    jump capitulo9_tarde

label capitulo9_katia:
    show katia bikini at center
    narrator "Você e Katia estão subindo uma trilha até a falésia, com o som das ondas ao fundo."
    katia "Se isso fosse um filme, esse seria o momento em que o [nome] faz uma grande revelação."
    '[nome]' "E você? Qual seria sua grande revelação?"
    katia "Que eu odeio clichês... mas talvez goste de momentos como esse."

    if romance_katia:
        $ add_shared_memory("beach_cliff_katia", ["katia"], "Trilha até a falésia com Katia")
        $ add_affinity_points("katia", 8, "Momento romântico na praia")
        narrator "Katia para por um momento e olha para você. 'Não vou dizer que isso é especial... mas talvez seja.'"
    elif points_katia >= 5:
        $ add_shared_memory("beach_cliff_katia", ["katia"], "Trilha até a falésia com Katia")
        $ add_affinity_points("katia", 6, "Conexão emocional na praia")
        narrator "Katia sorri de lado. 'Você é menos irritante do que eu pensei. Isso é um elogio.'"
    else:
        $ add_shared_memory("beach_cliff_katia", ["katia"], "Trilha até a falésia com Katia")
        $ add_affinity_points("katia", 4, "Conversa profunda na praia")
        narrator "Katia fala sobre como momentos simples podem ser os mais significativos, e você sente que a entende melhor."

    jump capitulo9_tarde

label capitulo9_fogueira:
    scene bg fogueira_noite with fade
    narrator "À noite, o grupo monta uma fogueira. Risos, batidas na perna, violão desafinado, biscoitos queimados e segredos partilhados."
    
    # Momento emocional da fogueira
    call emotional_moment("beach_bonfire_night", None, "Noite de fogueira na praia") from _call_emotional_moment_cap9_5
    
    narrator "Era um momento mágico, onde os corações se abriam e os laços se fortaleciam sob o céu estrelado."

    show nicole bikini at left
    nicole "Acho que... isso é o mais perto de paz que já estive."
    nicole "Esta é a família que eu sempre quis ter."
    $ add_affinity_points("nicole", 3, "Momentos de paz na fogueira")
    hide nicole

    show huey bikini at center
    huey "Essas cores dançam como a gente hoje dançou o dia inteiro."
    huey "Cada chama conta uma história, cada história nos une mais."
    $ add_affinity_points("huey", 3, "Visão artística da fogueira")
    hide huey

    show katia bikini at right
    katia "Isso é conteúdo demais pra não virar roteiro."
    katia "N-não é como se eu estivesse emocionada ou qualquer coisa assim! É só que... momentos como este são especiais."
    $ add_affinity_points("katia", 3, "Vulnerabilidade na fogueira")
    hide katia

    show camille bikini at left
    camille "Promete que a gente se encontra sempre, mesmo depois?"
    camille "Que nossas almas continuem conectadas, independente do que aconteça."
    $ add_affinity_points("camille", 3, "Conexão espiritual na fogueira")
    hide camille

    show larissa bikini at center
    larissa "Eu prometo. Com sangue de atleta."
    larissa "Somos uma família agora, e famílias ficam juntas para sempre!"
    $ add_affinity_points("larissa", 3, "Determinação familiar na fogueira")
    hide larissa

    show samantha bikini at right
    samantha "Você prometeu me escolher na próxima campanha..."
    samantha "E eu prometo que sempre seremos os melhores parceiros de guilda!"
    $ add_affinity_points("samantha", 3, "Promessa de amizade na fogueira")
    hide samantha

    if romance_samantha:
        narrator "Samantha se aproxima e vocês compartilham um momento íntimo à parte."
    elif romance_nicole:
        narrator "Nicole senta ao seu lado, e vocês trocam olhares significativos."
    elif romance_huey:
        narrator "Huey mostra um desenho que fez de você, cheio de detalhes."
    elif romance_camille:
        narrator "Camille segura sua mão e murmura algo sobre eternidade."
    elif romance_larissa:
        narrator "Larissa desafia você para uma corrida até a beira do mar."
    elif romance_katia:
        narrator "Katia compartilha um segredo que ela nunca contou a ninguém."

    jump capitulo9_amanhecer

label capitulo9_amanhecer:
    scene bg praia_amanhecer with fade
    narrator "O sol começa a nascer. Todos ainda sonolentos, cobertos de areia e lembranças. Você caminha sozinho até o mar."

    # Exibe todas as interações de amizade (onde romance_<personagem> é False)
    if not romance_nicole:
        show nicole bikini at left
        narrator "Nicole se aproxima, ajustando os óculos enquanto observa o mar."
        nicole "Eu nunca fui boa em dizer essas coisas, mas... obrigada por tudo. Você me mostrou que nem tudo precisa ser tão calculado. Às vezes, só estar presente já é suficiente."
        '[nome]' "Você também me ensinou muito, Nicole. Obrigado por ser você."
        nicole "Bem... acho que isso significa que somos uma boa equipe."

    if not romance_samantha:
        show samantha bikini at center
        narrator "Samantha aparece com um sorriso radiante, segurando um cobertor enrolado nos ombros."
        samantha "Ei, parceiro de guilda! Só queria dizer que você é o melhor companheiro de aventuras que eu poderia pedir. Obrigada por sempre estar ao meu lado."
        '[nome]' "E você é a pessoa mais criativa e divertida que eu conheço. Obrigado por tornar tudo mais leve."
        samantha "Ah, para! Você vai me fazer chorar... ou talvez só rir mais alto."

    if not romance_huey:
        show huey bikini at right
        narrator "Huey se aproxima, segurando seu caderno de desenhos, com um sorriso sereno."
        huey "Eu queria te mostrar isso... é um desenho que fiz de todos nós. Você está bem no centro, porque foi você que manteve tudo unido."
        '[nome]' "Huey, isso é incrível. Obrigado por capturar algo tão especial."
        huey "Obrigado por ser minha inspiração. Você é uma pessoa única."

    if not romance_camille:
        show camille bikini at left
        narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
        camille "Você sente isso? A energia... ela está em paz. E acho que é porque você esteve aqui para equilibrar tudo."
        '[nome]' "Você sempre me fez ver o mundo de uma forma diferente, Camille. Obrigado por isso."
        camille "E você me fez acreditar que algumas conexões são eternas, mesmo sem palavras."

    if not romance_larissa:
        show larissa bikini at center
        narrator "Larissa aparece com sua energia contagiante, segurando uma bola de vôlei."
        larissa "Ei, só queria dizer que você é incrível. Não sei como você conseguiu acompanhar meu ritmo, mas você fez isso parecer fácil."
        '[nome]' "Você me ensinou a nunca desistir, Larissa. Obrigado por isso."
        larissa "Ah, para com isso! Mas... obrigada por estar aqui. Você é um amigo incrível."

    if not romance_katia:
        show katia bikini at right
        narrator "Katia se aproxima, com o celular na mão e um sorriso discreto."
        katia "Se você contar pra alguém que eu disse isso, eu nego até o fim, mas... você é uma das pessoas mais importantes que já conheci. Obrigada por tudo."
        '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
        katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."

    # Exibe a interação romântica com a personagem escolhida
    if romance_nicole:
        jump capitulo9_final_nicole
    elif romance_samantha:
        jump capitulo9_final_samantha
    elif romance_huey:
        jump capitulo9_final_huey
    elif romance_camille:
        jump capitulo9_final_camille
    elif romance_larissa:
        jump capitulo9_final_larissa
    elif romance_katia:
        jump capitulo9_final_katia

    jump capitulo9_final

label capitulo9_final_nicole:
    show nicole bikini at center
    narrator "Nicole se aproxima em silêncio, com o som das ondas preenchendo o espaço entre vocês."
    nicole "Acordei com barulho de passos... e achei que fosse um ladrão de dados. Mas era só você."
    '[nome]' "Não consegui dormir. Minha mente está cheia... mas você me acalma."
    nicole "Você sempre sabe o que dizer. É estranho... mas acho que nunca me senti tão segura com alguém."
    menu:
        "Confessar que quer estar com ela":
            $ romance_nicole = True
            $ add_shared_memory("beach_sunrise_nicole", ["nicole"], "Amanhecer na praia com Nicole")
            $ add_affinity_points("nicole", 10, "Confissão de amor no amanhecer")
            "[nome]" "Nicole, eu quero estar com você. Não só agora, mas sempre."
            nicole "Sempre? Isso é... mais do que eu esperava. Mas acho que eu também quero isso."
            narrator "Nicole se aproxima e, com um sorriso tímido, vocês compartilham um beijo sob o céu estrelado."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_nicole", ["nicole"], "Amanhecer na praia com Nicole")
            $ add_affinity_points("nicole", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você é meu ponto de equilíbrio."
            nicole "Isso é... bom de ouvir. Obrigada por ser você."
            narrator "Nicole segura sua mão por um momento, e vocês ficam em silêncio, apreciando a companhia um do outro."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_nicole", ["nicole"], "Amanhecer na praia com Nicole")
            $ add_affinity_points("nicole", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o olhar de Nicole diz tudo. A conexão entre vocês se aprofunda sem a necessidade de palavras."
            jump capitulo9_final

label capitulo9_final_samantha:
    show samantha bikini at center
    narrator "Samantha se aproxima, segurando um cobertor e olhando para o mar com um sorriso suave."
    samantha "Você... não conseguiu dormir também?"
    '[nome]' "Não. Mas acho que é porque eu queria estar aqui com você."
    samantha "Você é tão bobo... mas eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_samantha = True
            $ add_shared_memory("beach_sunrise_samantha", ["samantha"], "Amanhecer na praia com Samantha")
            $ add_affinity_points("samantha", 10, "Confissão de amor no amanhecer")
            "[nome]" "Samantha, eu quero estar com você. Você faz tudo parecer mais divertido, mais leve."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. E eu aceito. Obrigada por me escolher."
            narrator "Samantha se aproxima e, com um sorriso radiante, vocês compartilham um beijo cheio de alegria e carinho."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_samantha", ["samantha"], "Amanhecer na praia com Samantha")
            $ add_affinity_points("samantha", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você faz tudo parecer mais especial."
            samantha "Você é o melhor parceiro de guilda que eu poderia ter. Obrigada por isso."
            narrator "Samantha se aconchega ao seu lado, e vocês compartilham um momento tranquilo sob o céu estrelado."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_samantha", ["samantha"], "Amanhecer na praia com Samantha")
            $ add_affinity_points("samantha", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o sorriso de Samantha diz tudo. A conexão entre vocês é inegável."
            jump capitulo9_final

label capitulo9_final_huey:
    show huey bikini at center
    narrator "Huey se aproxima, segurando um pequeno caderno de desenhos, com um sorriso tímido."
    huey "Eu ainda não terminei... mas acho que esse traço aqui é você."
    '[nome]' "Você ficou acordado desenhando? Isso é lindo, Huey."
    huey "A arte é como eu expresso o que sinto. E você... você é minha maior inspiração."
    menu:
        "Confessar que quer estar com ele":
            $ romance_huey = True
            $ add_shared_memory("beach_sunrise_huey", ["huey"], "Amanhecer na praia com Huey")
            $ add_affinity_points("huey", 10, "Confissão de amor no amanhecer")
            "[nome]" "Huey, eu quero estar com você. Você vê o mundo de um jeito que me faz querer ser parte dele."
            huey "Eu... nunca pensei que alguém pudesse dizer isso pra mim. Obrigado por me ver de verdade."
            narrator "Huey se aproxima, e vocês compartilham um beijo suave, cheio de significado e emoção."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_huey", ["huey"], "Amanhecer na praia com Huey")
            $ add_affinity_points("huey", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você me inspira."
            huey "Isso significa muito pra mim. Obrigado por estar aqui."
            narrator "Huey segura sua mão, e vocês compartilham um momento tranquilo, cercados pelo som das ondas."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_huey", ["huey"], "Amanhecer na praia com Huey")
            $ add_affinity_points("huey", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o olhar de Huey transmite tudo o que ele sente. A conexão entre vocês é profunda e sincera."
            jump capitulo9_final

label capitulo9_final_camille:
    show camille bikini at center
    narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
    camille "Você sente isso? A energia... ela está mudando."
    '[nome]' "Sim. Parece que tudo está em equilíbrio agora. Como se fosse o lugar certo para estarmos juntos."
    camille "Talvez seja porque estamos aqui. Juntos. E isso é tudo o que importa."
    menu:
        "Confessar que quer estar com ela":
            $ romance_camille = True
            $ add_shared_memory("beach_sunrise_camille", ["camille"], "Amanhecer na praia com Camille")
            $ add_affinity_points("camille", 10, "Confissão de amor no amanhecer")
            "[nome]" "Camille, eu quero estar com você. Você me faz acreditar em coisas que eu nunca pensei serem possíveis."
            camille "Você é uma alma especial. Obrigada por me encontrar, vida após vida."
            narrator "Camille segura sua mão e, com um sorriso suave, vocês compartilham um beijo cheio de significado e conexão."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_camille", ["camille"], "Amanhecer na praia com Camille")
            $ add_affinity_points("camille", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você traz paz ao meu coração."
            camille "E você traz luz ao meu mundo. Obrigada por isso."
            narrator "Camille se aproxima e segura sua mão, e vocês compartilham um momento de pura serenidade."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_camille", ["camille"], "Amanhecer na praia com Camille")
            $ add_affinity_points("camille", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o toque de Camille transmite tudo o que as palavras não conseguem expressar."
            jump capitulo9_final

label capitulo9_final_larissa:
    show larissa bikini at center
    narrator "Larissa se aproxima, segurando uma garrafa d’água e sorrindo com entusiasmo."
    larissa "Acha que amanhã a gente pode correr juntos? Ou você vai me deixar na poeira?"
    '[nome]' "Eu acho que vou tentar acompanhar você. Mas, na verdade, só quero estar ao seu lado."
    larissa "Você é tão bobo... mas eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_larissa = True
            $ add_shared_memory("beach_sunrise_larissa", ["larissa"], "Amanhecer na praia com Larissa")
            $ add_affinity_points("larissa", 10, "Confissão de amor no amanhecer")
            "[nome]" "Larissa, eu quero estar com você. Você me faz querer ser melhor, todos os dias."
            larissa  "Sério?! Uau. Isso é... incrível. Eu também quero isso."
            narrator "Larissa se aproxima e, com um sorriso radiante, vocês compartilham um beijo cheio de energia e paixão."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_larissa", ["larissa"], "Amanhecer na praia com Larissa")
            $ add_affinity_points("larissa", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você ilumina tudo ao seu redor."
            larissa "Você é incrível. Obrigada por estar aqui comigo."
            narrator "Larissa segura sua mão, e vocês compartilham um momento de pura alegria e conexão."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_larissa", ["larissa"], "Amanhecer na praia com Larissa")
            $ add_affinity_points("larissa", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o sorriso de Larissa diz tudo. A conexão entre vocês é cheia de vida e significado."
            jump capitulo9_final

label capitulo9_final_katia:
    show katia bikini at center
    narrator "Katia se aproxima, segurando o celular e olhando para o mar com um sorriso discreto."
    katia "Se você comentar que eu tô aqui, eu juro que te ignoro o resto da vida."
    '[nome]' "Eu não vou comentar. Só estou feliz que você está aqui comigo."
    katia "Você é tão irritante... mas acho que eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_katia = True
            $ add_shared_memory("beach_sunrise_katia", ["katia"], "Amanhecer na praia com Katia")
            $ add_affinity_points("katia", 10, "Confissão de amor no amanhecer")
            "[nome]" "Katia, eu quero estar com você. Você me faz ver o mundo de um jeito que ninguém mais consegue."
            katia  "Hmpf. Não se ache. Mas... obrigada por dizer isso. Eu também quero estar com você."
            narrator "Katia se aproxima e, com um sorriso tímido, vocês compartilham um beijo cheio de emoção e sinceridade."
            jump capitulo9_final
        "Dizer que está em paz só com a presença":
            $ add_shared_memory("beach_sunrise_katia", ["katia"], "Amanhecer na praia com Katia")
            $ add_affinity_points("katia", 6, "Conexão profunda no amanhecer")
            "[nome]" "Só estar aqui com você já é suficiente. Você é única."
            katia "Tá. Mas não me faça esperar muito. Obrigada por isso."
            narrator "Katia olha para você com um sorriso sincero, e vocês compartilham um momento tranquilo e significativo."
            jump capitulo9_final
        "Permanecer em silêncio":
            $ add_shared_memory("beach_sunrise_katia", ["katia"], "Amanhecer na praia com Katia")
            $ add_affinity_points("katia", 3, "Momento silencioso no amanhecer")
            narrator "Vocês ficam em silêncio, mas o olhar de Katia transmite tudo o que ela sente. A conexão entre vocês é profunda e verdadeira."
            jump capitulo9_final

label capitulo9_final_amizade:
    scene bg praia_amanhecer with fade
    narrator "Com o sol nascendo no horizonte, você se encontra cercado pelas pessoas que fizeram parte dessa jornada. Mesmo sem um romance, os laços de amizade construídos ao longo do tempo são inegáveis."

    # Nicole
    if not romance_nicole:
        show nicole bikini at left
        narrator "Nicole se aproxima, ajustando os óculos enquanto observa o mar."
        nicole "Eu nunca fui boa em dizer essas coisas, mas... obrigada por tudo. Você me mostrou que nem tudo precisa ser tão calculado. Às vezes, só estar presente já é suficiente."
        '[nome]' "Você também me ensinou muito, Nicole. Obrigado por ser você."
        nicole "Bem... acho que isso significa que somos uma boa equipe."

    # Samantha
    if not romance_samantha:
        show samantha bikini at center
        narrator "Samantha aparece com um sorriso radiante, segurando um cobertor enrolado nos ombros."
        samantha "Ei, parceiro de guilda! Só queria dizer que você é o melhor companheiro de aventuras que eu poderia pedir. Obrigada por sempre estar ao meu lado."
        '[nome]' "E você é a pessoa mais criativa e divertida que eu conheço. Obrigado por tornar tudo mais leve."
        samantha "Ah, para! Você vai me fazer chorar... ou talvez só rir mais alto."

    # Huey
    if not romance_huey:
        show huey bikini at right
        narrator "Huey se aproxima, segurando seu caderno de desenhos, com um sorriso sereno."
        huey "Eu queria te mostrar isso... é um desenho que fiz de todos nós. Você está bem no centro, porque foi você que manteve tudo unido."
        '[nome]' "Huey, isso é incrível. Obrigado por capturar algo tão especial."
        huey "Obrigado por ser minha inspiração. Você é uma pessoa única."

    # Camille
    if not romance_camille:
        show camille bikini at left
        narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
        camille "Você sente isso? A energia... ela está em paz. E acho que é porque você esteve aqui para equilibrar tudo."
        '[nome]' "Você sempre me fez ver o mundo de uma forma diferente, Camille. Obrigado por isso."
        camille "E você me fez acreditar que algumas conexões são eternas, mesmo sem palavras."

    # Larissa
    if not romance_larissa:
        show larissa bikini at center
        narrator "Larissa aparece com sua energia contagiante, segurando uma bola de vôlei."
        larissa "Ei, só queria dizer que você é incrível. Não sei como você conseguiu acompanhar meu ritmo, mas você fez isso parecer fácil."
        '[nome]' "Você me ensinou a nunca desistir, Larissa. Obrigado por isso."
        larissa "Ah, para com isso! Mas... obrigada por estar aqui. Você é um amigo incrível."

    # Katia
    if not romance_katia:
        show katia bikini at right
        narrator "Katia se aproxima, com o celular na mão e um sorriso discreto."
        katia "Se você contar pra alguém que eu disse isso, eu nego até o fim, mas... você é uma das pessoas mais importantes que já conheci. Obrigada por tudo."
        '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
        katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."

    narrator "Enquanto o sol sobe no céu, você percebe que, independentemente de romances ou destinos, os laços que você construiu com essas pessoas são inquebráveis. E isso é o que realmente importa."

label capitulo9_final:
    scene bg praia_amanhecer with fade
    narrator "O sol nasce sobre a praia, iluminando um novo dia. Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."
    
    # Momento emocional de reflexão
    call emotional_moment("beach_sunrise_reflection", None, "Reflexão sobre a viagem à praia") from _call_emotional_moment_cap9_6
    
    narrator "Era um momento de reflexão profunda, onde os corações se abriam e os laços se fortaleciam sob o céu dourado."

    # Retrospectiva dos relacionamentos
    narrator "Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(9)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap9_7
        
        narrator "[progress_message]"
        narrator "A viagem à praia havia sido mais do que uma comemoração. Foi um momento de conexão, onde os laços se fortaleceram e os corações se abriram."
        
        show samantha bikini at left
        samantha "Parece que nossa viagem realmente nos uniu ainda mais, né?"
        hide samantha
        
        show nicole bikini at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. A viagem havia sido mais que uma comemoração - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump capitulo10
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap9_8
        
        narrator "[progress_message]"
        narrator "A viagem havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia bikini at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille bikini at right
        camille "Cada conexão tem seu próprio ritmo. A viagem foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. A viagem havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo9_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo9_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 9 novamente":
                jump capitulo9