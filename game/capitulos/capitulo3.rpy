label capitulo3:
    if "capitulo3" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo3")
    
    # Cena 1 – Aviso Inesperado
    scene bg campus_morning with fade
    narrator "Na manhã de uma segunda-feira, [nome] chega ao campus e percebe uma agitação incomum. Cartazes estão sendo pregados às pressas, e há um burburinho geral entre os estudantes."
    
    # Momento emocional de mudança
    call emotional_moment("life_changing_event", None, "Um evento que mudará a vida de todos para sempre") from _call_emotional_moment_cap3_1

    show professor_wendell neutral at center
    professor_wendell "Atenção, alunos da moradia estudantil Alfa e Beta: por conta de infiltrações estruturais, os dormitórios estão interditados. Vocês serão realocados temporariamente em casas compartilhadas."

    hide professor_wendell neutral
    "[nome]" "Casa compartilhada… Rua Aurora, número 57. Espera… esse é o meu endereço!"
    
    narrator "Meu coração acelerou. Isso não podia estar acontecendo. A casa que eu havia escolhido para viver sozinho estava prestes a se tornar o lar de todo o grupo."

    scene bg rua_aurora with dissolve
    narrator "Ao chegar em casa, ele encontra todas as garotas do grupo na frente do portão, cada uma com sua mala."
    
    # Momento emocional de descoberta
    call emotional_moment("unexpected_reunion", None, "Reunião inesperada que mudará tudo") from _call_emotional_moment_cap3_2
    
    show samantha happy at left
    samantha "O quê?! Você também vai morar aqui?!"
    samantha "Isso é... isso é incrível! Vamos poder trabalhar juntos nos projetos toda hora!"
    $ add_affinity_points("samantha", 5, "Entusiasmo com a convivência")
    hide samantha happy

    show katia neutral at center
    katia "Isso só pode ser pegadinha."
    katia "N-não é como se eu estivesse... animada ou qualquer coisa assim! É só que... é estranho."
    $ add_affinity_points("katia", 3, "Reação tsundere à convivência")
    hide katia neutral
    
    show camille gentle at right
    camille "Talvez o universo esteja nos unindo por alguma razão… cósmica?"
    camille "Sinto que há uma energia especial aqui. Como se fosse destino."
    $ add_affinity_points("camille", 4, "Conexão espiritual com a situação")
    hide camille gentle
    
    show nicole neutral at left
    nicole "Isso é uma falha logística gritante. Inaceitável. Mas… irreversível."
    nicole "Bem, pelo menos posso organizar tudo de forma eficiente. Vamos precisar de regras claras."
    $ add_affinity_points("nicole", 3, "Aceitação estratégica da situação")
    hide nicole neutral
    
    show larissa neutral at center
    larissa "Pelo menos tem quintal. Dá pra correr de manhã."
    larissa "E quem sabe a gente não faz uns treinos em grupo? Seria divertido!"
    $ add_affinity_points("larissa", 4, "Entusiasmo com as possibilidades esportivas")
    hide larissa neutral
    
    show huey happy at right
    huey "AAAAAA EU SEMPRE QUIS MORAR EM UMA SÉRIE DE TV!"
    huey "Isso vai ser como um anime da vida real! Vou desenhar tudo que acontecer!"
    $ add_affinity_points("huey", 5, "Pura alegria com a situação")
    hide huey happy
    
    "[nome]" "Isso vai dar muito certo. Ou muito errado."
    
    narrator "Cada uma delas reagiu de forma única à situação, mas todas pareciam... curiosas. Talvez até um pouco animadas, mesmo que algumas tentassem disfarçar."

    # Cena 2 – Organização dos Quartos
    scene bg casa_interior with dissolve
    narrator "Todos entram na casa, que tem sete quartos individuais, uma cozinha, sala ampla e dois banheiros."
    
    # Momento emocional de escolha
    call emotional_moment("room_selection", None, "Escolha que definirá a dinâmica da convivência") from _call_emotional_moment_cap3_3
    
    narrator "Cada quarto tinha sua própria personalidade, assim como cada pessoa. A escolha que eu fizesse agora definiria muito sobre como seria nossa convivência."

    menu:
        "Escolher o quarto ao lado de Samantha (Proximidade com criatividade e tecnologia)":
            $ add_shared_memory("roommate_samantha", ["samantha"], "Primeira escolha de quarto - ao lado de Samantha")
            $ add_affinity_points("samantha", 8, "Escolha de proximidade")
            jump quarto_samantha
            
        "Escolher o quarto ao lado de Nicole (Proximidade com organização e estratégia)":
            $ add_shared_memory("roommate_nicole", ["nicole"], "Primeira escolha de quarto - ao lado de Nicole")
            $ add_affinity_points("nicole", 8, "Escolha de proximidade")
            jump quarto_nicole
            
        "Escolher o quarto ao lado de Camille (Proximidade com serenidade e espiritualidade)":
            $ add_shared_memory("roommate_camille", ["camille"], "Primeira escolha de quarto - ao lado de Camille")
            $ add_affinity_points("camille", 8, "Escolha de proximidade")
            jump quarto_camille
            
        "Escolher o quarto ao lado de Huey (Proximidade com arte e entusiasmo)":
            $ add_shared_memory("roommate_huey", ["huey"], "Primeira escolha de quarto - ao lado de Huey")
            $ add_affinity_points("huey", 8, "Escolha de proximidade")
            jump quarto_huey
            
        "Escolher o quarto ao lado de Larissa (Proximidade com energia e esportes)":
            $ add_shared_memory("roommate_larissa", ["larissa"], "Primeira escolha de quarto - ao lado de Larissa")
            $ add_affinity_points("larissa", 8, "Escolha de proximidade")
            jump quarto_larissa
            
        "Escolher o quarto ao lado de Katia (Proximidade com arte e personalidade tsundere)":
            $ add_shared_memory("roommate_katia", ["katia"], "Primeira escolha de quarto - ao lado de Katia")
            $ add_affinity_points("katia", 8, "Escolha de proximidade")
            jump quarto_katia
            
        "Escolher o quarto do fundo, longe de todos (Privacidade e independência)":
            $ add_shared_memory("roommate_independence", [], "Primeira escolha de quarto - independência total")
            jump quarto_fundo

    # Cena 3 – Conflitos na Convivência
