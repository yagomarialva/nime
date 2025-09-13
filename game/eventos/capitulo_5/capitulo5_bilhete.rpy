label cena3_bilhete_anonimo:
    scene bg quarto_protagonista with dissolve
    narrator "No dia seguinte, você encontra um bilhete deixado na sua escrivaninha. Ele é escrito à mão, com traços misteriosos."

    show bilhete at center
    narrator "📝 Texto do bilhete:"
    narrator "“Você me faz sentir estranhamente confortável. Não sei como lidar com isso ainda, mas queria que soubesse. — de alguém que ainda está descobrindo o que sente.”"
    hide bilhete

    narrator "Você sente uma mistura de curiosidade e surpresa. Quem teria escrito isso? E por quê?"

    # Determina quem escreveu o bilhete com base na afinidade
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ autora_bilhete = max(afinidades, key=afinidades.get)

    # Verifica se a afinidade da autora é maior que 5
    if afinidades[autora_bilhete] <= 5:
        narrator "O bilhete permanece um mistério, já que ninguém parece ter afinidade suficiente para escrevê-lo."
        jump cena4_tarde_estudo

    menu:
        "Tentar identificar pela letra":
            jump identificar_bilhete
        "Ignorar e guardar o bilhete":
            jump guardar_bilhete
        "Falar com todas na sala comum":
            jump confrontar_sala_comum

label identificar_bilhete:
    narrator "Você decide tentar identificar quem escreveu o bilhete, analisando a caligrafia e pensando em quem poderia ter deixado algo assim."

    if autora_bilhete == "camille":
        $ points_camille += 1
        narrator "Você percebe que a caligrafia combina com a de Camille. Ela parece ter escrito o bilhete, mas não quer admitir diretamente."
        camille "Ah... você encontrou o bilhete. Bem, eu só queria que você soubesse como me sinto."
        narrator "Camille sorriu timidamente, mas parecia aliviada por você ter descoberto."
    elif autora_bilhete == "samantha":
        $ points_samantha += 1
        narrator "Você percebe que a caligrafia combina com a de Samantha. Ela tenta disfarçar, mas acaba admitindo."
        samantha "Ah, droga... você descobriu. Eu só queria dizer algo, mas não sabia como."
        narrator "Samantha riu nervosamente, mas parecia feliz que você não a julgou."
    elif autora_bilhete == "nicole":
        $ points_nicole += 1
        narrator "Você percebe que a caligrafia combina com a de Nicole. Ela tenta manter a compostura, mas acaba admitindo."
        nicole "Eu... achei que seria mais fácil escrever do que falar. Não esperava que você fosse descobrir tão rápido."
        narrator "Nicole desviou o olhar, mas havia um leve sorriso em seu rosto."
    elif autora_bilhete == "katia":
        $ points_katia += 1
        narrator "Você percebe que a caligrafia combina com a de Katia. Ela tenta negar, mas acaba admitindo com um tom defensivo."
        katia "Tá, fui eu. Mas não significa nada, ok? Só... esquece isso."
        narrator "Apesar de suas palavras, Katia parecia aliviada por você ter descoberto."
    elif autora_bilhete == "huey":
        $ points_huey += 1
        narrator "Você percebe que a caligrafia combina com a de Huey. Ela sorri timidamente e admite."
        huey "Eu... só queria expressar algo que sinto. Não sabia como dizer isso em palavras."
        narrator "Huey parecia aliviada por você ter entendido o gesto."
    elif autora_bilhete == "larissa":
        $ points_larissa += 1
        narrator "Você percebe que a caligrafia combina com a de Larissa. Ela ri e admite sem rodeios."
        larissa "Haha, fui eu! Achei que seria divertido te deixar curioso."
        narrator "Larissa parecia animada e despreocupada com sua descoberta."
    jump cena4_tarde_estudo

label guardar_bilhete:
    narrator "Você decide guardar o bilhete sem tentar descobrir quem o escreveu. Talvez seja melhor deixar o mistério no ar."
    narrator "O bilhete permanece guardado em sua gaveta, como um lembrete de que alguém está pensando em você."
    jump cena4_tarde_estudo


