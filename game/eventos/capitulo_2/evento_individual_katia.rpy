label evento_individual_katia:
    scene bg cafe_artistic with fade
    show katia neutral at center

    narrator "Katia me convidou para tomar um café em um lugar que ela descreveu como 'não tão ruim assim'. Era um café artístico, com quadros nas paredes e uma atmosfera tranquila."

    katia "Não pense que eu te chamei porque queria sua companhia ou algo assim. Só achei que você poderia aprender algo aqui."

    narrator "Katia desviou o olhar, tentando esconder o leve rubor em seu rosto. Era típico dela agir assim, mas eu sabia que ela estava feliz por estar aqui."

    menu:
        "Perguntar por que ela escolheu este lugar":
            $ points_katia += 1
            katia "Eu gosto do ambiente... Não que eu me importe tanto assim, mas é um bom lugar para pensar."
            narrator "Katia parecia tentar disfarçar o quanto gostava do lugar, mas era evidente que ela se sentia confortável ali."

        "Comentar sobre o estilo artístico do café":
            $ points_katia += 1
            katia "É... até que não é tão ruim. Eles têm bom gosto, pelo menos."
            narrator "Katia parecia satisfeita com o comentário, mesmo que tentasse esconder."

        "Elogiar o bom gosto dela por escolher o lugar":
            $ points_katia += 1
            katia "Hmph, não é como se eu precisasse do seu elogio ou algo assim... Mas obrigada, eu acho."
            narrator "Katia desviou o olhar, mas era evidente que o elogio a agradou."

    # Cena 1: Conversa sobre arte
    scene bg cafe_artistic with dissolve
    show katia neutral at center
    narrator "Enquanto tomávamos café, começamos a conversar sobre arte e cultura. Katia parecia mais relaxada, embora ainda mantivesse sua atitude reservada."

    katia "A arte é uma forma de expressão que vai além das palavras. É por isso que eu gosto dela... Não que eu precise explicar isso para você."

    menu:
        "Perguntar qual é o estilo de arte favorito dela":
            $ points_katia += 1
            katia "Eu gosto de algo que desafie a mente, como surrealismo ou simbolismo. Algo que faça você pensar."
            narrator "Katia falou com entusiasmo, embora tentasse manter sua postura indiferente."

        "Discutir como a arte pode refletir emoções profundas":
            $ points_katia += 1
            katia "Sim, é isso que a torna tão poderosa. Ela pode transmitir o que palavras não conseguem."
            narrator "Katia parecia impressionada com minha perspectiva, embora tentasse não demonstrar."

        "Sugerir que vocês visitem uma galeria juntos no futuro":
            $ points_katia += 1
            katia "Hmph, talvez. Não que eu esteja ansiosa ou algo assim, mas pode ser interessante."
            narrator "Katia tentou disfarçar, mas era evidente que a ideia a agradou."

    # Cena 2: Reflexão pessoal
    scene bg cafe_artistic with dissolve
    show katia neutral at center
    narrator "Depois de algum tempo, a conversa tomou um tom mais pessoal. Katia parecia disposta a compartilhar um pouco mais sobre si mesma."

    katia "Às vezes, eu me pergunto se as pessoas realmente entendem o que eu quero dizer. É por isso que eu prefiro deixar a arte falar por mim."

    menu:
        "Dizer que a autenticidade dela é inspiradora":
            $ points_katia += 1
            katia "Hmph, não é como se eu precisasse ouvir isso... Mas obrigada, eu acho."
            narrator "Katia parecia tocada pelo comentário, embora tentasse esconder."

        "Perguntar como ela começou a se interessar por arte":
            $ points_katia += 1
            katia "Desde pequena. Sempre gostei de desenhar e criar coisas. É algo que sempre fez parte de mim."
            narrator "Katia falou com paixão sobre sua jornada artística, mostrando um lado mais vulnerável."

        "Sugerir que ela use sua arte para se expressar mais":
            $ points_katia += 1
            katia "Talvez você tenha razão. Pode ser uma forma de mostrar quem eu realmente sou."
            narrator "Katia parecia considerar seriamente a sugestão, algo raro para ela."

    # Cena 3: Finalizando o encontro
    scene bg cafe_artistic with dissolve
    show katia neutral at center
    narrator "Depois de algum tempo, Katia olhou para o relógio e suspirou levemente."

    katia "Acho que já está na hora de ir. Não foi tão ruim passar esse tempo com você... Não que eu esteja dizendo que gostei ou algo assim."

    menu:
        "Agradecer a Katia pelo tempo juntos":
            $ points_katia += 1
            katia "Hmph, não precisa agradecer. Foi... interessante, eu acho."

        "Elogiar a paixão dela por arte":
            $ points_katia += 1
            katia "Obrigada... Não que eu precise ouvir isso, mas é bom saber que alguém entende."

        "Sugerir que vocês façam isso novamente no futuro":
            $ points_katia += 1
            katia "Talvez. Não que eu esteja ansiosa ou algo assim, mas pode ser interessante."

    hide katia
    narrator "Passei uma tarde reflexiva e interessante com Katia, aprendendo mais sobre sua visão de mundo e sua paixão por arte. Foi uma experiência que certamente ficará na memória."
    jump capitulo2_final