label capitulo7:
    if "capitulo7" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo7")
    
    scene bg republica_manha with fade
    narrator "Uma semana após o Festival das Estações, a rotina volta... mas algo mudou na república. Os olhares são mais longos, os silêncios mais densos, e as conversas carregam intenções novas."
    
    # Momento emocional de mudança
    call emotional_moment("post_festival_change", None, "Mudanças após o Festival das Estações que transformam os relacionamentos") from _call_emotional_moment_cap7_1
    
    narrator "Havia algo diferente no ar. O Festival das Estações havia plantado sementes de mudança que agora começavam a florescer."

    show camille gentle at left
    camille "Os ciclos se movem... E agora, algo está girando diferente."
    camille "Sinto que estamos todos conectados de uma forma que nunca estivemos antes."
    $ add_affinity_points("camille", 3, "Conexão espiritual pós-festival")
    hide camille

    show nicole neutral at center
    nicole "É só consequência. Tudo que começa a importar, exige mais da gente."
    nicole "Mas talvez seja isso que torna tudo mais especial."
    $ add_affinity_points("nicole", 3, "Reflexão sobre mudanças")
    hide nicole

    show samantha sad at right
    samantha "...Alguém sonhou com o grupo sendo separado também, ou só eu?"
    samantha "É como se eu tivesse medo de perder tudo que construímos juntos."
    $ add_affinity_points("samantha", 3, "Vulnerabilidade sobre o futuro")
    hide samantha

    narrator "Você reflete sobre seu relacionamento com as garotas. Se já iniciou uma rota romântica, a relação começa a se manifestar publicamente. Se não, pequenos gestos revelam uma tensão crescente."

    jump cena2_desafios_convivencia

