# === AULA COM O PROFESSOR WENDELL - TODOS SE CONHECEM ===
label capitulo1_aula_professor_wendell:
    scene bg auditorium with fade
    
    narrator "Após todas as explorações do dia, recebi uma mensagem do Professor Wendell convidando para uma aula especial sobre 'Conexões Humanas e Desenvolvimento Pessoal'."
    narrator "Era uma matéria eletiva que ele ministrava para alunos interessados em crescimento pessoal e relacionamentos."
    
    narrator "Quando entrei na sala, fiquei surpreso ao ver que todas as pessoas que havia conhecido nos últimos dias estavam presentes."
    narrator "Era como se o destino tivesse nos reunido naquele momento especial."
    
    show professor_wendell at center
    professor_wendell "Bem-vindos, queridos alunos! Hoje temos uma aula muito especial sobre conexões humanas."
    professor_wendell "E vejo que temos alguns rostos novos aqui... que maravilhoso!"
    
    hide professor_wendell
    narrator "O Professor Wendell começou a apresentar cada pessoa, criando um ambiente acolhedor onde todos puderam se conhecer formalmente."
    
    # Apresentação das personagens
    show nicole neutral at left
    nicole "Olá, sou Nicole. Estudo comunicação estratégica e análise de dados comportamentais."
    nicole "É um prazer conhecer todos vocês formalmente."
    hide nicole with dissolve
    
    show camille gentle at right
    camille "Oi, sou Camille. Estudo conexões energéticas e práticas de mindfulness."
    camille "É reconfortante estar em um ambiente onde todos valorizam o crescimento pessoal."
    hide camille with dissolve
    
    show katia neutral at left
    katia "Sou Katia, estudo cinema e análise de narrativas."
    katia "N-não é como se eu me importasse, mas vocês parecem ter perspectivas... interessantes sobre comunicação."
    hide katia with dissolve
    
    show huey gentle at right
    huey "Oi, sou Huey. Estudo artes visuais e expressão criativa."
    huey "É inspirador estar rodeada de pessoas tão diferentes e interessantes."
    hide huey with dissolve
    
    show samantha happy at left
    samantha "O-oi, sou Samantha... estudo jogos e estratégia criativa."
    samantha "É bom conhecer todos vocês... sempre valorizo diferentes perspectivas sobre criatividade."
    hide samantha with dissolve
    
    show larissa happy at right
    larissa "Eaí, sou Larissa! Estudo educação física e estratégia esportiva."
    larissa "Que legal conhecer todo mundo! Adoro trabalhar em equipe e superar desafios juntos!"
    hide larissa with dissolve
    
    show professor_wendell at center
    professor_wendell "Maravilhoso! Vejo que temos um grupo muito diverso e talentoso aqui."
    professor_wendell "Hoje vamos falar sobre como as conexões humanas se formam e como podemos aprender uns com os outros."
    
    narrator "A aula foi fascinante. O Professor Wendell falou sobre como pessoas diferentes podem se complementar perfeitamente."
    narrator "Ele destacou como cada um de nós traz uma perspectiva única que pode enriquecer o grupo todo."
    
    professor_wendell "Lembrem-se, queridos alunos: as melhores conexões acontecem quando abrimos nossos corações para aprender com pessoas diferentes de nós."
    professor_wendell "Cada um de vocês tem algo especial para oferecer ao mundo e uns aos outros."
    
    hide professor_wendell
    narrator "Após a aula, todos ficaram conversando, compartilhando suas experiências dos últimos dias."
    narrator "Era incrível ver como, mesmo tendo personalidades tão diferentes, todos conseguiam se conectar de forma genuína."
    
    narrator "Foi um momento especial onde finalmente todos se conheceram, criando laços que prometiam durar muito tempo."
    
    # Memória compartilhada especial
    $ add_shared_memory("first_group_meeting", ["nicole", "camille", "katia", "huey", "samantha", "larissa"], "O primeiro encontro oficial de todo o grupo na aula do Professor Wendell")
    
    jump capitulo1_terceira_escolha