label convivencia:
    scene bg sala_casa with dissolve
    narrator "No dia seguinte, todos se reúnem na sala para definir as regras da casa."
    
    # Momento emocional de estabelecimento de regras
    call emotional_moment("house_rules_establishment", None, "Estabelecimento das regras que definirão a convivência") from _call_emotional_moment_cap3_4
    
    narrator "Era hora de estabelecer as regras que governariam nossa nova vida juntos. Cada pessoa tinha suas próprias necessidades e expectativas."

    show samantha neutral at left
    samantha "Cada um lava o que usa. Sem exceções."
    samantha "Eu trabalho até tarde nos meus projetos, então preciso que minha louça fique onde eu deixei até eu lavar."

    show nicole neutral at center
    nicole "E criamos um calendário de tarefas rotativo. Excel, compartilhado no Drive."
    nicole "Organização é fundamental para uma convivência harmoniosa. Vou criar um sistema eficiente."

    show katia neutral at right
    katia "Eu não vou limpar banheiro que outra pessoa sujou."
    katia "N-não é como se eu fosse preguiçosa ou qualquer coisa assim! É só que... cada um tem que fazer sua parte."

    show huey happy at left
    huey "Eu posso organizar tudo com base nas suas cores favoritas!"
    huey "Vai ficar lindo! Cada cômodo com sua própria paleta de cores!"

    show larissa neutral at center
    larissa "Eu só quero que ninguém toque nas minhas coisas de treino."
    larissa "E se alguém quiser treinar comigo, é só avisar! Adoraria ter companhia!"

    show camille gentle at right
    camille "A gente pode colocar um cristal de equilíbrio no centro da casa. Ajuda, juro."
    camille "A energia da casa precisa estar em harmonia para que todos se sintam bem."

    menu:
        "Propor regras rígidas (Organização e disciplina)":
            $ add_shared_memory("house_rules_strict", ["nicole", "katia"], "Estabelecimento de regras rígidas para a casa")
            $ add_affinity_points("nicole", 6, "Apoio à organização")
            $ add_affinity_points("katia", 6, "Apoio à disciplina")
            jump convivencia_rigida
            
        "Sugerir uma convivência flexível e amigável (Harmonia e compreensão)":
            $ add_shared_memory("house_rules_flexible", ["camille", "huey"], "Estabelecimento de regras flexíveis para a casa")
            $ add_affinity_points("camille", 6, "Apoio à harmonia")
            $ add_affinity_points("huey", 6, "Apoio à flexibilidade")
            jump convivencia_flexivel
            
        "Apoiar a ideia de lavar só o que usou (Responsabilidade individual)":
            $ add_shared_memory("house_rules_individual", ["samantha", "larissa"], "Estabelecimento de regras de responsabilidade individual")
            $ add_affinity_points("samantha", 6, "Apoio à responsabilidade")
            $ add_affinity_points("larissa", 6, "Apoio à independência")
            jump convivencia_lavar

    # Cena 4 – Noite de Tempestade
