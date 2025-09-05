label capitulo6:
    if "capitulo6" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo6")
    
    scene bg campus_festival with fade
    narrator "Solária se prepara para o tradicional Festival das Estações, um evento anual da universidade que mistura arte, esportes e espiritualidade. Cada grupo de moradores da república será responsável por montar uma barraca temática."
    
    # Momento emocional de festival
    call emotional_moment("festival_preparation", None, "Preparação para o Festival das Estações que unirá todos") from _call_emotional_moment_cap6_1
    
    narrator "Havia algo especial no ar. O Festival das Estações não era apenas um evento - era uma oportunidade para mostrar ao mundo quem éramos como grupo, como família."

    show nicole neutral at left
    nicole "Se não entregarmos a proposta até amanhã de manhã, perdemos o stand."
    nicole "Mas tenho certeza de que vamos criar algo incrível juntos."
    $ add_affinity_points("nicole", 3, "Confiança no grupo")
    hide nicole

    show camille gentle at center
    camille "O universo vai guiar… mas sim, é bom entregar no prazo."
    camille "Sinto que este festival será especial para todos nós."
    $ add_affinity_points("camille", 3, "Conexão espiritual com o festival")
    hide camille

    show katia neutral at right
    katia "A gente podia fazer uma tenda de filmes de terror interativos…"
    katia "N-não é como se eu estivesse animada ou qualquer coisa assim! É só que... seria interessante."
    $ add_affinity_points("katia", 2, "Interesse tsundere no festival")
    hide katia

    show huey neutral at left
    huey "Ou uma galeria com instalações sensoriais."
    huey "Cada pessoa aqui é uma obra de arte, e o festival será nosso palco!"
    $ add_affinity_points("huey", 3, "Inspiração artística para o festival")
    hide huey

    show samantha happy at center
    samantha "E se for um stand de RPG ao vivo? Tipo, as pessoas passam por missões!"
    samantha "Seria como uma aventura épica que criamos juntos!"
    $ add_affinity_points("samantha", 3, "Entusiasmo com a aventura")
    hide samantha

    show larissa happy at right
    larissa "Dá pra ter uma parte com desafios físicos também! Mini circuito!"
    larissa "Vamos mostrar nossa energia e determinação!"
    $ add_affinity_points("larissa", 3, "Energia contagiante para o festival")
    hide larissa

    narrator "O grupo debate longamente, mas o protagonista é escolhido para tomar a decisão final da temática."

    menu:
        "RPG ao vivo (Samantha) - Aventura e criatividade":
            $ add_shared_memory("festival_rpg_choice", ["samantha"], "Escolha do stand de RPG ao vivo para o festival")
            $ add_affinity_points("samantha", 8, "Escolha do tema do festival")
            jump rpg_samantha
            
        "Tenda de terror interativo (Katia) - Arte e entretenimento":
            $ add_shared_memory("festival_horror_choice", ["katia"], "Escolha da tenda de terror interativo para o festival")
            $ add_affinity_points("katia", 8, "Escolha do tema do festival")
            jump terror_katia
            
        "Galeria sensorial de arte (Huey) - Criatividade e expressão":
            $ add_shared_memory("festival_art_choice", ["huey"], "Escolha da galeria sensorial de arte para o festival")
            $ add_affinity_points("huey", 8, "Escolha do tema do festival")
            jump galeria_huey
            
        "Circuito de desafios físicos (Larissa) - Energia e movimento":
            $ add_shared_memory("festival_physical_choice", ["larissa"], "Escolha do circuito de desafios físicos para o festival")
            $ add_affinity_points("larissa", 8, "Escolha do tema do festival")
            jump circuito_larissa
            
        "Espaço de equilíbrio energético e meditação (Camille) - Espiritualidade e paz":
            $ add_shared_memory("festival_spiritual_choice", ["camille"], "Escolha do espaço de equilíbrio energético para o festival")
            $ add_affinity_points("camille", 8, "Escolha do tema do festival")
            jump meditacao_camille
            
        "Planejamento de marca e experiências (Nicole) - Estratégia e organização":
            $ add_shared_memory("festival_strategy_choice", ["nicole"], "Escolha do planejamento de marca para o festival")
            $ add_affinity_points("nicole", 8, "Escolha do tema do festival")
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
    
    # Momento emocional de trabalho em dupla
    call emotional_moment("duo_work_session", None, "Trabalho em dupla que fortalece os laços") from _call_emotional_moment_cap6_2
    
    narrator "Era hora de trabalhar juntos, de criar algo especial que representasse nossa união como grupo."

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
            $ add_shared_memory("duo_destiny_conversation", ["camille"], "Conversa sobre destino durante trabalho em dupla")
            $ add_affinity_points("camille", 6, "Conexão espiritual profunda")
            "[nome]" "Sim, acho que algumas coisas estão além do nosso controle. Como se fossem escritas nas estrelas."
            camille "Eu sabia que você entenderia. É reconfortante pensar assim."
        "Não, acredito em escolhas.":
            $ add_shared_memory("duo_choices_conversation", ["camille"], "Conversa sobre escolhas durante trabalho em dupla")
            $ add_affinity_points("camille", 4, "Respeito por diferentes perspectivas")
            "[nome]" "Não, acho que somos responsáveis pelas nossas escolhas. O destino é o que fazemos dele."
            camille "Talvez você esteja certo. Mas às vezes, é bom acreditar em algo maior."
        "Não sei, nunca pensei nisso.":
            $ add_shared_memory("duo_uncertainty_conversation", ["camille"], "Conversa sobre incerteza durante trabalho em dupla")
            $ add_affinity_points("camille", 2, "Honestidade sobre incerteza")
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
            $ add_shared_memory("duo_empathy_conversation", ["samantha"], "Conversa sobre empatia durante trabalho em dupla")
            $ add_affinity_points("samantha", 6, "Conexão emocional profunda")
            "[nome]" "Eu acho que você é incrível no que faz. E as pessoas percebem isso, mesmo que não digam."
            samantha "Obrigada... isso significa muito pra mim."
        "Responder de forma objetiva.":
            $ add_shared_memory("duo_objective_conversation", ["samantha"], "Conversa objetiva durante trabalho em dupla")
            $ add_affinity_points("samantha", 4, "Apoio prático")
            "[nome]" "Se você é boa, as pessoas vão notar. Só continue fazendo o que ama."
            samantha "É... talvez você tenha razão."
        "Minimizar a questão.":
            $ add_shared_memory("duo_minimizing_conversation", ["samantha"], "Conversa que minimiza durante trabalho em dupla")
            $ add_affinity_points("samantha", 2, "Resposta neutra")
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
            $ add_shared_memory("duo_understanding_conversation", ["nicole"], "Conversa sobre compreensão durante trabalho em dupla")
            $ add_affinity_points("nicole", 6, "Conexão emocional profunda")
            "[nome]" "Sim, eu entendo. Às vezes, é difícil desligar e apenas aproveitar o momento."
            nicole "É bom saber que não sou a única. Obrigada por entender."
        "Talvez você precise de um descanso.":
            $ add_shared_memory("duo_rest_conversation", ["nicole"], "Conversa sobre descanso durante trabalho em dupla")
            $ add_affinity_points("nicole", 4, "Cuidado e preocupação")
            "[nome]" "Talvez você só precise de um descanso. Todo mundo precisa de uma pausa às vezes."
            nicole "Talvez você esteja certo. Vou tentar pensar nisso."
        "Não, nunca tive esse problema.":
            $ add_shared_memory("duo_dismissal_conversation", ["nicole"], "Conversa que dispensa durante trabalho em dupla")
            $ add_affinity_points("nicole", 2, "Resposta neutra")
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
            $ add_shared_memory("duo_gentle_encouragement", ["katia"], "Incentivo gentil durante trabalho em dupla")
            $ add_affinity_points("katia", 6, "Conexão emocional profunda")
            "[nome]" "Talvez você só precise de tempo. Mas eu acho que você deveria tentar. Você tem talento."
            katia "Obrigada... talvez eu tente. Um dia."
        "Ser direto.":
            $ add_shared_memory("duo_direct_encouragement", ["katia"], "Incentivo direto durante trabalho em dupla")
            $ add_affinity_points("katia", 4, "Apoio direto")
            "[nome]" "Se é algo que você ama, você deveria tentar. Não deixe o medo te parar."
            katia "Você tem razão. Talvez eu esteja pensando demais."
        "Evitar o assunto.":
            $ add_shared_memory("duo_avoidance", ["katia"], "Evitação do assunto durante trabalho em dupla")
            $ add_affinity_points("katia", 2, "Resposta neutra")
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
            $ add_shared_memory("duo_sincere_praise", ["huey"], "Elogio sincero durante trabalho em dupla")
            $ add_affinity_points("huey", 6, "Conexão emocional profunda")
            "[nome]" "Isso é incrível, Huey. Você colocou tanto de si aqui. É lindo."
            huey "Obrigada... significa muito ouvir isso de você."
        "Fazer uma pergunta curiosa.":
            $ add_shared_memory("duo_curious_question", ["huey"], "Pergunta curiosa durante trabalho em dupla")
            $ add_affinity_points("huey", 4, "Interesse genuíno")
            "[nome]" "Por que decidiu compartilhar isso comigo?"
            huey "Porque... acho que você entenderia. Obrigada por ouvir."
        "Evitar comentar.":
            $ add_shared_memory("duo_avoidance_comment", ["huey"], "Evitação de comentário durante trabalho em dupla")
            $ add_affinity_points("huey", 2, "Resposta neutra")
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
            $ add_shared_memory("duo_competition_question", ["larissa"], "Pergunta sobre competições durante trabalho em dupla")
            $ add_affinity_points("larissa", 6, "Conexão emocional profunda")
            "[nome]" "Como era competir? Deve ter sido incrível."
            larissa "Era. Mas também era difícil. Obrigada por perguntar."
        "Elogiar sua dedicação.":
            $ add_shared_memory("duo_dedication_praise", ["larissa"], "Elogio à dedicação durante trabalho em dupla")
            $ add_affinity_points("larissa", 4, "Apreciação sincera")
            "[nome]" "Você deve ter sido incrível. Sua dedicação é inspiradora."
            larissa "Obrigada. Isso significa muito pra mim."
        "Mudar de assunto.":
            $ add_shared_memory("duo_subject_change", ["larissa"], "Mudança de assunto durante trabalho em dupla")
            $ add_affinity_points("larissa", 2, "Resposta neutra")
            "[nome]" "Vamos focar no projeto. Podemos falar disso depois."
            larissa "Ah... claro. Sem problemas."
    narrator "Larissa voltou ao trabalho, mas parecia um pouco mais distante depois da conversa."
    jump capitulo6_evento_noturno

