label capitulo15_nicole:
    if status_nicole == "amizade":
        scene bg sala_luxo with fade
        narrator "A festa beneficente da mãe de Nicole era o evento mais fechado da cidade."
        narrator "Eu estava lá como um mero convidado na parte de trás do salão."
        narrator "Nicole usava um vestido que custava mais do que a minha faculdade inteira. Rodeada de bajuladores, ela sorria com a boca, mas os olhos estavam vazios."
        narrator "Nós trocamos um olhar de longe. Ela abaixou a cabeça, escondendo a vergonha de estar de volta àquela gaiola de ouro que havíamos tentando destruir. Levantei minha taça e fui embora."
        jump creditos_finais
        
    elif status_nicole == "romance":
        scene bg casa_simples with fade
        narrator "Nossa casa não ficava no bairro mais caro da cidade. Era pequena, aconchegante, e cheirava a café moído na hora."
        show nicole happy at center
        narrator "Nicole estava com um avental de jardinagem, cheia de terra no rosto, rindo alto enquanto tentava plantar tomates na janela."
        mc "A CEO da fundação de apoio às artes locais não deveria estar numa reunião chique agora?"
        nicole "A diretora aprova que eu tire meia hora de folga pra matar as minhas próprias plantas."
        show nicole blush
        narrator "Eu limpei a bochecha dela com o dedo. Ela era independente, dirigia a própria vida e não devia um centavo à mãe opressora."
        nicole "Você lembra de quando eu achava que a vida sem salto alto era um inferno?"
        mc "Eu lembro que você não sabia nem ferver água."
        narrator "Ela jogou terra na minha camisa, me abraçando e rindo alto."
        nicole "Eu fervo muito bem hoje em dia."
        narrator "Ela me beijou com o frescor de quem finalmente era dona da própria liberdade. Uma vida humilde, confortável, e absolutamente perfeita ao meu lado."
        jump creditos_finais
