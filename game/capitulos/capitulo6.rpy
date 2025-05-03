label capitulo6:
    scene bg campus_festival with fade
    narrator "Solária se prepara para o tradicional Festival das Estações, um evento anual da universidade que mistura arte, esportes e espiritualidade. Cada grupo de moradores da república será responsável por montar uma barraca temática."

    show nicole neutral at left
    nicole "Se não entregarmos a proposta até amanhã de manhã, perdemos o stand."

    show camille gentle at center
    camille "O universo vai guiar… mas sim, é bom entregar no prazo."

    show katia neutral at right
    katia "A gente podia fazer uma tenda de filmes de terror interativos…"

    show huey neutral at left
    huey "Ou uma galeria com instalações sensoriais."

    show samantha happy at center
    samantha "E se for um stand de RPG ao vivo? Tipo, as pessoas passam por missões!"

    show larissa happy at right
    larissa "Dá pra ter uma parte com desafios físicos também! Mini circuito!"

    narrator "O grupo debate longamente, mas o protagonista é escolhido para tomar a decisão final da temática."

    menu:
        "RPG ao vivo (Samantha)":
            $ points_samantha += 1
            jump rpg_samantha
        "Tenda de terror interativo (Katia)":
            $ points_katia += 1
            jump terror_katia
        "Galeria sensorial de arte (Huey)":
            $ points_huey += 1
            jump galeria_huey
        "Circuito de desafios físicos (Larissa)":
            $ points_larissa += 1
            jump circuito_larissa
        "Espaço de equilíbrio energético e meditação (Camille)":
            $ points_camille += 1
            jump meditacao_camille
        "Planejamento de marca e experiências (Nicole)":
            $ points_nicole += 1
            jump planejamento_nicole

label rpg_samantha:
    narrator "Você escolheu o stand de RPG ao vivo. Samantha ficou animada com a ideia e começou a planejar as missões."
    jump reunioes_em_dupla

label terror_katia:
    narrator "Você escolheu a tenda de terror interativo. Katia sorriu de canto e começou a listar ideias assustadoras."
    jump reunioes_em_dupla

label galeria_huey:
    narrator "Você escolheu a galeria sensorial de arte. Huey parecia inspirada e começou a esboçar ideias no caderno."
    jump reunioes_em_dupla

label circuito_larissa:
    narrator "Você escolheu o circuito de desafios físicos. Larissa deu um soco no ar, animada para começar a planejar."
    jump reunioes_em_dupla

label meditacao_camille:
    narrator "Você escolheu o espaço de equilíbrio energético e meditação. Camille sorriu suavemente e começou a organizar os detalhes."
    jump reunioes_em_dupla

label planejamento_nicole:
    narrator "Você escolheu o planejamento de marca e experiências. Nicole ajustou os óculos e começou a estruturar o projeto."
    jump reunioes_em_dupla

label reunioes_em_dupla:
    scene bg sala_reuniao with dissolve
    narrator "Com a escolha feita, os grupos se dividem em duplas para desenvolver os detalhes. O protagonista é emparelhado com alguém aleatório, mas com maior chance de ser a personagem com maior afinidade."

    # Determina a personagem com maior afinidade
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_dupla = max(afinidades, key=afinidades.get)

    # Verifica quem será a dupla
    if personagem_dupla == "camille":
        jump dupla_camille
    elif personagem_dupla == "samantha":
        jump dupla_samantha
    elif personagem_dupla == "nicole":
        jump dupla_nicole
    elif personagem_dupla == "katia":
        jump dupla_katia
    elif personagem_dupla == "huey":
        jump dupla_huey
    elif personagem_dupla == "larissa":
        jump dupla_larissa