label capitulo6_evento_noturno:
    narrator "A noite cai e o campus se enche de luzes suaves. Todos os moradores da república participam do ritual do desejo, e o protagonista encontra-se com a personagem com maior afinidade."
    
    # Momento emocional de ritual do desejo
    call emotional_moment("wish_ritual", None, "Ritual do desejo que fortalece os laços") from _call_emotional_moment_cap6_3
    
    narrator "Era um momento mágico, onde os desejos se tornavam visíveis e os corações se abriam."

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
    $ add_affinity_points("camille", 8, "Ritual do desejo especial")
    jump escolha_do_coracao

label evento_samantha:
    show samantha sad at center
    narrator "Samantha segura uma fita, parecendo um pouco nervosa, enquanto olha para você."
    samantha "Eu... escrevi meu desejo, mas não consegui amarrar ainda. Estava esperando... você."
    "[nome]" "Por que eu?"
    samantha "Porque... talvez você entenda. Talvez você seja parte do que eu desejei."
    narrator "Ela te entrega a fita, e quando você toca, seus dedos se encostam levemente. Ela não recua, e por um instante, seus olhos se encontram."
    samantha "Talvez... eu esteja falando de mais do que jogos."
    narrator "Vocês amarram a fita juntos, e o sorriso de Samantha parece mais sincero do que nunca."
    $ add_affinity_points("samantha", 8, "Ritual do desejo especial")
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
    $ add_affinity_points("nicole", 8, "Ritual do desejo especial")
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
    $ add_affinity_points("katia", 8, "Ritual do desejo especial")
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
    $ add_affinity_points("huey", 8, "Ritual do desejo especial")
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
    $ add_affinity_points("larissa", 8, "Ritual do desejo especial")
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
    
    # Momento emocional de escolha do coração
    call emotional_moment("heart_choice", None, "Escolha do coração que define o futuro") from _call_emotional_moment_cap6_4
    
    narrator "Era um momento decisivo, onde os corações se abriam e os sentimentos se revelavam."

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
            $ add_shared_memory("heart_choice_romance", ["camille"], "Escolha romântica do coração")
            $ add_affinity_points("camille", 12, "Confissão de amor")
            "[nome]" "Então… posso sentar aqui mais vezes e respirar com você?"
            camille "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Camille sorriu suavemente, e o momento parecia cheio de significado."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["camille"], "Escolha de tempo para o coração")
            $ add_affinity_points("camille", 8, "Honestidade sobre sentimentos")
            "[nome]" "O tempo é um rio. E se nos encontrarmos na mesma margem de novo… saberei que é amor."
            camille "O tempo sempre nos guia. Obrigada por ser honesto."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["camille"], "Escolha de silêncio para o coração")
            $ add_affinity_points("camille", 4, "Resposta neutra")
            narrator "Camille olhou para você por um momento, antes de desviar o olhar."
            camille "Silêncio… também tem significado. Boa noite, então."
            narrator "Ela se despediu com um olhar melancólico, deixando o cristal na sacada."
            jump capitulo6_final