label noite_tempestade:
    scene bg sala_escura with dissolve
    narrator "Chove forte. A luz acaba. Todos se reúnem na sala escura com lanternas."
    
    # Momento emocional de intimidade na escuridão
    call emotional_moment("intimate_darkness", None, "Momento de intimidade e vulnerabilidade na escuridão") from _call_emotional_moment_cap3_5
    
    narrator "A escuridão tinha uma forma estranha de quebrar barreiras. No escuro, as pessoas se tornavam mais vulneráveis, mais autênticas."

    show camille gentle at left
    camille "Isso me lembra o retiro de artistas que fiz nas montanhas… só que sem as montanhas."
    camille "Há algo especial em compartilhar momentos assim. A escuridão nos une de uma forma única."

    show nicole neutral at center
    nicole "Apaguei meus backups hoje. Se meu notebook fritar, eu frito junto."
    nicole "Mas... talvez seja bom ter uma pausa forçada. Às vezes preciso ser forçada a parar."

    show samantha neutral at right
    samantha "A casa parece assombrada. Não é que eu esteja com medo… mas posso sentar aí?"
    samantha "É estranho como a escuridão pode fazer até uma casa familiar parecer diferente."

    show katia neutral at left
    katia "Eu vou ficar na cozinha. Se algo aparecer, eu taco uma frigideira."
    katia "N-não é como se eu estivesse com medo ou qualquer coisa assim! É só que... a cozinha é mais segura."

    show larissa neutral at center
    larissa "Vamos fazer uma série de exercícios para passar o tempo!"
    larissa "O movimento ajuda a dissipar a tensão. Quem quiser se juntar, é só avisar!"

    show huey happy at right
    huey "Hora da dança ritual de proteção contra espíritos!!!"
    huey "Vamos criar uma energia positiva para afastar qualquer coisa ruim!"

    menu:
        "Ficar ao lado de Samantha (Conforto e proteção)":
            $ add_shared_memory("darkness_comfort_samantha", ["samantha"], "Momento de conforto na escuridão com Samantha")
            $ add_affinity_points("samantha", 7, "Proteção na escuridão")
            jump noite_samantha
            
        "Ficar ao lado de Nicole (Apoio e compreensão)":
            $ add_shared_memory("darkness_support_nicole", ["nicole"], "Momento de apoio na escuridão com Nicole")
            $ add_affinity_points("nicole", 7, "Apoio na vulnerabilidade")
            jump noite_nicole
            
        "Ficar ao lado de Huey (Alegria e criatividade)":
            $ add_shared_memory("darkness_joy_huey", ["huey"], "Momento de alegria na escuridão com Huey")
            $ add_affinity_points("huey", 7, "Alegria na escuridão")
            jump noite_huey
            
        "Ajudar Katia na cozinha (Proteção e cuidado)":
            $ add_shared_memory("darkness_protection_katia", ["katia"], "Momento de proteção na escuridão com Katia")
            $ add_affinity_points("katia", 7, "Cuidado na vulnerabilidade")
            jump noite_katia
            
        "Ajudar Larissa a se alongar (Energia e movimento)":
            $ add_shared_memory("darkness_energy_larissa", ["larissa"], "Momento de energia na escuridão com Larissa")
            $ add_affinity_points("larissa", 7, "Energia na escuridão")
            jump noite_larissa
            
        "Participar da 'dança' com Camille (Espiritualidade e harmonia)":
            $ add_shared_memory("darkness_spirituality_camille", ["camille"], "Momento espiritual na escuridão com Camille")
            $ add_affinity_points("camille", 7, "Espiritualidade na escuridão")
            jump noite_camille