label dupla_camille:
    show camille gentle at center
    narrator "Você foi emparelhado com Camille para trabalhar no projeto. Ela parecia tranquila, mas havia algo pensativo em seu olhar."
    camille "Você acredita em destino? Que algumas coisas estão destinadas a acontecer, não importa o que façamos?"
    menu:
        "Sim, acredito em destino.":
            $ points_camille += 2
            "[nome]" "Sim, acho que algumas coisas estão além do nosso controle. Como se fossem escritas nas estrelas."
            camille "Eu sabia que você entenderia. É reconfortante pensar assim."
        "Não, acredito em escolhas.":
            $ points_camille += 1
            "[nome]" "Não, acho que somos responsáveis pelas nossas escolhas. O destino é o que fazemos dele."
            camille "Talvez você esteja certo. Mas às vezes, é bom acreditar em algo maior."
        "Não sei, nunca pensei nisso.":
            $ points_camille -= 1
            "[nome]" "Não sei. Nunca pensei muito sobre isso."
            camille "Talvez seja algo para refletir. Obrigada por compartilhar."
    narrator "Vocês continuaram trabalhando, mas a conversa deixou uma marca no ar, como se algo mais profundo tivesse sido compartilhado."
    jump capitulo6_evento_noturno

label dupla_samantha:
    show samantha happy at center
    narrator "Você foi emparelhado com Samantha para trabalhar no projeto. Ela parecia animada, mas havia uma leve hesitação em sua voz."
    samantha "Esse projeto vai ser épico. Mas se a gente errar o equilíbrio, vira só um joguinho bobo..."
    narrator "O trabalho foi fluido, mas no final, ela hesitou."
    samantha "Você já teve medo de ser bom demais em algo… e ainda assim ninguém se importar?"
    menu:
        "Confortar com empatia.":
            $ points_samantha += 2
            "[nome]" "Eu acho que você é incrível no que faz. E as pessoas percebem isso, mesmo que não digam."
            samantha "Obrigada... isso significa muito pra mim."
        "Responder de forma objetiva.":
            $ points_samantha += 1
            "[nome]" "Se você é boa, as pessoas vão notar. Só continue fazendo o que ama."
            samantha "É... talvez você tenha razão."
        "Minimizar a questão.":
            $ points_samantha -= 1
            "[nome]" "Não é tão importante assim. Só faça o que gosta."
            samantha "Ah... é, talvez."
    narrator "Vocês continuaram trabalhando, mas a conversa deixou algo no ar, como se ela tivesse compartilhado mais do que pretendia."
    jump capitulo6_evento_noturno

label dupla_nicole:
    show nicole neutral at center
    narrator "Você foi emparelhado com Nicole para trabalhar no projeto. Ela parecia focada, mas havia algo diferente em sua postura."
    nicole "Você já teve dificuldade em relaxar? Como se sempre houvesse algo que precisa ser feito?"
    menu:
        "Sim, eu entendo como é.":
            $ points_nicole += 2
            "[nome]" "Sim, eu entendo. Às vezes, é difícil desligar e apenas aproveitar o momento."
            nicole "É bom saber que não sou a única. Obrigada por entender."
        "Talvez você precise de um descanso.":
            $ points_nicole += 1
            "[nome]" "Talvez você só precise de um descanso. Todo mundo precisa de uma pausa às vezes."
            nicole "Talvez você esteja certo. Vou tentar pensar nisso."
        "Não, nunca tive esse problema.":
            $ points_nicole -= 1
            "[nome]" "Não, nunca tive esse problema. Sempre consigo relaxar."
            nicole "Entendi. Talvez seja só coisa minha, então."
    narrator "Nicole voltou ao trabalho, mas a conversa parecia ter deixado algo não dito entre vocês."
    jump capitulo6_evento_noturno

label dupla_katia:
    show katia neutral at center
    narrator "Você foi emparelhado com Katia para trabalhar no projeto. Ela parecia hesitante, mas havia algo vulnerável em sua voz."
    katia "Eu parei de escrever. Depois de... algumas coisas. Não sei se consigo voltar."
    menu:
        "Incentivar gentilmente.":
            $ points_katia += 2
            "[nome]" "Talvez você só precise de tempo. Mas eu acho que você deveria tentar. Você tem talento."
            katia "Obrigada... talvez eu tente. Um dia."
        "Ser direto.":
            $ points_katia += 1
            "[nome]" "Se é algo que você ama, você deveria tentar. Não deixe o medo te parar."
            katia "Você tem razão. Talvez eu esteja pensando demais."
        "Evitar o assunto.":
            $ points_katia -= 1
            "[nome]" "Se não quer falar sobre isso, tudo bem. Vamos focar no projeto."
            katia "É... melhor assim. Obrigada."
    narrator "Katia voltou ao trabalho, mas a conversa parecia ter deixado algo não resolvido entre vocês."
    jump capitulo6_evento_noturno