label escolha_samantha:
    show samantha sad at center
    narrator "Samantha aparece com um controle de videogame nas mãos, olhando para o céu."
    samantha "Eu ia só continuar jogando, mas... achei que devia tentar pessoalmente."
    samantha "Se a gente fosse personagens, você teria escolhido minha rota?"
    menu:
        "Reafirmar que também sente algo.":
            $ romance_samantha = True
            $ add_shared_memory("heart_choice_romance", ["samantha"], "Escolha romântica do coração")
            $ add_affinity_points("samantha", 12, "Confissão de amor")
            "[nome]" "Sério?! Tipo... sério mesmo? Nossa, isso foi um crítico de afeto."
            samantha "Você é incrível. Obrigada por me escolher."
            narrator "Samantha sorriu, e o momento parecia mais especial do que qualquer partida."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["samantha"], "Escolha de tempo para o coração")
            $ add_affinity_points("samantha", 8, "Honestidade sobre sentimentos")
            "[nome]" "Tudo bem. Eu... posso esperar. Mas vou continuar salvando espaço pra você na party."
            samantha "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["samantha"], "Escolha de silêncio para o coração")
            $ add_affinity_points("samantha", 4, "Resposta neutra")
            narrator "Samantha olhou para você, tentando esconder a decepção."
            samantha "Tá, eu entendi. Boa noite, então."
            narrator "Ela desceu as escadas em silêncio, segurando o controle com força."
            jump capitulo6_final

