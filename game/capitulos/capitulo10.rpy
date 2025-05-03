label capitulo10:
    scene bg republica_vazia with fade
    narrator "É a última semana do semestre. A república começa a esvaziar. Caixas se acumulam. Paredes perdem os quadros e bilhetes. Cada passo soa como uma despedida não dita."

    show nicole neutral at left
    nicole "Estamos seguindo o cronograma, mas emocionalmente... estamos atrasados."

    show katia neutral at center
    katia "Esse plano de fundo vai render um curta sobre fim de ciclos."

    show camille gentle at right
    camille "O cheiro da casa vai mudar... Mas a vibração ficará."

    show larissa happy at left
    larissa "Quero fazer agachamento emocional e físico com todo mundo antes do fim."

    show samantha happy at center
    samantha "A gente devia ter salvado mais momentos com clipes de voz…"

    show huey gentle at right
    huey "Última arte antes da parede ser pintada de branco. Adeus, memória viva."

    # Segue para os eventos de despedida automaticamente
    jump capitulo10_samantha

label capitulo10_samantha:
    show samantha happy at center
    narrator "Você ajuda Samantha a salvar os dados dos jogos antigos no computador."
    samantha "Esses jogos são como memórias vivas. Cada escolha, cada vitória... é como se a gente pudesse reviver tudo."
    protagonist "E agora você pode guardar tudo isso pra sempre."
    samantha "Obrigada por me ajudar. Você é o melhor parceiro de guilda que eu poderia pedir."
    jump capitulo10_katia

label capitulo10_katia:
    show katia neutral at center
    narrator "Você ajuda Katia a embalar livros enquanto discutem finais de filmes."
    katia "Sabe o que eu odeio? Finais abertos. Mas... às vezes, eles são os mais reais."
    protagonist "Talvez porque a vida nunca tem um ponto final definitivo."
    katia "Hmpf. Filosófico demais pra mim. Mas... obrigada por estar aqui."
    jump capitulo10_huey

label capitulo10_huey:
    show huey gentle at center
    narrator "Você ajuda Huey a pintar a parede com uma última arte antes de ser apagada."
    huey "Cada pincelada é como uma memória. Mesmo que desapareça, ela ainda existiu."
    protagonist "E você capturou tudo isso de um jeito único."
    huey "Obrigado por pintar isso comigo. Você é uma inspiração."
    jump capitulo10_camille

label capitulo10_camille:
    show camille gentle at center
    narrator "Você queima incensos com Camille enquanto refletem sobre mudanças."
    camille "O cheiro muda, mas a energia permanece. É como se a casa guardasse tudo o que vivemos."
    protagonist "E agora, ela vai guardar isso pra sempre."
    camille "Obrigada por estar aqui. Você trouxe equilíbrio pra tudo isso."
    jump capitulo10_nicole

label capitulo10_nicole:
    show nicole neutral at center
    narrator "Você ajuda Nicole a criar etiquetas organizadas para as caixas."
    nicole "Organizar tudo isso é como organizar as memórias. Cada coisa no seu lugar."
    protagonist "E você faz isso melhor do que ninguém."
    nicole "Obrigada por me ajudar. Você é... eficiente. E especial."
    jump capitulo10_larissa

label capitulo10_larissa:
    show larissa happy at center
    narrator "Você treina com Larissa entre as caixas, transformando a despedida em algo físico."
    larissa "Treinar é minha forma de lidar com tudo. Mas... isso aqui é mais difícil do que eu pensei."
    protagonist "Você é forte, Larissa. E não precisa carregar tudo sozinha."
    larissa "Obrigada por estar aqui. Você é um parceiro incrível."
    jump capitulo10_evento_final

label capitulo10_evento_final:
    scene bg republica_noite with fade
    narrator "Na véspera do fim, cada morador sai para resolver sua vida. Você fica sozinho na casa… até que uma porta se abre."

    # Determina a personagem de maior afinidade
    if points_samantha >= 6 and points_samantha == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_samantha
    elif points_nicole >= 6 and points_nicole == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_nicole
    elif points_huey >= 6 and points_huey == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_huey
    elif points_camille >= 6 and points_camille == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_camille
    elif points_larissa >= 6 and points_larissa == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_larissa
    elif points_katia >= 6 and points_katia == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_katia
    else:
        jump capitulo10_despedida

# Finais individuais (exemplo com Samantha)
label capitulo10_final_samantha:
    show samantha happy at center
    narrator "Samantha aparece com dois controles nas mãos."
    samantha "É a última noite… e a gente ainda não zerou aquele jogo. Quer... terminar comigo?"
    narrator "Vocês jogam juntos, rindo, até a tela final."
    samantha "Você... foi meu player 2 favorito."
    if romance_samantha:
        samantha "No próximo jogo, eu quero começar contigo desde o prólogo."
    else:
        samantha "Mesmo em partidas separadas… sempre vou torcer pelo seu sucesso crítico."
    jump capitulo10_despedida

# Repita o padrão acima para Nicole, Huey, Camille, Larissa e Katia.

label capitulo10_despedida:
    scene bg republica_saida with fade
    narrator "Todos estão prontos. A van os espera. A casa está vazia. Um último olhar para trás."

    show nicole neutral at left
    nicole "Nunca mais vou achar um grupo tão caótico… e tão meu."

    show camille gentle at center
    camille "Essa casa... vibrou como família."

    show katia neutral at right
    katia "Alguém anota isso. É final de temporada."

    show larissa happy at left
    larissa "Bora. Ou vou começar a chorar."

    show samantha happy at center
    samantha "Missão: manter contato. Recompensa: corações inteiros."

    show huey gentle at right
    huey "Posso pintar essa despedida? Só se alguém prometer voltar."

    narrator "E assim, a história da república Rua Aurora chega ao fim. Mas entre as risadas, os silêncios e os olhares… algo foi construído. Algo que nem o tempo pode apagar."

    return