label dupla_huey:
    show huey gentle at center
    narrator "Você foi emparelhado com Huey para trabalhar no projeto. Ela parecia tranquila, mas havia algo diferente em seu olhar."
    huey "Eu quero te mostrar algo. É um caderno... mas é meio pessoal."
    narrator "Ela abriu o caderno, revelando autorretratos emocionais que pareciam capturar momentos de sua vida."
    menu:
        "Elogiar sinceramente.":
            $ points_huey += 2
            "[nome]" "Isso é incrível, Huey. Você colocou tanto de si aqui. É lindo."
            huey "Obrigada... significa muito ouvir isso de você."
        "Fazer uma pergunta curiosa.":
            $ points_huey += 1
            "[nome]" "Por que decidiu compartilhar isso comigo?"
            huey "Porque... acho que você entenderia. Obrigada por ouvir."
        "Evitar comentar.":
            $ points_huey -= 1
            "[nome]" "É interessante. Vamos voltar ao projeto?"
            huey "Ah... claro. Obrigada por olhar."
    narrator "Huey voltou ao trabalho, mas parecia mais reservada depois da conversa."
    jump capitulo6_evento_noturno

label dupla_larissa:
    show larissa happy at center
    narrator "Você foi emparelhado com Larissa para trabalhar no projeto. Ela parecia animada, mas havia algo nostálgico em sua voz."
    larissa "Eu costumava competir profissionalmente. Era... intenso. Mas sinto falta às vezes."
    menu:
        "Perguntar sobre as competições.":
            $ points_larissa += 2
            "[nome]" "Como era competir? Deve ter sido incrível."
            larissa "Era. Mas também era difícil. Obrigada por perguntar."
        "Elogiar sua dedicação.":
            $ points_larissa += 1
            "[nome]" "Você deve ter sido incrível. Sua dedicação é inspiradora."
            larissa "Obrigada. Isso significa muito pra mim."
        "Mudar de assunto.":
            $ points_larissa -= 1
            "[nome]" "Vamos focar no projeto. Podemos falar disso depois."
            larissa "Ah... claro. Sem problemas."
    narrator "Larissa voltou ao trabalho, mas parecia um pouco mais distante depois da conversa."
    jump capitulo6_evento_noturno

label capitulo6_evento_noturno:
    narrator "A noite cai e o campus se enche de luzes suaves. Todos os moradores da república participam do ritual do desejo, e o protagonista encontra-se com a personagem com maior afinidade."

    # Determina a personagem com maior afinidade
    $ personagem_evento = max(afinidades, key=afinidades.get)

    if personagem_evento == "camille":
        jump evento_camille
    elif personagem_evento == "samantha":
        jump evento_samantha
    elif personagem_evento == "nicole":
        jump evento_nicole
    elif personagem_evento == "katia":
        jump evento_katia
    elif personagem_evento == "huey":
        jump evento_huey
    elif personagem_evento == "larissa":
        jump evento_larissa

label evento_camille:
    show camille gentle at center
    narrator "Camille segura uma fita com um sorriso suave, seus olhos brilhando à luz das lanternas do festival."
    camille "Escrevi meu desejo com o coração. Mas ele só faz sentido se for partilhado."
    "[nome]" "E você quer compartilhar comigo?"
    camille "Sim. Você tem uma energia que me faz acreditar que os desejos podem se tornar realidade."
    narrator "Ela segura sua mão com firmeza enquanto prende a fita no galho. O toque é suave, mas cheio de significado."
    camille "Obrigada por existir no mesmo tempo que eu. Isso já é um presente."
    narrator "Por um momento, o mundo ao redor parece desaparecer, deixando apenas vocês dois sob as luzes do festival."
    $ points_camille += 1
    jump escolha_do_coracao