label escolha_nicole:
    show nicole neutral at center
    narrator "Nicole aparece segurando um caderno com anotações precisas, mas há algo diferente em sua expressão."
    nicole "Eu estava revisando algumas hipóteses... mas percebi que precisava testar algo mais importante."
    nicole "Você."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_nicole = True
            $ add_shared_memory("heart_choice_romance", ["nicole"], "Escolha romântica do coração")
            $ add_affinity_points("nicole", 12, "Confissão de amor")
            "[nome]" "...Então tá. Vamos documentar isso com exclusividade."
            nicole "Você é... surpreendente. Obrigada por me deixar fazer parte disso."
            narrator "Nicole segurou sua mão com firmeza, e o momento parecia mais importante do que qualquer cálculo."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["nicole"], "Escolha de tempo para o coração")
            $ add_affinity_points("nicole", 8, "Honestidade sobre sentimentos")
            "[nome]" "Tempo é um recurso não-renovável... mas se for você, eu invisto."
            nicole "Eu aceito. Obrigada por ser honesto."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["nicole"], "Escolha de silêncio para o coração")
            $ add_affinity_points("nicole", 4, "Resposta neutra")
            narrator "Nicole ajustou os óculos, escondendo a decepção."
            nicole "Entendido. Silêncio também é uma resposta."
            narrator "Ela saiu, deixando o caderno sobre a mesa."
            jump capitulo6_final