label luz_volta:
    scene bg sala_casa with dissolve
    narrator "Depois de algumas horas no escuro, a luz finalmente voltou. Um suspiro coletivo de alívio ecoou pela casa."
    
    # Momento emocional de alívio e conexão
    call emotional_moment("light_returns", None, "A luz volta, mas a conexão formada na escuridão permanece") from _call_emotional_moment_cap3_6
    
    narrator "A luz trouxe de volta a normalidade, mas algo havia mudado. As horas na escuridão criaram uma conexão especial entre todos nós."

    show samantha happy at left
    samantha "Finalmente! Achei que ia precisar usar meus óculos de visão noturna... se eu tivesse um, claro."
    samantha "Mas foi... foi bom ter vocês por perto. Obrigada por me fazerem companhia."
    hide samantha happy
    
    show nicole neutral at center
    nicole "Pelo menos agora posso voltar ao trabalho. Isso foi uma perda de tempo."
    nicole "Mas... talvez não tenha sido completamente inútil. Foi bom ter uma pausa forçada."
    hide nicole neutral
    
    show katia neutral at right
    katia "Hmpf. Eu sabia que não tinha nada de assombrado. Só um apagão comum."
    katia "N-não é como se eu tivesse gostado ou qualquer coisa assim! Mas... foi menos chato com vocês por perto."
    hide katia neutral
    
    show huey happy at left
    huey "Ahhh, mas foi divertido! Parecia um episódio de mistério!"
    huey "Vou desenhar tudo que aconteceu! Foi uma experiência incrível!"
    hide huey happy
    
    show larissa neutral at center
    larissa "Agora sim! Vou preparar algo para comer. Ficar no escuro me deu fome."
    larissa "Mas foi bom ter companhia. Obrigada por não me deixarem sozinha."
    hide larissa neutral
    
    show camille gentle at right
    camille "A luz voltou, mas a energia que compartilhamos no escuro foi especial. Obrigada por isso."
    camille "Momentos assim nos lembram do que realmente importa: as conexões que criamos."
    hide camille gentle
    # Interação personalizada com base na escolha
    if _return == "noite_samantha":
        $ points_samantha += 1    
        jump luz_samantha
    elif _return == "noite_nicole":
        $ points_nicole += 1
        jump luz_nicole
    elif _return == "noite_huey":
        $ points_huey += 1
        jump luz_huey
    elif _return == "noite_katia":
        $ points_katia += 1
        jump luz_katia
    elif _return == "noite_larissa":
        $ points_larissa += 1
        jump luz_larissa
    elif _return == "noite_camille":
        $ points_camille += 1
        jump luz_camille

label luz_samantha:
    show samantha neutral at center
    narrator "Samantha se aproximou, ainda animada com a ideia de transformar o apagão em uma aventura."
    
    samantha "Ei, foi divertido, né? Quem sabe na próxima a gente realmente jogue um RPG no escuro!"
    
    "[nome]" "Desde que você não me faça rolar dados para decidir se eu sobrevivo, tudo bem."
    
    show samantha happy at center
    samantha "Hahaha! Combinado. Mas eu vou te ensinar a criar um personagem incrível!"
    
    narrator "Samantha parecia mais animada do que nunca. Sua energia era contagiante."
    jump fim_de_semana

label luz_nicole:
    show nicole neutral at center
    narrator "Nicole suspirou aliviada, mas ainda parecia um pouco tensa."
    
    nicole "Finalmente. Agora posso voltar ao trabalho. Mas... obrigada por ficar por perto."
    
    "[nome]" "Sem problemas. Às vezes, até você precisa de uma pausa, sabia?"
    
    show nicole blush at center
    nicole "Hmpf. Talvez você esteja certo. Mas não se acostume com isso."
    
    narrator "Nicole deu um pequeno sorriso antes de voltar ao seu notebook. Foi um momento raro, mas especial."
    jump fim_de_semana

label luz_huey:
    show huey happy at center
    narrator "Huey parecia radiante, como se o apagão tivesse sido a melhor parte do dia."
    
    huey "Isso foi tão divertido! Eu até desenhei algumas ideias para uma história de mistério."
    
    "[nome]" "Você realmente consegue transformar qualquer coisa em arte, né?"
    
    show huey blush at center
    huey "Hahaha, talvez. Mas você foi uma ótima companhia. Obrigada por isso!"
    
    narrator "Huey mostrou alguns de seus desenhos, e você não pôde deixar de admirar sua criatividade."
    jump fim_de_semana

label luz_katia:
    show katia neutral at center
    narrator "Katia cruzou os braços, tentando parecer indiferente."
    
    katia "Hmpf. Não é como se eu precisasse de você lá na cozinha, mas... foi menos chato com você por perto."
    
    "[nome]" "Ah, então você admite que gostou da minha companhia?"
    
    show katia blush at center
    katia "N-Não se ache tanto! Só estou dizendo que você não foi completamente inútil."
    
    narrator "Apesar de suas palavras duras, Katia parecia satisfeita. Você até conseguiu arrancar um pequeno sorriso dela."
    jump fim_de_semana