label evento_samantha:
    show samantha nervous at center
    narrator "Samantha segura uma fita, parecendo um pouco nervosa, enquanto olha para você."
    samantha "Eu... escrevi meu desejo, mas não consegui amarrar ainda. Estava esperando... você."
    "[nome]" "Por que eu?"
    samantha "Porque... talvez você entenda. Talvez você seja parte do que eu desejei."
    narrator "Ela te entrega a fita, e quando você toca, seus dedos se encostam levemente. Ela não recua, e por um instante, seus olhos se encontram."
    samantha "Talvez... eu esteja falando de mais do que jogos."
    narrator "Vocês amarram a fita juntos, e o sorriso de Samantha parece mais sincero do que nunca."
    $ points_samantha += 1
    jump escolha_do_coracao

label evento_nicole:
    show nicole neutral at center
    narrator "Nicole segura uma fita com um olhar pensativo, mas ao mesmo tempo, há algo suave em sua expressão."
    nicole "Eu não sou boa com essas coisas... mas achei que deveria tentar."
    "[nome]" "O que você desejou?"
    nicole "Algo simples. Algo que talvez já esteja acontecendo."
    narrator "Ela prende a fita no galho, mas hesita antes de soltar. Seus olhos encontram os seus, e por um momento, ela parece vulnerável."
    nicole "Obrigada por estar aqui. Isso... significa muito para mim."
    narrator "Nicole dá um pequeno sorriso, e o silêncio entre vocês é confortável, quase íntimo."
    $ points_nicole += 1
    jump escolha_do_coracao

label evento_katia:
    show katia neutral at center
    narrator "Katia segura uma fita, mas parece hesitante, como se não quisesse estar ali."
    katia "Eu não sei por que estou fazendo isso. Não acredito nessas coisas."
    "[nome]" "Então por que veio?"
    katia "Porque... talvez eu quisesse que você estivesse aqui comigo."
    narrator "Ela prende a fita no galho, mas não solta imediatamente. Seus dedos tremem levemente, e ela evita olhar diretamente para você."
    katia "Não significa nada, tá? Só... obrigada por estar aqui."
    narrator "Katia dá um sorriso tímido antes de se afastar, mas o momento entre vocês permanece."
    $ points_katia += 1
    jump escolha_do_coracao

label evento_huey:
    show huey gentle at center
    narrator "Huey segura uma fita com um sorriso tímido, suas mãos levemente manchadas de tinta."
    huey "Eu escrevi algo... mas não sei se faz sentido."
    "[nome]" "O que você escreveu?"
    huey "Algo sobre cores e sentimentos. Algo sobre você."
    narrator "Ela prende a fita no galho, mas seus olhos permanecem fixos nos seus. Há algo profundo e sincero em seu olhar."
    huey "Você me inspira. Obrigada por ser parte disso."
    narrator "Huey sorri, e por um momento, parece que o mundo inteiro está pintado em tons mais suaves e brilhantes."
    $ points_huey += 1
    jump escolha_do_coracao

label evento_larissa:
    show larissa happy at center
    narrator "Larissa segura uma fita com um sorriso animado, mas há algo mais suave em seus olhos."
    larissa "Eu escrevi meu desejo. Algo sobre encontrar alguém que acompanhe meu ritmo."
    "[nome]" "E você acha que vai encontrar?"
    larissa "Talvez... já tenha encontrado."
    narrator "Ela te dá uma cotovelada leve e sorri, mas há um rubor em suas bochechas que ela tenta esconder."
    larissa "Obrigada por estar aqui. Isso significa muito pra mim."
    narrator "Vocês amarram a fita juntos, e o sorriso de Larissa parece mais caloroso do que nunca."
    $ points_larissa += 1
    jump escolha_do_coracao