label escolha_katia:
    show katia neutral at center
    narrator "Katia aparece segurando um DVD antigo, com um sorriso de canto."
    katia "Não é como se eu tivesse esperado aqui ou algo assim... Só... passei."
    katia "Você tem esse talento estranho de... me deixar menos cínica."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_katia = True
            $ add_shared_memory("heart_choice_romance", ["katia"], "Escolha romântica do coração")
            $ add_affinity_points("katia", 12, "Confissão de amor")
            "[nome]" "Você é mais idiota do que eu pensava… Mas é meu idiota agora."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia fingiu desprezo, mas havia um sorriso sincero em seu rosto."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["katia"], "Escolha de tempo para o coração")
            $ add_affinity_points("katia", 8, "Honestidade sobre sentimentos")
            "[nome]" "Pff. Esperar nunca foi meu forte, mas... talvez valha a pena."
            katia "Talvez. Não me faça esperar muito."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["katia"], "Escolha de silêncio para o coração")
            $ add_affinity_points("katia", 4, "Resposta neutra")
            narrator "Katia jogou o DVD no chão, irritada."
            katia "…Isso é patético. Esquece."
            narrator "Ela saiu, batendo a porta atrás de si."
            jump capitulo6_final

label escolha_huey:
    show huey gentle at center
    narrator "Huey aparece segurando um pequeno quadro embrulhado, com traços de tinta ainda fresca."
    huey "Fiz isso pensando em você. Não sabia se entregava… ou se deixava o tempo falar."
    huey "Mas estou aprendendo a mostrar. Aos poucos."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_huey = True
            $ add_shared_memory("heart_choice_romance", ["huey"], "Escolha romântica do coração")
            $ add_affinity_points("huey", 12, "Confissão de amor")
            "[nome]" "Então… posso pintar com você por mais tempo?"
            huey "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Huey sorriu, e o momento parecia cheio de significado."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["huey"], "Escolha de tempo para o coração")
            $ add_affinity_points("huey", 8, "Honestidade sobre sentimentos")
            "[nome]" "Tudo bem. Eu espero. E continuo pintando."
            huey "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["huey"], "Escolha de silêncio para o coração")
            $ add_affinity_points("huey", 4, "Resposta neutra")
            narrator "Huey olhou para você, tentando esconder a decepção."
            huey "Sem problema. Às vezes o silêncio também é arte."
            narrator "Ela saiu, deixando o quadro sobre a mesa."
            jump capitulo6_final