label luz_larissa:
    show larissa neutral at center
    narrator "Larissa parecia aliviada, mas ainda cheia de energia."
    
    larissa "Agora que a luz voltou, podemos fazer um treino de verdade! Que tal?"
    
    "[nome]" "Depois de tudo isso? Acho que vou passar."
    
    show larissa happy at center
    larissa "Hahaha! Tudo bem, você merece um descanso. Mas amanhã não tem desculpa!"
    
    narrator "Larissa deu um tapinha amigável no seu ombro antes de sair. Sua energia era contagiante."
    jump fim_de_semana

label luz_camille:
    show camille gentle at center
    narrator "Camille sorriu suavemente, como se o apagão tivesse sido uma experiência especial para ela."
    
    camille "A luz voltou, mas eu gostei do que compartilhamos no escuro. Foi... único."
    
    "[nome]" "Você realmente consegue encontrar beleza em qualquer situação, não é?"
    
    show camille happy at center
    camille "Talvez. Mas acho que foi você que tornou o momento especial."
    
    narrator "Camille parecia genuinamente grata. Sua serenidade era reconfortante."
    jump fim_de_semana
    # Cena 5 – Primeiro Fim de Semana Juntos
label fim_de_semana:
    scene bg sala_casa with dissolve
    narrator "A casa decide fazer uma noite de pizzas e filmes."
    
    # Momento emocional de convivência familiar
    call emotional_moment("family_movie_night", None, "Primeira noite de filmes como uma família") from _call_emotional_moment_cap3_7
    
    narrator "Era nossa primeira noite de fim de semana juntos. Havia algo especial em compartilhar esse momento como uma família improvisada."

    show huey happy at left
    huey "Cada um escolhe um filme. No final, votação pra saber o campeão."
    huey "Vai ser como um festival de cinema caseiro! Mal posso esperar!"

    show samantha neutral at center
    samantha "Eu trouxe uns animes. Ouvi dizer que alguns aqui curtem…"
    samantha "Espero que gostem! São histórias incríveis sobre amizade e crescimento."

    show nicole neutral at right
    nicole "Dividi os títulos por gênero e duração. Está tudo nesse QR Code."
    nicole "Organização é fundamental, mesmo para momentos de lazer."

    show katia neutral at left
    katia "Só escolham algo que não tenha romance meloso."
    katia "N-não é como se eu não gostasse de romance ou qualquer coisa assim! É só que... prefiro algo mais profundo."

    show camille gentle at center
    camille "Eu trouxe um documentário sobre energia vital e conexões humanas."
    camille "Acho que vai ser perfeito para o momento que estamos vivendo."

    show larissa neutral at right
    larissa "Se tiver cena de ação e explosão emocional, já ganhou meu voto!"
    larissa "Mas estou aberta a qualquer coisa que nos una mais!"

    menu:
        "Sentar-se ao lado de Samantha (Companhia criativa)":
            $ add_shared_memory("movie_night_samantha", ["samantha"], "Primeira noite de filmes ao lado de Samantha")
            $ add_affinity_points("samantha", 8, "Companhia na noite de filmes")
            jump filme_samantha
            
        "Sentar-se ao lado de Katia (Companhia artística)":
            $ add_shared_memory("movie_night_katia", ["katia"], "Primeira noite de filmes ao lado de Katia")
            $ add_affinity_points("katia", 8, "Companhia na noite de filmes")
            jump filme_katia
            
        "Sentar-se ao lado de Nicole (Companhia estratégica)":
            $ add_shared_memory("movie_night_nicole", ["nicole"], "Primeira noite de filmes ao lado de Nicole")
            $ add_affinity_points("nicole", 8, "Companhia na noite de filmes")
            jump filme_nicole
            
        "Sentar-se ao lado de Camille (Companhia espiritual)":
            $ add_shared_memory("movie_night_camille", ["camille"], "Primeira noite de filmes ao lado de Camille")
            $ add_affinity_points("camille", 8, "Companhia na noite de filmes")
            jump filme_camille
            
        "Sentar-se ao lado de Larissa (Companhia energética)":
            $ add_shared_memory("movie_night_larissa", ["larissa"], "Primeira noite de filmes ao lado de Larissa")
            $ add_affinity_points("larissa", 8, "Companhia na noite de filmes")
            jump filme_larissa

    jump capitulo3_final