label evento_noturno_festival:
    narrator "A noite cai e o campus se enche de luzes suaves. Todos os moradores da república participam do ritual do desejo, e o protagonista encontra-se com a personagem com maior afinidade (mínimo de 6 pontos)."

    # Determina a personagem com maior afinidade (mínimo de 6 pontos)
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_evento = max(afinidades, key=afinidades.get)

    if afinidades[personagem_evento] < 6:
        jump evento_sem_afinidade
    elif personagem_evento == "camille":
        jump evento_camille
    elif personagem_evento == "samantha":
        jump evento_samantha
    elif personagem_evento == "nicole":
        jump evento_nicole
    elif personagem_evento == "katia":
        jump evento_katia
    elif personagem_evento == "huey":
        jump evento_huey
    elif personagem_evento == "larissa":
        jump evento_larissa

label escolha_do_coracao:
    narrator "A noite desce sobre Solária. O som distante das cigarras mistura-se ao sussurro do vento. Na sacada da república, o protagonista encontra algo inesperado... algo que só poderia vir de alguém especial."

    # Determina a personagem com maior afinidade (mínimo de 8 pontos)
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_evento = max(afinidades, key=afinidades.get)

    if afinidades[personagem_evento] < 8:
        jump escolha_sem_afinidade
    elif personagem_evento == "camille":
        jump escolha_camille
    elif personagem_evento == "samantha":
        jump escolha_samantha
    elif personagem_evento == "nicole":
        jump escolha_nicole
    elif personagem_evento == "katia":
        jump escolha_katia
    elif personagem_evento == "huey":
        jump escolha_huey
    elif personagem_evento == "larissa":
        jump escolha_larissa

label escolha_camille:
    show camille gentle at center
    narrator "Camille aparece em silêncio, segurando um cristal que reflete a luz da lua."
    camille "Você brilha… mesmo quando não percebe. E eu só queria me aproximar."
    camille "Este cristal é um reflexo do que sinto. Ele vibra na mesma frequência que você."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_camille = True
            "[nome]" "Então… posso sentar aqui mais vezes e respirar com você?"
            camille "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Camille sorriu suavemente, e o momento parecia cheio de significado."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_camille += 1
            "[nome]" "O tempo é um rio. E se nos encontrarmos na mesma margem de novo… saberei que é amor."
            camille "O tempo sempre nos guia. Obrigada por ser honesto."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_camille -= 1
            narrator "Camille olhou para você por um momento, antes de desviar o olhar."
            camille "Silêncio… também tem significado. Boa noite, então."
            narrator "Ela se despediu com um olhar melancólico, deixando o cristal na sacada."
            jump capitulo6_conclusao

label escolha_samantha:
    show samantha nervous at center
    narrator "Samantha aparece com um controle de videogame nas mãos, olhando para o céu."
    samantha "Eu ia só continuar jogando, mas... achei que devia tentar pessoalmente."
    samantha "Se a gente fosse personagens, você teria escolhido minha rota?"
    menu:
        "Reafirmar que também sente algo.":
            $ romance_samantha = True
            "[nome]" "Sério?! Tipo... sério mesmo? Nossa, isso foi um crítico de afeto."
            samantha "Você é incrível. Obrigada por me escolher."
            narrator "Samantha sorriu, e o momento parecia mais especial do que qualquer partida."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_samantha += 1
            "[nome]" "Tudo bem. Eu... posso esperar. Mas vou continuar salvando espaço pra você na party."
            samantha "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_samantha -= 1
            narrator "Samantha olhou para você, tentando esconder a decepção."
            samantha "Tá, eu entendi. Boa noite, então."
            narrator "Ela desceu as escadas em silêncio, segurando o controle com força."
            jump capitulo6_conclusao

label escolha_nicole:
    show nicole neutral at center
    narrator "Nicole aparece segurando um caderno com anotações precisas, mas há algo diferente em sua expressão."
    nicole "Eu estava revisando algumas hipóteses... mas percebi que precisava testar algo mais importante."
    nicole "Você."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_nicole = True
            "[nome]" "...Então tá. Vamos documentar isso com exclusividade."
            nicole "Você é... surpreendente. Obrigada por me deixar fazer parte disso."
            narrator "Nicole segurou sua mão com firmeza, e o momento parecia mais importante do que qualquer cálculo."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_nicole += 1
            "[nome]" "Tempo é um recurso não-renovável... mas se for você, eu invisto."
            nicole "Eu aceito. Obrigada por ser honesto."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_nicole -= 1
            narrator "Nicole ajustou os óculos, escondendo a decepção."
            nicole "Entendido. Silêncio também é uma resposta."
            narrator "Ela saiu, deixando o caderno sobre a mesa."
            jump capitulo6_conclusao