label confrontar_sala_comum:
    scene bg sala_comum with dissolve
    narrator "Você decide falar com todos na sala comum, perguntando diretamente sobre o bilhete."
    show samantha happy at left
    show nicole neutral at center
    show larissa happy at right
    
    hide samantha
    hide nicole
    hide larissa
    
    show katia neutral at left
    show huey neutral at center
    show camille gentle at right

    "[nome]" "Alguém aqui deixou um bilhete na minha escrivaninha? Só queria saber quem foi."

    if autora_bilhete == "camille":
        $ points_camille += 1
        camille "Ah... você encontrou o bilhete. Bem, eu só queria que você soubesse como me sinto."
        narrator "Camille desviou o olhar, mas um sorriso tímido surgiu em seus lábios."
        "[nome]" "Eu gostei. Foi... especial."
        camille "Fico feliz que tenha entendido. Às vezes, as palavras escritas falam mais do que as ditas."
        narrator "Camille se aproximou levemente, e por um breve momento, seus ombros se encostaram. O silêncio entre vocês parecia cheio de significado."

    elif autora_bilhete == "samantha":
        $ points_samantha += 1
        samantha "Ah, droga... você descobriu. Eu só queria dizer algo, mas não sabia como."
        narrator "Samantha riu nervosamente, mas seus olhos brilhavam com uma mistura de alívio e diversão."
        "[nome]" "Foi uma surpresa boa. Você tem um jeito único de se expressar."
        samantha "Bem, eu sou única, né? Mas... obrigada por não achar estranho."
        narrator "Samantha deu um leve empurrão no seu ombro, rindo. O toque foi breve, mas deixou uma sensação calorosa."

    elif autora_bilhete == "nicole":
        $ points_nicole += 1
        nicole "Eu... achei que seria mais fácil escrever do que falar. Não esperava que você fosse descobrir tão rápido."
        narrator "Nicole desviou o olhar, mas havia um leve sorriso em seu rosto."
        "[nome]" "Eu achei muito sincero. Obrigado por compartilhar isso comigo."
        nicole "Bem, não se acostume. Eu não sou boa com essas coisas."
        narrator "Apesar de suas palavras, Nicole se aproximou um pouco mais, e seus olhares se cruzaram por um instante mais longo do que o normal."

    elif autora_bilhete == "katia":
        $ points_katia += 1
        katia "Tá, fui eu. Mas não significa nada, ok? Só... esquece isso."
        narrator "Apesar de suas palavras, Katia parecia aliviada por você ter descoberto. Um leve rubor surgiu em suas bochechas."
        "[nome]" "Eu não vou esquecer. Foi importante para mim."
        katia "Hmpf. Você é impossível."
        narrator "Katia cruzou os braços, mas não se afastou. Pelo contrário, ela ficou ao seu lado, e por um breve momento, seus olhares se encontraram."

    elif autora_bilhete == "huey":
        $ points_huey += 1
        huey "Eu... só queria expressar algo que sinto. Não sabia como dizer isso em palavras."
        narrator "Huey sorriu timidamente, e seus olhos brilhavam com emoção."
        "[nome]" "Você conseguiu. Foi bonito. Obrigado por confiar em mim."
        huey "Eu fico feliz que tenha entendido. Isso significa muito para mim."
        narrator "Huey se inclinou levemente para mais perto, e por um breve momento, seus dedos quase se tocaram. O gesto foi sutil, mas cheio de significado."

    elif autora_bilhete == "larissa":
        $ points_larissa += 1
        larissa "Haha, fui eu! Achei que seria divertido te deixar curioso. Mas parece que você levou a sério."
        narrator "Larissa riu, mas havia um brilho diferente em seus olhos, algo mais sincero."
        "[nome]" "Eu levei a sério porque foi especial. Obrigado por isso."
        larissa "Ah, não precisa agradecer. Mas... fico feliz que tenha gostado."
        narrator "Larissa deu um leve toque no seu braço, e por um instante, vocês trocaram um olhar que parecia dizer mais do que palavras poderiam."

    narrator "A sala ficou em silêncio por um momento, mas o gesto da autora do bilhete deixou uma marca em você. Era um pequeno passo, mas cheio de significado."
    jump cena4_tarde_estudo