label cena2_desafios_convivencia:
    scene bg sala_reuniao with dissolve
    narrator "A direção da faculdade anuncia que uma repórter virá visitar a república para fazer uma matéria especial. O grupo precisa organizar a casa, montar um projeto coletivo e escolher quem vai dar entrevista."
    
    # Momento emocional de desafio
    call emotional_moment("media_challenge", None, "Desafio da mídia que testa a união do grupo") from _call_emotional_moment_cap7_2
    
    narrator "Era um momento que testaria a força dos laços que havíamos construído. Como nos apresentaríamos ao mundo?"

    show nicole neutral at left
    nicole "Óbvio que alguém articulado precisa representar. Isso define nossa imagem."
    nicole "Mas também precisamos mostrar quem realmente somos."
    $ add_affinity_points("nicole", 3, "Responsabilidade pela imagem do grupo")
    hide nicole

    show katia neutral at center
    katia "Imagem ou autenticidade? Eu voto por não fingir."
    katia "N-não é como se eu me importasse com o que pensam ou qualquer coisa assim! É só que... prefiro ser real."
    $ add_affinity_points("katia", 3, "Defesa da autenticidade")
    hide katia

    show camille gentle at right
    camille "Talvez devêssemos nos alinhar energeticamente antes. A repórter vai sentir o clima."
    camille "A energia que emanamos é mais importante que as palavras que dizemos."
    $ add_affinity_points("camille", 3, "Conexão espiritual com o desafio")
    hide camille

    narrator "Após uma breve discussão, o grupo decide que a pessoa mais adequada para representar a república será escolhida com base em quem tem mais afinidade com o grupo."

    # Verifica quem tem mais afinidade
    if points_nicole >= max(points_katia, points_samantha, points_camille, points_huey, points_larissa):
        "[nome]" "Nicole tem razão. Precisamos de alguém articulado."
        nicole "Obrigada. Vou garantir que nossa imagem seja impecável."
        $ add_shared_memory("media_representation_nicole", ["nicole"], "Nicole escolhida para representar o grupo na mídia")
        $ add_affinity_points("nicole", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    elif points_katia >= max(points_nicole, points_samantha, points_camille, points_huey, points_larissa):
        "[nome]" "Katia está certa. Precisamos ser autênticos."
        katia "Finalmente alguém que entende. Vamos mostrar quem realmente somos."
        $ add_shared_memory("media_representation_katia", ["katia"], "Katia escolhida para representar o grupo na mídia")
        $ add_affinity_points("katia", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    elif points_samantha >= max(points_nicole, points_katia, points_camille, points_huey, points_larissa):
        "[nome]" "Samantha pode representar bem o grupo."
        samantha "Eu? Tá bom, vou tentar não estragar tudo."
        $ add_shared_memory("media_representation_samantha", ["samantha"], "Samantha escolhida para representar o grupo na mídia")
        $ add_affinity_points("samantha", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    elif points_camille >= max(points_nicole, points_katia, points_samantha, points_huey, points_larissa):
        "[nome]" "Camille pode trazer uma energia única para a entrevista."
        camille "Vou fazer o meu melhor para representar todos nós."
        $ add_shared_memory("media_representation_camille", ["camille"], "Camille escolhida para representar o grupo na mídia")
        $ add_affinity_points("camille", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    elif points_huey >= max(points_nicole, points_katia, points_samantha, points_camille, points_larissa):
        "[nome]" "Huey pode trazer uma perspectiva artística e sensível para a entrevista."
        huey "Obrigado. Vou tentar capturar a essência do que somos."
        $ add_shared_memory("media_representation_huey", ["huey"], "Huey escolhida para representar o grupo na mídia")
        $ add_affinity_points("huey", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    elif points_larissa >= max(points_nicole, points_katia, points_samantha, points_camille, points_huey):
        "[nome]" "Larissa pode trazer uma energia vibrante e dinâmica para a entrevista."
        larissa "Sério? Beleza, vou dar o meu melhor!"
        $ add_shared_memory("media_representation_larissa", ["larissa"], "Larissa escolhida para representar o grupo na mídia")
        $ add_affinity_points("larissa", 8, "Representação do grupo na mídia")
        jump cena3_duvidas_crescem
    else:
        "[nome]" "Eu posso fazer isso. Quero representar todos nós."
        narrator "O grupo concorda, e você se prepara para a entrevista."
        $ add_shared_memory("media_representation_protagonist", [], "Protagonista escolhido para representar o grupo na mídia")
        jump cena3_duvidas_crescem

label cena3_duvidas_crescem:
    narrator "À noite, a personagem com quem você iniciou uma relação amorosa te chama para uma conversa mais séria."
    
    # Momento emocional de dúvidas
    call emotional_moment("growing_doubts", None, "Dúvidas crescentes sobre o futuro dos relacionamentos") from _call_emotional_moment_cap7_3
    
    narrator "Era um momento de vulnerabilidade, onde os corações se abriam e as dúvidas se revelavam."

    if romance_camille:
        jump cena3_camille
    elif romance_samantha:
        jump cena3_samantha
    elif romance_nicole:
        jump cena3_nicole
    elif romance_katia:
        jump cena3_katia
    elif romance_huey:
        jump cena3_huey
    elif romance_larissa:
        jump cena3_larissa
    else:
        jump cena4_convite_externo

label cena3_camille:
    show camille gentle at center
    narrator "Camille te chama para uma conversa na sala de meditação."
    camille "É estranho. Quando estou com você, sinto que o tempo para. E isso... me dá medo."
    menu:
        "Sinto o mesmo. Mas vale a pena.":
            $ add_shared_memory("doubts_conversation_camille", ["camille"], "Conversa sobre dúvidas com Camille")
            $ add_affinity_points("camille", 6, "Conexão emocional profunda")
            "[nome]" "Eu sinto o mesmo. Mas acho que vale a pena."
            camille "Obrigada. Você me faz acreditar que o universo nos uniu por um motivo."
            jump cena4_convite_externo
        "Ainda estou entendendo.":
            $ add_shared_memory("doubts_conversation_camille", ["camille"], "Conversa sobre dúvidas com Camille")
            $ add_affinity_points("camille", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            camille "Eu entendo. O tempo nos guiará."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_camille", ["camille"], "Conversa sobre dúvidas com Camille")
            $ add_affinity_points("camille", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            camille "Entendi. Talvez o universo tenha outros planos."
            jump cena4_convite_externo

label cena3_samantha:
    show samantha sad at center
    narrator "Samantha te chama para uma conversa no sofá da sala, segurando um controle de videogame."
    samantha "Eu fico pensando... se a gente fosse personagens, você teria escolhido minha rota?"
    menu:
        "Claro, você é especial para mim.":
            $ add_shared_memory("doubts_conversation_samantha", ["samantha"], "Conversa sobre dúvidas com Samantha")
            $ add_affinity_points("samantha", 6, "Conexão emocional profunda")
            "[nome]" "Claro. Você é especial para mim."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ add_shared_memory("doubts_conversation_samantha", ["samantha"], "Conversa sobre dúvidas com Samantha")
            $ add_affinity_points("samantha", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            samantha "Tudo bem. Eu posso esperar. Só não demore muito, tá?"
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_samantha", ["samantha"], "Conversa sobre dúvidas com Samantha")
            $ add_affinity_points("samantha", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            samantha "Ah... entendi. Tá tudo bem. Boa noite."
            jump cena4_convite_externo

label cena3_nicole:
    show nicole neutral at center
    narrator "Nicole te chama para uma conversa na cozinha, enquanto organiza uma planilha no tablet."
    nicole "Eu não sou boa com essas coisas... mas acho que preciso de uma resposta. O que você quer de nós?"
    menu:
        "Quero estar ao seu lado.":
            $ add_shared_memory("doubts_conversation_nicole", ["nicole"], "Conversa sobre dúvidas com Nicole")
            $ add_affinity_points("nicole", 6, "Conexão emocional profunda")
            "[nome]" "Quero estar ao seu lado."
            nicole "Então tá. Vamos documentar isso com exclusividade."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer cálculo."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ add_shared_memory("doubts_conversation_nicole", ["nicole"], "Conversa sobre dúvidas com Nicole")
            $ add_affinity_points("nicole", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            nicole "Tempo é um recurso não-renovável... mas se for você, eu invisto."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_nicole", ["nicole"], "Conversa sobre dúvidas com Nicole")
            $ add_affinity_points("nicole", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            nicole "Entendido. Silêncio também é uma resposta."
            narrator "Nicole ajustou os óculos e voltou ao trabalho, sem dizer mais nada."
            jump cena4_convite_externo

label cena3_katia:
    show katia neutral at center
    narrator "Katia te chama para uma conversa no corredor, encostada na parede com os braços cruzados."
    katia "Você tem esse talento estranho de... me deixar menos cínica. Não sei se gosto disso."
    menu:
        "Talvez porque eu me importo com você.":
            $ add_shared_memory("doubts_conversation_katia", ["katia"], "Conversa sobre dúvidas com Katia")
            $ add_affinity_points("katia", 6, "Conexão emocional profunda")
            "[nome]" "Talvez porque eu me importo com você."
            katia "Você é mais idiota do que eu pensava... mas obrigada por isso."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ add_shared_memory("doubts_conversation_katia", ["katia"], "Conversa sobre dúvidas com Katia")
            $ add_affinity_points("katia", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            katia "Tá, mas não me faça esperar muito. Não sou boa com paciência."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_katia", ["katia"], "Conversa sobre dúvidas com Katia")
            $ add_affinity_points("katia", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            katia "Ah, claro. Esquece que eu disse qualquer coisa."
            narrator "Katia saiu, tentando esconder sua frustração."
            jump cena4_convite_externo

label cena3_huey:
    show huey gentle at center
    narrator "Huey te chama para uma conversa no jardim, segurando um pequeno caderno de desenhos."
    huey "Eu fico pensando... se eu te mostro tanto de mim, será que você vê o que eu vejo?"
    menu:
        "Eu vejo você, e é lindo.":
            $ add_shared_memory("doubts_conversation_huey", ["huey"], "Conversa sobre dúvidas com Huey")
            $ add_affinity_points("huey", 6, "Conexão emocional profunda")
            "[nome]" "Eu vejo você, e é lindo."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ add_shared_memory("doubts_conversation_huey", ["huey"], "Conversa sobre dúvidas com Huey")
            $ add_affinity_points("huey", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            huey "Tudo bem. Eu espero. E continuo pintando."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_huey", ["huey"], "Conversa sobre dúvidas com Huey")
            $ add_affinity_points("huey", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            huey "Ah... entendi. Às vezes o silêncio também é arte."
            narrator "Huey fechou o caderno e se afastou em silêncio."
            jump cena4_convite_externo

label cena3_larissa:
    show larissa happy at center
    narrator "Larissa te chama para uma conversa na sala de treino, segurando uma garrafa d’água."
    larissa "Eu não sou boa com palavras, mas... acho que você me faz querer tentar."
    menu:
        "Eu sinto o mesmo por você.":
            $ add_shared_memory("doubts_conversation_larissa", ["larissa"], "Conversa sobre dúvidas com Larissa")
            $ add_affinity_points("larissa", 6, "Conexão emocional profunda")
            "[nome]" "Eu sinto o mesmo por você."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ add_shared_memory("doubts_conversation_larissa", ["larissa"], "Conversa sobre dúvidas com Larissa")
            $ add_affinity_points("larissa", 4, "Honestidade sobre sentimentos")
            "[nome]" "Ainda estou tentando entender tudo isso."
            larissa "Tranquilo. A gente fortalece a amizade nos alongamentos."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ add_shared_memory("doubts_conversation_larissa", ["larissa"], "Conversa sobre dúvidas com Larissa")
            $ add_affinity_points("larissa", 2, "Resposta neutra")
            "[nome]" "Não sei se é o certo agora."
            larissa "Beleza. Valeu aí."
            narrator "Larissa deu uma risada forçada e voltou ao treino."
            jump cena4_convite_externo

label cena4_convite_externo:
    narrator "Um ex da [personagem_evento] aparece na universidade. Ele está participando de um evento na cidade e convida todos… especialmente ela."
    
    # Momento emocional de teste
    call emotional_moment("external_challenge", None, "Desafio externo que testa os relacionamentos") from _call_emotional_moment_cap7_4
    
    narrator "Era um momento que testaria a força dos laços que havíamos construído. Como reagiríamos quando o passado batesse à porta?"

    if personagem_evento == "camille":
        jump convite_camille
    elif personagem_evento == "samantha":
        jump convite_samantha
    elif personagem_evento == "nicole":
        jump convite_nicole
    elif personagem_evento == "katia":
        jump convite_katia
    elif personagem_evento == "huey":
        jump convite_huey
    elif personagem_evento == "larissa":
        jump convite_larissa

label convite_camille:
    show camille gentle at center
    narrator "Camille parece hesitante ao receber o convite."
    camille "O universo testa a frequência quando ela está mais instável."
    narrator "Ela decide ir ao evento, onde seu ex está apresentando uma palestra sobre espiritualidade e conexões humanas. Você decide acompanhá-la para apoiá-la."

    scene bg evento_camille with fade
    narrator "No evento, Camille ouve atentamente enquanto seu ex fala sobre como as energias das pessoas se conectam e se separam ao longo do tempo. Após a palestra, ele se aproxima dela."
    show ex_camille neutral at center
    ex_camille "Camille, é bom te ver. Espero que você ainda acredite que nossas almas estavam destinadas a se encontrar."
    show camille gentle at center
    camille "Talvez estivessem. Mas algumas conexões são feitas para ensinar, não para durar."
    narrator "Camille olha para você, seus olhos brilhando com uma nova certeza."
    camille "[nome], você me mostrou que algumas conexões são mais profundas porque são reais, não porque são idealizadas."
    menu:
        "Segurar a mão dela":
            $ romance_camille = True
            $ add_shared_memory("external_challenge_camille", ["camille"], "Desafio externo com Camille")
            $ add_affinity_points("camille", 10, "Superação do desafio externo")
            "[nome]" "E eu quero que a nossa conexão continue crescendo."
            camille "Obrigada. Você é a energia que eu quero ao meu lado."
            narrator "Camille sorri suavemente, e o momento entre vocês parece eterno."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            $ add_shared_memory("external_challenge_camille", ["camille"], "Desafio externo com Camille")
            $ add_affinity_points("camille", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Camille entende o que você sente, mesmo sem palavras. Ela segura sua mão por um momento antes de voltar ao evento."
            jump cena5_domingo_para_dois

label convite_samantha:
    show samantha sad at center
    narrator "Samantha parece surpresa ao receber o convite, mas tenta disfarçar."
    samantha "Ah, claro... ele sempre aparece nos momentos mais aleatórios."
    narrator "No evento, seu ex está organizando um campeonato de videogame. Samantha decide participar, e você a acompanha para torcer por ela."

    scene bg evento_samantha with fade
    narrator "Samantha joga com intensidade, derrotando vários oponentes até chegar à final. Seu ex, que também está competindo, a enfrenta na última partida."
    show ex_samantha smug at center
    ex_samantha "Você sempre foi boa, Sam. Mas será que consegue me vencer agora?"
    show samantha determined at center
    samantha "Eu não preciso provar nada para você. Mas vou ganhar, só para deixar claro."
    narrator "Samantha vence a partida com uma jogada brilhante. Após o jogo, ela se aproxima de você, ainda segurando o controle."
    samantha "[nome], você é a única pessoa que me faz sentir que sou mais do que uma jogadora. Com você, eu sou eu mesma."
    menu:
        "Abraçá-la":
            $ romance_samantha = True
            $ add_shared_memory("external_challenge_samantha", ["samantha"], "Desafio externo com Samantha")
            $ add_affinity_points("samantha", 10, "Superação do desafio externo")
            "[nome]" "E você é a pessoa que eu quero ao meu lado, em qualquer jogo."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada por me escolher."
            narrator "Samantha sorri, e vocês compartilham um momento de pura conexão."
            jump cena5_domingo_para_dois
        "Dar um sorriso de apoio":
            $ add_shared_memory("external_challenge_samantha", ["samantha"], "Desafio externo com Samantha")
            $ add_affinity_points("samantha", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Samantha entende o que você sente e sorri de volta, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label convite_nicole:
    show nicole neutral at center
    narrator "Nicole ajusta os óculos ao receber o convite, tentando esconder qualquer reação."
    nicole "Isso é... inesperado. Mas não impossível de gerenciar."
    narrator "No evento, seu ex está apresentando um projeto de tecnologia inovadora. Nicole decide ir para avaliar o trabalho, e você a acompanha."

    scene bg evento_nicole with fade
    narrator "Nicole observa atentamente enquanto seu ex apresenta gráficos e estatísticas. Após a apresentação, ele se aproxima dela."
    show ex_nicole confident at center
    ex_nicole "Nicole, você sempre foi a mente mais brilhante que conheci. Espero que ainda pense em mim quando vê algo bem organizado."
    show nicole neutral at center
    nicole "Eu penso em eficiência, não em nostalgia. E, sinceramente, já encontrei alguém que entende isso melhor do que você."
    narrator "Nicole olha para você, ajustando os óculos com um leve sorriso."
    nicole "[nome], você é a única variável que faz minha equação funcionar."
    menu:
        "Segurar sua mão":
            $ romance_nicole = True
            $ add_shared_memory("external_challenge_nicole", ["nicole"], "Desafio externo com Nicole")
            $ add_affinity_points("nicole", 10, "Superação do desafio externo")
            "[nome]" "E eu quero continuar sendo parte da sua equação."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorri levemente, e o momento parece mais importante do que qualquer cálculo."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            $ add_shared_memory("external_challenge_nicole", ["nicole"], "Desafio externo com Nicole")
            $ add_affinity_points("nicole", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Nicole entende o que você sente, mas volta a focar no evento, como se algo tivesse ficado por dizer."
            jump cena5_domingo_para_dois

label convite_katia:
    show katia neutral at center
    narrator "Katia revira os olhos ao receber o convite, mas há algo em seu tom que sugere hesitação."
    katia "Claro que ele aparece agora. É tão típico."
    narrator "No evento, seu ex está exibindo um curta-metragem que dirigiu. Katia decide ir para criticar, e você a acompanha."

    scene bg evento_katia with fade
    narrator "Katia assiste ao curta com atenção, mas seu olhar crítico é evidente. Após a exibição, seu ex se aproxima dela."
    show ex_katia smug at center
    ex_katia "Então, o que achou? Ainda acha que eu não sei contar histórias?"
    show katia neutral at center
    katia "Você melhorou. Mas ainda falta algo... talvez autenticidade."
    narrator "Katia olha para você, seus olhos suavizando por um momento."
    katia "[nome], você é a única pessoa que me faz acreditar que histórias podem ser reais."
    menu:
        "Concordar com ela":
            $ romance_katia = True
            $ add_shared_memory("external_challenge_katia", ["katia"], "Desafio externo com Katia")
            $ add_affinity_points("katia", 10, "Superação do desafio externo")
            "[nome]" "E eu quero continuar escrevendo essa história com você."
            katia "Hmpf. Não se ache. Mas... obrigada por isso."
            narrator "Katia desvia o olhar, mas há um leve sorriso em seu rosto."
            jump cena5_domingo_para_dois
        "Ficar em silêncio":
            $ add_shared_memory("external_challenge_katia", ["katia"], "Desafio externo com Katia")
            $ add_affinity_points("katia", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Katia finge que não se importa, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label convite_huey:
    show huey gentle at center
    narrator "Huey segura o convite com cuidado, como se fosse algo frágil."
    huey "Eu não esperava isso... mas talvez seja uma oportunidade."
    narrator "No evento, seu ex está exibindo uma galeria de arte com obras que exploram emoções humanas. Huey decide ir para ver as obras, e você o acompanha."

    scene bg evento_huey with fade
    narrator "Huey observa as pinturas com atenção, seus olhos capturando cada detalhe. Após um tempo, seu ex se aproxima dele."
    show ex_huey confident at center
    ex_huey "Huey, você sempre teve um olhar único. Espero que ainda veja algo especial nas minhas obras."
    show huey gentle at center
    huey "Elas são boas. Mas acho que o que vejo agora é diferente... porque encontrei algo mais verdadeiro."
    narrator "Huey olha para você, seus olhos cheios de emoção."
    huey "[nome], você é a inspiração que eu nunca soube que precisava."
    menu:
        "Segurar sua mão":
            $ romance_huey = True
            $ add_shared_memory("external_challenge_huey", ["huey"], "Desafio externo com Huey")
            $ add_affinity_points("huey", 10, "Superação do desafio externo")
            "[nome]" "E você é a arte mais bonita que eu já vi."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorri timidamente, e o momento entre vocês parece cheio de significado."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            $ add_shared_memory("external_challenge_huey", ["huey"], "Desafio externo com Huey")
            $ add_affinity_points("huey", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Huey entende o que você sente, mas volta a observar as pinturas, como se algo tivesse ficado por dizer."
            jump cena5_domingo_para_dois

label convite_larissa:
    show larissa happy at center
    narrator "Larissa ri ao receber o convite, mas há algo em seu olhar que sugere incerteza."
    larissa "Ele sempre aparece nos momentos mais aleatórios. É quase engraçado."
    narrator "No evento, seu ex está organizando uma competição de atletismo. Larissa decide participar, e você a acompanha para torcer por ela."

    scene bg evento_larissa with fade
    narrator "Larissa corre com determinação, superando cada obstáculo com facilidade. Na linha de chegada, seu ex a parabeniza."
    show ex_larissa smug at center
    ex_larissa "Você ainda é incrível, Larissa. Mas será que ainda tem espaço para mim na sua vida?"
    show larissa happy at center
    larissa "Eu sou incrível porque aprendi a correr para frente, não para trás."
    narrator "Larissa olha para você, seu sorriso cheio de energia e sinceridade."
    larissa "[nome], você é a única pessoa que eu quero ao meu lado, em qualquer corrida."
    menu:
        "Abraçá-la":
            $ romance_larissa = True
            $ add_shared_memory("external_challenge_larissa", ["larissa"], "Desafio externo com Larissa")
            $ add_affinity_points("larissa", 10, "Superação do desafio externo")
            "[nome]" "E eu quero correr ao seu lado, em qualquer ritmo."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa ri, mas há algo mais profundo em seu olhar."
            jump cena5_domingo_para_dois
        "Dar um sorriso de apoio":
            $ add_shared_memory("external_challenge_larissa", ["larissa"], "Desafio externo com Larissa")
            $ add_affinity_points("larissa", 6, "Resposta neutra ao desafio externo")
            "[nome]" "..."
            narrator "Larissa entende o que você sente e sorri de volta, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label cena5_domingo_para_dois:
    narrator "Por acaso ou destino, você e [personagem_evento] acabam ficando sozinhos em casa por um dia. A energia muda."
    
    # Momento emocional de intimidade
    call emotional_moment("intimate_moment", None, "Momento íntimo que fortalece os laços") from _call_emotional_moment_cap7_5
    
    narrator "Era um momento especial, onde os corações se abriam e os laços se fortaleciam."

    if romance_camille:
        jump domingo_camille
    elif romance_samantha:
        jump domingo_samantha
    elif romance_nicole:
        jump domingo_nicole
    elif romance_katia:
        jump domingo_katia
    elif romance_huey:
        jump domingo_huey
    elif romance_larissa:
        jump domingo_larissa
    else:
        narrator "Algo deu errado. Nenhum romance está ativo."
        return

label domingo_camille:
    show camille gentle at center
    narrator "Você e Camille passam o dia meditando e conversando sobre o universo."
    camille "Sabe... às vezes, sinto que o tempo para quando estamos juntos."
    menu:
        "Concordar e se aproximar":
            $ romance_camille = True
            $ add_shared_memory("intimate_moment_camille", ["camille"], "Momento íntimo com Camille")
            $ add_affinity_points("camille", 8, "Conexão íntima profunda")
            "[nome]" "Eu sinto o mesmo. É como se o universo conspirasse a nosso favor."
            camille "Talvez ele esteja. Obrigada por estar aqui."
            narrator "Vocês compartilham um momento de conexão profunda."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_camille", ["camille"], "Momento íntimo com Camille")
            $ add_affinity_points("camille", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Camille observa você em silêncio, mas o momento parece incompleto."
            jump cena_final_escolha_silenciosa

label domingo_samantha:
    show samantha sad at center
    narrator "Você e Samantha passam o dia jogando videogame e conversando sobre estratégias."
    samantha "Sabe... às vezes, parece que você é meu player dois na vida real."
    menu:
        "Concordar e se aproximar":
            $ romance_samantha = True
            $ add_shared_memory("intimate_moment_samantha", ["samantha"], "Momento íntimo com Samantha")
            $ add_affinity_points("samantha", 8, "Conexão íntima profunda")
            "[nome]" "E você é minha melhor aliada. Sempre."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            narrator "Vocês compartilham um momento de conexão especial, como se fossem uma dupla imbatível."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_samantha", ["samantha"], "Momento íntimo com Samantha")
            $ add_affinity_points("samantha", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Samantha olha para você, esperando uma resposta, mas volta a focar no jogo."
            jump cena_final_escolha_silenciosa

label domingo_nicole:
    show nicole neutral at center
    narrator "Você e Nicole passam o dia organizando a casa e discutindo ideias para projetos futuros."
    nicole "Sabe... trabalhar com você é eficiente. Mas também... confortável."
    menu:
        "Concordar e se aproximar":
            $ romance_nicole = True
            $ add_shared_memory("intimate_moment_nicole", ["nicole"], "Momento íntimo com Nicole")
            $ add_affinity_points("nicole", 8, "Conexão íntima profunda")
            "[nome]" "Eu sinto o mesmo. Trabalhar com você é sempre especial."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer planilha."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_nicole", ["nicole"], "Momento íntimo com Nicole")
            $ add_affinity_points("nicole", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Nicole ajusta os óculos e volta a trabalhar, mas o silêncio entre vocês pareceu estranho."
            jump cena_final_escolha_silenciosa

label domingo_katia:
    show katia neutral at center
    narrator "Você e Katia passam o dia assistindo a filmes antigos e discutindo sobre eles."
    katia "Sabe... você é a única pessoa com quem eu consigo assistir isso sem me irritar."
    menu:
        "Concordar e se aproximar":
            $ romance_katia = True
            $ add_shared_memory("intimate_moment_katia", ["katia"], "Momento íntimo com Katia")
            $ add_affinity_points("katia", 8, "Conexão íntima profunda")
            "[nome]" "Talvez porque eu gosto de estar com você, mesmo que você finja que não gosta."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_katia", ["katia"], "Momento íntimo com Katia")
            $ add_affinity_points("katia", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Katia olha para você, esperando uma resposta, mas finge que não se importa."
            jump cena_final_escolha_silenciosa

label domingo_huey:
    show huey gentle at center
    narrator "Você e Huey passam o dia pintando juntos e conversando sobre arte."
    huey "Sabe... quando você está aqui, as cores parecem mais vivas."
    menu:
        "Concordar e se aproximar":
            $ romance_huey = True
            $ add_shared_memory("intimate_moment_huey", ["huey"], "Momento íntimo com Huey")
            $ add_affinity_points("huey", 8, "Conexão íntima profunda")
            "[nome]" "Talvez porque você me inspira a ver o mundo de um jeito diferente."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_huey", ["huey"], "Momento íntimo com Huey")
            $ add_affinity_points("huey", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Huey olha para você, mas volta a focar na pintura, como se algo tivesse ficado por dizer."
            jump cena_final_escolha_silenciosa

label domingo_larissa:
    show larissa happy at center
    narrator "Você e Larissa passam o dia treinando juntos e conversando sobre metas."
    larissa "Sabe... você é a única pessoa que eu deixo me acompanhar no treino."
    menu:
        "Concordar e se aproximar":
            $ romance_larissa = True
            $ add_shared_memory("intimate_moment_larissa", ["larissa"], "Momento íntimo com Larissa")
            $ add_affinity_points("larissa", 8, "Conexão íntima profunda")
            "[nome]" "Talvez porque eu quero estar ao seu lado, em qualquer ritmo."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            $ add_shared_memory("intimate_moment_larissa", ["larissa"], "Momento íntimo com Larissa")
            $ add_affinity_points("larissa", 4, "Resposta neutra ao momento íntimo")
            "[nome]" "..."
            narrator "Larissa olha para você, esperando uma resposta, mas volta a focar no treino."
            jump cena_final_escolha_silenciosa

label cena_final_escolha_silenciosa:
    narrator "Antes de dormir, o protagonista recebe uma mensagem de texto. Só uma frase, de [personagem_evento]"
    
    # Momento emocional de mensagem
    call emotional_moment("silent_message", None, "Mensagem silenciosa que fortalece os laços") from _call_emotional_moment_cap7_6
    
    narrator "Era um momento de conexão silenciosa, onde as palavras se tornavam desnecessárias."

    if personagem_evento == "camille":
        "[nome]" "Você sente quando alguém pensa em você à distância?"
    elif personagem_evento == "samantha":
        "[nome]" "Acabei de perder um boss... mas acho que ganhei uma mensagem importante."
    elif personagem_evento == "nicole":
        "[nome]" "A planilha ficou incompleta. Faltava você."
    elif personagem_evento == "katia":
        "[nome]" "Apaguei e reescrevi essa mensagem quatro vezes. Então... boa noite, idiota."
    elif personagem_evento == "huey":
        "[nome]" "Amanhã eu vou te mostrar a pintura. Só se você prometer não rir."
    elif personagem_evento == "larissa":
        "[nome]" "Se amanhã você quiser correr... me espera, tá?"

    menu:
        "Responder de forma afetuosa":
            $ add_shared_memory("silent_message_response", [personagem_evento], "Resposta afetuosa à mensagem silenciosa")
            $ add_affinity_points(personagem_evento, 6, "Resposta afetuosa à mensagem")
            narrator "Você responde com carinho, e a conexão entre vocês parece crescer ainda mais."
            jump cena_extra_madrugada
        "Responder com emoji simples":
            $ add_shared_memory("silent_message_response", [personagem_evento], "Resposta simples à mensagem silenciosa")
            $ add_affinity_points(personagem_evento, 3, "Resposta simples à mensagem")
            narrator "Você responde com um emoji simples. A mensagem é recebida, mas sem muito impacto."
            jump cena_extra_madrugada
        "Não responder":
            $ add_shared_memory("silent_message_response", [personagem_evento], "Sem resposta à mensagem silenciosa")
            $ add_affinity_points(personagem_evento, 1, "Sem resposta à mensagem")
            narrator "Você decide não responder. A personagem parece distante no dia seguinte."
            jump cena_extra_madrugada

label cena_extra_madrugada:
    narrator "Mais tarde, no silêncio da madrugada, o som de uma leve batida na porta ecoa pelo quarto. Uma das garotas aparece, com olhos sinceros."
    
    # Momento emocional da madrugada
    call emotional_moment("midnight_visit", None, "Visita da madrugada que fortalece os laços") from _call_emotional_moment_cap7_7
    
    narrator "Era um momento de vulnerabilidade, onde os corações se abriam e os laços se fortaleciam."

    if personagem_evento == "camille":
        jump madrugada_camille
    elif personagem_evento == "samantha":
        jump madrugada_samantha
    elif personagem_evento == "nicole":
        jump madrugada_nicole
    elif personagem_evento == "katia":
        jump madrugada_katia
    elif personagem_evento == "huey":
        jump madrugada_huey
    elif personagem_evento == "larissa":
        jump madrugada_larissa

label madrugada_camille:
    show camille neutral at center
    narrator "Camille entra no quarto, sentando no chão e acendendo um incenso discretamente."
    camille "Eu queria que esse momento durasse mais do que uma vida."
    menu:
        "Talvez a gente possa criar esse momento de novo. Sempre.":
            $ romance_camille = True
            $ add_shared_memory("midnight_visit_camille", ["camille"], "Visita da madrugada com Camille")
            $ add_affinity_points("camille", 12, "Conexão profunda da madrugada")
            "[nome]" "Talvez a gente possa criar esse momento de novo. Sempre."
            camille "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Camille sorriu suavemente, e o momento parecia cheio de significado."
            jump capitulo7_final

label madrugada_samantha:
    show samantha neutral at center
    narrator "Samantha aparece carregando dois controles de videogame, com um sorriso tímido."
    samantha "Se tudo mudar... posso salvar a gente num slot diferente?"
    menu:
        "Prefiro jogar nesse aqui, com você.":
            $ romance_samantha = True
            $ add_shared_memory("midnight_visit_samantha", ["samantha"], "Visita da madrugada com Samantha")
            $ add_affinity_points("samantha", 12, "Conexão profunda da madrugada")
            "[nome]" "Prefiro jogar nesse aqui, com você."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            narrator "Vocês compartilham um momento doce e envolvente, como se fossem uma dupla imbatível."
            jump capitulo7_final

label madrugada_nicole:
    show nicole neutral at center
    narrator "Nicole entra no quarto e senta à beira da cama, sua voz controlada, mas os olhos revelando algo mais."
    nicole "Você parece tranquilo... enquanto tudo ao nosso redor muda. Como faz isso?"
    menu:
        "Você me faz querer ficar.":
            $ romance_nicole = True
            $ add_shared_memory("midnight_visit_nicole", ["nicole"], "Visita da madrugada com Nicole")
            $ add_affinity_points("nicole", 12, "Conexão profunda da madrugada")
            "[nome]" "Você me faz querer ficar."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer planilha."
            jump capitulo7_final

label madrugada_katia:
    show katia neutral at center
    narrator "Katia aparece encostada no batente da porta, de braços cruzados, tentando parecer indiferente."
    katia "Se você comentar que eu bati aqui, eu juro que te ignoro o resto da vida."
    menu:
        "Então entra. Eu não falo... só ouço.":
            $ romance_katia = True
            $ add_shared_memory("midnight_visit_katia", ["katia"], "Visita da madrugada com Katia")
            $ add_affinity_points("katia", 12, "Conexão profunda da madrugada")
            "[nome]" "Então entra. Eu não falo... só ouço."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump capitulo7_final

label madrugada_huey:
    show huey neutral at center
    narrator "Huey entra no quarto segurando um croqui inacabado, com traços que parecem familiares."
    huey "Ainda tô desenhando... mas acho que já é você aqui, nesse traço."
    menu:
        "Quero ver você terminar. Comigo aqui.":
            $ romance_huey = True
            $ add_shared_memory("midnight_visit_huey", ["huey"], "Visita da madrugada com Huey")
            $ add_affinity_points("huey", 12, "Conexão profunda da madrugada")
            "[nome]" "Quero ver você terminar. Comigo aqui."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump capitulo7_final

label madrugada_larissa:
    show larissa neutral at center
    narrator "Larissa aparece segurando uma toalha, recém-saída do banho, com um sorriso brincalhão."
    larissa "Achei que talvez… a gente pudesse fazer flexão emocional juntos."
    larissa "(risos baixos)"
    menu:
        "Conta comigo. Até a última repetição.":
            $ romance_larissa = True
            $ add_shared_memory("midnight_visit_larissa", ["larissa"], "Visita da madrugada com Larissa")
            $ add_affinity_points("larissa", 12, "Conexão profunda da madrugada")
            "[nome]" "Conta comigo. Até a última repetição."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump capitulo7_final

label capitulo7_final:
    scene bg republica_noite with fade
    narrator "No final da noite, uma carta da administração da universidade chega... anunciando mudanças inesperadas no programa de moradia da república."

    # Momento emocional de mudança
    call emotional_moment("unexpected_changes", None, "Mudanças inesperadas que testam os laços") from _call_emotional_moment_cap7_8

    show nicole angry at center
    nicole "O quê?! Estão planejando redistribuir os moradores em novas casas no semestre seguinte..."
    nicole "Mas... isso significa que nossa família pode ser separada."
    $ add_affinity_points("nicole", 3, "Preocupação com a separação da família")
    hide nicole

    show camille shocked at left
    camille "O universo está mudando os ventos..."
    camille "Mas talvez seja um teste para ver o quanto nos importamos uns com os outros."
    $ add_affinity_points("camille", 3, "Conexão espiritual com as mudanças")
    hide camille

    narrator "Todos se olham em silêncio, pensando: 'Será que este é nosso último semestre juntos?'"

    # Retrospectiva dos relacionamentos
    narrator "Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(7)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap7_9
        
        narrator "[progress_message]"
        narrator "As mudanças inesperadas haviam testado a força dos laços que havíamos construído. Algo havia mudado em todos nós, criando conexões mais profundas e significativas."
        
        show samantha happy at left
        samantha "Parece que as mudanças realmente trouxeram mudanças, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. As mudanças inesperadas haviam sido mais que um desafio - haviam sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump capitulo8
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap7_10
        
        narrator "[progress_message]"
        narrator "As mudanças inesperadas haviam sido especiais, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. As mudanças foram apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. As mudanças inesperadas haviam sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo7_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo7_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 7 novamente":
                jump capitulo7