label escolha_larissa:
    show larissa happy at center
    narrator "Larissa aparece com uma garrafa d’água e uma camiseta de treino, sorrindo de lado."
    larissa "Eu tava só… passando. Não que eu tenha vindo só por sua causa."
    larissa "Mas... se quiser correr comigo amanhã, eu finjo que você aguenta meu ritmo."
    menu:
        "Reafirmar que também sente algo.":
            $ romance_larissa = True
            $ add_shared_memory("heart_choice_romance", ["larissa"], "Escolha romântica do coração")
            $ add_affinity_points("larissa", 12, "Confissão de amor")
            "[nome]" "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            larissa "Você é incrível. Obrigada por me escolher."
            narrator "Larissa sorriu, e o momento parecia mais especial do que qualquer treino."
            jump capitulo6_final
        "Dizer que precisa de mais tempo.":
            $ add_shared_memory("heart_choice_time", ["larissa"], "Escolha de tempo para o coração")
            $ add_affinity_points("larissa", 8, "Honestidade sobre sentimentos")
            "[nome]" "Tranquilo. A gente fortalece a amizade nos alongamentos."
            larissa "Obrigada. Eu espero que um dia você me escolha."
            jump capitulo6_final
        "Não responder.":
            $ add_shared_memory("heart_choice_silence", ["larissa"], "Escolha de silêncio para o coração")
            $ add_affinity_points("larissa", 4, "Resposta neutra")
            narrator "Larissa olhou para você, tentando esconder a decepção."
            larissa "Beleza. Valeu aí."
            narrator "Ela saiu, dando uma risada forçada."
            jump capitulo6_final

label escolha_sem_afinidade:
    narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você volta para dentro, sentindo o peso do silêncio."
    narrator "Talvez, nos próximos capítulos, você consiga se aproximar mais deles."
    jump capitulo6_final

label evento_sem_afinidade:
    narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você amarra sua fita sozinho. Ao longe, observa os grupos sorrindo juntos, criando uma leve sensação de distância."
    narrator "Talvez, nos próximos capítulos, você consiga se aproximar mais deles."
    jump capitulo6_final

