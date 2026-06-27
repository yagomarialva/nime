label capitulo15_larissa:
    if status_larissa == "amizade":
        scene bg sala_estar with fade
        narrator "Era domingo à tarde. Eu estava no sofá do meu apartamento, assistindo à final do campeonato de vôlei na TV."
        narrator "A câmera focou no banco de reservas do time campeão."
        narrator "Lá estava Larissa. Vestida num terninho esportivo, séria, anotando táticas numa prancheta."
        narrator "Peguei meu celular e mandei uma mensagem: 'Parabéns pela vitória, Coach.' Dois minutos depois, ela respondeu: 'Valeu, player. A gente se vê no Natal, se eu não tiver viajando.'"
        narrator "Sorri para a tela da TV. Estávamos bem. Sucesso, distância e uma amizade morna, sem arrependimentos."
        jump creditos_finais
        
    elif status_larissa == "romance":
        scene bg quadra with fade
        narrator "O apito final estourou meus tímpanos no meio da arquibancada."
        narrator "O time nacional acabava de vencer o maior torneio da década."
        narrator "A mídia cercou a técnica principal do time imediatamente. Larissa estava linda, suada de nervosismo e com os olhos brilhando."
        narrator "Repórter: 'Treinadora! Qual foi a tática para essa virada impossível no último set?!'"
        show larissa happy at center
        larissa "A tática é sempre a mesma: ter a pessoa certa fora de quadra te lembrando por que você joga."
        narrator "Ela afastou os microfones educadamente, pulou a placa de publicidade e correu na minha direção."
        show larissa blush
        narrator "Ela pulou a grade da arquibancada e me puxou pela gola."
        mc "Você sabe que você tá ao vivo em rede nacional, né?"
        larissa "E daí? Eles achavam que eu ia sair mancando pro resto da vida. Olha pra mim agora."
        narrator "Ela me beijou com força, levantando o troféu de prata que uma jogadora havia colocado nas mãos dela, espremendo o metal brilhante contra o meu peito."
        larissa "Nós somos campeões. E hoje à noite, a taça dorme na nossa cama."
        jump creditos_finais