label escolha_katia:
    show katia neutral at center
    narrator "Katia aparece segurando um DVD antigo, com um sorriso de canto."
    katia "Não é como se eu tivesse esperado aqui ou algo assim... Só... passei."
    katia "Você tem esse talento estranho de... me deixar menos cínica."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_katia = True
            "[nome]" "Você é mais idiota do que eu pensava… Mas é meu idiota agora."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia fingiu desprezo, mas havia um sorriso sincero em seu rosto."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_katia += 1
            "[nome]" "Pff. Esperar nunca foi meu forte, mas... talvez valha a pena."
            katia "Talvez. Não me faça esperar muito."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_katia -= 1
            narrator "Katia jogou o DVD no chão, irritada."
            katia "…Isso é patético. Esquece."
            narrator "Ela saiu, batendo a porta atrás de si."
            jump capitulo6_conclusao

label escolha_huey:
    show huey gentle at center
    narrator "Huey aparece segurando um pequeno quadro embrulhado, com traços de tinta ainda fresca."
    huey "Fiz isso pensando em você. Não sabia se entregava… ou se deixava o tempo falar."
    huey "Mas estou aprendendo a mostrar. Aos poucos."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_huey = True
            "[nome]" "Então… posso pintar com você por mais tempo?"
            huey "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Huey sorriu, e o momento parecia cheio de significado."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_huey += 1
            "[nome]" "Tudo bem. Eu espero. E continuo pintando."
            huey "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_huey -= 1
            narrator "Huey olhou para você, tentando esconder a decepção."
            huey "Sem problema. Às vezes o silêncio também é arte."
            narrator "Ela saiu, deixando o quadro sobre a mesa."
            jump capitulo6_conclusao

label escolha_larissa:
    show larissa happy at center
    narrator "Larissa aparece com uma garrafa d’água e uma camiseta de treino, sorrindo de lado."
    larissa "Eu tava só… passando. Não que eu tenha vindo só por sua causa."
    larissa "Mas... se quiser correr comigo amanhã, eu finjo que você aguenta meu ritmo."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_larissa = True
            "[nome]" "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            larissa "Você é incrível. Obrigada por me escolher."
            narrator "Larissa sorriu, e o momento parecia mais especial do que qualquer treino."
            jump capitulo6_conclusao
        "Dizer que precisa de mais tempo.":
            $ points_larissa += 1
            "[nome]" "Tranquilo. A gente fortalece a amizade nos alongamentos."
            larissa "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_conclusao
        "Não responder.":
            $ points_larissa -= 1
            narrator "Larissa olhou para você, tentando esconder a decepção."
            larissa "Beleza. Valeu aí."
            narrator "Ela saiu, dando uma risada forçada."
            jump capitulo6_conclusao

label escolha_sem_afinidade:
    narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você volta para dentro, sentindo o peso do silêncio."
    narrator "Talvez, nos próximos capítulos, você consiga se aproximar mais deles."
    jump capitulo6_conclusao

label evento_sem_afinidade:
    narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você amarra sua fita sozinho. Ao longe, observa os grupos sorrindo juntos, criando uma leve sensação de distância."
    narrator "Talvez, nos próximos capítulos, você consiga se aproximar mais deles."
    jump capitulo6_conclusao