label capitulo6_final:
    scene bg quarto_protagonista_noite with fade
    narrator "A noite chega ao fim, e você se encontra sozinho em seu quarto, refletindo sobre tudo o que aconteceu durante o Festival das Estações."

    # Momento emocional de reflexão sobre o festival
    call emotional_moment("festival_reflection", None, "Reflexão sobre o Festival das Estações e os momentos especiais compartilhados") from _call_emotional_moment_cap6_5

    # Retrospectiva baseada nas interações e eventos
    if personagem_evento == "camille":
        narrator "Os momentos com Camille foram marcados por uma conexão profunda e espiritual. Sua presença trouxe uma sensação de calma e significado ao festival."
        show camille gentle at left
        camille "O festival foi um momento de transformação para todos nós. Sinto que algo mudou dentro de mim."
        narrator "Você se lembra de como ela segurou sua mão enquanto amarravam a fita, e como suas palavras pareciam ecoar algo maior do que o momento."
        if romance_camille:
            narrator "O vínculo entre vocês parece ter se fortalecido ainda mais, como se o universo estivesse conspirando para aproximá-los."
        else:
            narrator "Embora o momento tenha sido especial, você sente que ainda há mais a explorar nessa conexão."
        hide camille
    elif personagem_evento == "samantha":
        narrator "Samantha trouxe energia e vulnerabilidade ao festival. Sua hesitação em amarrar a fita sozinha revelou um lado mais humano e sincero."
        show samantha happy at left
        samantha "O festival foi incrível! É como se o universo tivesse preparado uma aventura perfeita para nós!"
        narrator "Você se lembra de como seus dedos se tocaram levemente, e como ela sorriu, mesmo enquanto falava sobre algo mais profundo do que jogos."
        if romance_samantha:
            narrator "O festival marcou o início de algo especial entre vocês, como se vocês fossem aliados em uma nova jornada."
        else:
            narrator "Apesar do momento compartilhado, você sente que Samantha ainda está esperando algo mais de você."
        hide samantha
    elif personagem_evento == "nicole":
        narrator "Nicole, com sua postura séria e calculada, mostrou um lado mais vulnerável durante o festival. Sua fita em branco foi um reflexo de sua busca por significado."
        show nicole neutral at left
        nicole "O festival me fez perceber que nem tudo precisa ser perfeitamente organizado. Às vezes, a beleza está na espontaneidade."
        narrator "Você se lembra de como ela hesitou antes de soltar a fita, e como suas palavras carregavam mais do que ela estava disposta a admitir."
        if romance_nicole:
            narrator "O vínculo entre vocês parece ter se transformado em algo mais profundo, como se ela finalmente tivesse encontrado alguém em quem confiar."
        else:
            narrator "Embora o momento tenha sido significativo, você sente que Nicole ainda está tentando entender o que quer."
        hide nicole
    elif personagem_evento == "katia":
        narrator "Katia, com seu jeito defensivo e sarcástico, revelou um lado mais genuíno durante o festival. Sua hesitação em admitir o significado da fita foi um reflexo de sua luta interna."
        show katia neutral at left
        katia "N-não é como se eu tivesse gostado do festival ou qualquer coisa assim! É só que... foi menos chato com você por perto."
        narrator "Você se lembra de como ela evitou contato visual, mas ainda assim, suas palavras carregavam um peso emocional."
        if romance_katia:
            narrator "O festival marcou o início de algo especial entre vocês, mesmo que ela tente esconder isso com seu sarcasmo habitual."
        else:
            narrator "Apesar do momento compartilhado, você sente que Katia ainda está tentando proteger seus sentimentos."
        hide katia
    elif personagem_evento == "huey":
        narrator "Huey trouxe sensibilidade e criatividade ao festival. Sua fita pintada foi um reflexo de sua alma artística e de como ela vê o mundo."
        show huey happy at left
        huey "Pintar durante o festival foi mágico! Cada pessoa aqui é uma obra de arte, e o festival foi o cenário perfeito!"
        narrator "Você se lembra de como ela encostou a testa na sua por um breve momento, e como suas palavras pareciam cheias de significado."
        if romance_huey:
            narrator "O vínculo entre vocês parece ter se aprofundado, como se vocês estivessem pintando uma nova história juntos."
        else:
            narrator "Embora o momento tenha sido especial, você sente que Huey ainda está esperando para compartilhar mais de si mesma."
        hide huey
    elif personagem_evento == "larissa":
        narrator "Larissa trouxe energia e leveza ao festival. Sua fita foi um reflexo de sua busca por alguém que pudesse acompanhar seu ritmo."
        show larissa happy at left
        larissa "Correr durante o festival foi incrível! É como se a energia cósmica tivesse nos impulsionado!"
        narrator "Você se lembra de como ela te deu uma cotovelada leve e sorriu, tentando esconder o rubor em suas bochechas."
        if romance_larissa:
            narrator "O festival marcou o início de algo especial entre vocês, como se vocês fossem parceiros em uma corrida que nunca termina."
        else:
            narrator "Apesar do momento compartilhado, você sente que Larissa ainda está esperando para ver se você pode acompanhar seu ritmo."
        hide larissa

    # Caso nenhuma personagem tenha afinidade suficiente
    if afinidades[personagem_evento] < 6:
        narrator "Sem ninguém próximo o suficiente para compartilhar o momento, você passou o festival observando os outros moradores da república."
        narrator "Embora tenha sido uma experiência solitária, você sente que ainda há tempo para se aproximar deles nos próximos capítulos."

    # Retrospectiva dos relacionamentos
    narrator "Enquanto você se deita para dormir, as memórias do festival continuam a ecoar em sua mente. Cada momento compartilhado, cada palavra dita, parece ter deixado uma marca em você."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(6)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap6_6
        
        narrator "[progress_message]"
        narrator "O Festival das Estações havia sido um momento de transformação. Algo havia mudado em todos nós, criando conexões mais profundas e significativas."
        
        show samantha happy at left
        samantha "Parece que o festival realmente trouxe mudanças, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. O Festival das Estações havia sido mais que um evento - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump capitulo7
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap6_7
        
        narrator "[progress_message]"
        narrator "O Festival das Estações havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. O festival foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. O Festival das Estações havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo6_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo6_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 6 novamente":
                jump capitulo6