label capitulo6_conclusao:
    scene bg quarto_protagonista_noite with fade
    narrator "A noite chega ao fim, e você se encontra sozinho em seu quarto, refletindo sobre tudo o que aconteceu durante o Festival das Estações."

    # Retrospectiva baseada nas interações e eventos
    if personagem_evento == "camille":
        narrator "Os momentos com Camille foram marcados por uma conexão profunda e espiritual. Sua presença trouxe uma sensação de calma e significado ao festival."
        narrator "Você se lembra de como ela segurou sua mão enquanto amarravam a fita, e como suas palavras pareciam ecoar algo maior do que o momento."
        if romance_camille:
            narrator "O vínculo entre vocês parece ter se fortalecido ainda mais, como se o universo estivesse conspirando para aproximá-los."
        else:
            narrator "Embora o momento tenha sido especial, você sente que ainda há mais a explorar nessa conexão."
    elif personagem_evento == "samantha":
        narrator "Samantha trouxe energia e vulnerabilidade ao festival. Sua hesitação em amarrar a fita sozinha revelou um lado mais humano e sincero."
        narrator "Você se lembra de como seus dedos se tocaram levemente, e como ela sorriu, mesmo enquanto falava sobre algo mais profundo do que jogos."
        if romance_samantha:
            narrator "O festival marcou o início de algo especial entre vocês, como se vocês fossem aliados em uma nova jornada."
        else:
            narrator "Apesar do momento compartilhado, você sente que Samantha ainda está esperando algo mais de você."
    elif personagem_evento == "nicole":
        narrator "Nicole, com sua postura séria e calculada, mostrou um lado mais vulnerável durante o festival. Sua fita em branco foi um reflexo de sua busca por significado."
        narrator "Você se lembra de como ela hesitou antes de soltar a fita, e como suas palavras carregavam mais do que ela estava disposta a admitir."
        if romance_nicole:
            narrator "O vínculo entre vocês parece ter se transformado em algo mais profundo, como se ela finalmente tivesse encontrado alguém em quem confiar."
        else:
            narrator "Embora o momento tenha sido significativo, você sente que Nicole ainda está tentando entender o que quer."
    elif personagem_evento == "katia":
        narrator "Katia, com seu jeito defensivo e sarcástico, revelou um lado mais genuíno durante o festival. Sua hesitação em admitir o significado da fita foi um reflexo de sua luta interna."
        narrator "Você se lembra de como ela evitou contato visual, mas ainda assim, suas palavras carregavam um peso emocional."
        if romance_katia:
            narrator "O festival marcou o início de algo especial entre vocês, mesmo que ela tente esconder isso com seu sarcasmo habitual."
        else:
            narrator "Apesar do momento compartilhado, você sente que Katia ainda está tentando proteger seus sentimentos."
    elif personagem_evento == "huey":
        narrator "Huey trouxe sensibilidade e criatividade ao festival. Sua fita pintada foi um reflexo de sua alma artística e de como ela vê o mundo."
        narrator "Você se lembra de como ela encostou a testa na sua por um breve momento, e como suas palavras pareciam cheias de significado."
        if romance_huey:
            narrator "O vínculo entre vocês parece ter se aprofundado, como se vocês estivessem pintando uma nova história juntos."
        else:
            narrator "Embora o momento tenha sido especial, você sente que Huey ainda está esperando para compartilhar mais de si mesma."
    elif personagem_evento == "larissa":
        narrator "Larissa trouxe energia e leveza ao festival. Sua fita foi um reflexo de sua busca por alguém que pudesse acompanhar seu ritmo."
        narrator "Você se lembra de como ela te deu uma cotovelada leve e sorriu, tentando esconder o rubor em suas bochechas."
        if romance_larissa:
            narrator "O festival marcou o início de algo especial entre vocês, como se vocês fossem parceiros em uma corrida que nunca termina."
        else:
            narrator "Apesar do momento compartilhado, você sente que Larissa ainda está esperando para ver se você pode acompanhar seu ritmo."

    # Caso nenhuma personagem tenha afinidade suficiente
    if afinidades[personagem_evento] < 6:
        narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você passou o festival observando os outros moradores da república."
        narrator "Embora tenha sido uma experiência solitária, você sente que ainda há tempo para se aproximar deles nos próximos capítulos."

    narrator "Enquanto você se deita para dormir, as memórias do festival continuam a ecoar em sua mente. Cada momento compartilhado, cada palavra dita, parece ter deixado uma marca em você."
    narrator "Você percebe que, aos poucos, está construindo laços mais profundos com os moradores da república. E, talvez, o Festival das Estações tenha sido apenas o começo de algo maior."

    jump capitulo7