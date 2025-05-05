label evento_individual_camille:
    scene bg jardim_universidade with fade
    show camille neutral at center

    narrator "Camille me convidou para uma sessão de meditação no jardim da universidade. O lugar era tranquilo, com o som suave do vento e o canto dos pássaros ao fundo."

    camille "Fico feliz que você tenha vindo. Às vezes, precisamos de um momento para nos desconectar do caos e nos reconectar com nós mesmos."

    narrator "Camille parecia em paz, sentada em uma posição confortável no gramado. Sua presença era calmante, e eu sabia que seria uma experiência única."

    menu:
        "Perguntar como ela começou a meditar":
            $ points_camille += 1
            camille "Comecei quando percebi que precisava de algo para equilibrar minha mente e meu coração. A meditação me trouxe clareza."
            narrator "Camille falou com serenidade, compartilhando como a prática mudou sua vida."
            "[nome]" "Isso é incrível, Camille. Parece que a meditação realmente te ajudou a encontrar equilíbrio. Você acha que qualquer pessoa pode começar?"
            camille "Com certeza. Não importa onde você esteja na vida, sempre há espaço para começar algo novo."

        "Comentar sobre a tranquilidade do jardim":
            $ points_camille += 1
            camille "Sim, este lugar tem uma energia especial. É perfeito para encontrar paz interior."
            narrator "Camille sorriu levemente, parecendo feliz por compartilhar o momento comigo."
            "[nome]" "Eu nunca tinha reparado como este lugar é tão calmo. Você vem aqui com frequência?"
            camille "Sempre que posso. É um dos meus refúgios favoritos para recarregar as energias."

        "Sugerir que vocês comecem a meditação":
            $ points_camille += 1
            camille "Claro. Vamos começar. Apenas feche os olhos e respire profundamente."
            narrator "Camille guiou a meditação com uma voz suave, criando um ambiente de calma e introspecção."
            "[nome]" "Obrigado por me guiar, Camille. Acho que nunca teria conseguido relaxar assim sozinho."
            camille "Fico feliz em ajudar. Às vezes, tudo o que precisamos é de um empurrãozinho para começar."

    # Cena 1: Meditação guiada
    scene bg jardim_universidade with dissolve
    show camille neutral at center
    narrator "Camille começou a guiar a meditação, pedindo para que eu me concentrasse na minha respiração e deixasse os pensamentos fluírem."

    camille "Inspire profundamente... e expire lentamente. Sinta o ar entrando e saindo, conectando você ao momento presente."

    menu:
        "Seguir as instruções e relaxar completamente":
            $ points_camille += 1
            narrator "Segui as instruções de Camille e senti meu corpo relaxar completamente. Era como se o tempo tivesse parado."
            "[nome]" "Isso foi incrível, Camille. Eu nunca me senti tão relaxado antes."
            camille "Fico feliz que tenha funcionado para você. A prática pode realmente transformar como nos sentimos."

        "Perguntar como a meditação pode ajudar no dia a dia":
            $ points_camille += 1
            camille "A meditação nos ensina a estar presentes e a lidar com os desafios com mais clareza e calma."
            narrator "Camille explicou com paciência, mostrando sua paixão por compartilhar os benefícios da prática."
            "[nome]" "Faz sentido. Acho que preciso aprender a desacelerar e estar mais presente."
            camille "É um ótimo começo. Pequenos passos podem fazer uma grande diferença."

        "Comentar sobre a dificuldade de se concentrar no início":
            $ points_camille += 1
            camille "É normal. A prática leva tempo, mas com paciência, você encontrará sua própria forma de meditar."
            narrator "Camille sorriu, encorajando-me a continuar tentando."
            "[nome]" "Obrigado pela paciência, Camille. Acho que vou tentar praticar mais vezes."
            camille "Isso é ótimo. Lembre-se de que cada tentativa é um progresso."

    # Cena 2: Reflexão após a meditação
    scene bg jardim_universidade with dissolve
    show camille neutral at center
    narrator "Depois de algum tempo, Camille abriu os olhos e sorriu levemente, parecendo completamente em paz."

    camille "Como você se sente? Espero que tenha conseguido encontrar um pouco de tranquilidade."

    menu:
        "Dizer que se sente mais relaxado e em paz":
            $ points_camille += 1
            camille "Fico feliz em ouvir isso. É incrível o que alguns minutos de silêncio podem fazer por nós."
            narrator "Camille parecia satisfeita por ter ajudado a criar um momento de calma."
            "[nome]" "Eu realmente precisava disso. Obrigado por compartilhar esse momento comigo."
            camille "Foi um prazer. Espero que você leve essa calma com você."

        "Perguntar como ela mantém essa calma no dia a dia":
            $ points_camille += 1
            camille "Nem sempre é fácil, mas eu tento lembrar que cada momento é uma oportunidade de recomeçar."
            narrator "Camille falou com sabedoria, mostrando sua abordagem equilibrada para a vida."
            "[nome]" "Isso é inspirador. Acho que vou tentar aplicar isso na minha rotina."
            camille "Fico feliz em ouvir isso. Pequenas mudanças podem fazer uma grande diferença."

        "Agradecer por compartilhar a experiência":
            $ points_camille += 1
            camille "Não precisa agradecer. Fico feliz em compartilhar algo que me trouxe tanto bem-estar."
            narrator "Camille parecia genuinamente contente por ter compartilhado a prática comigo."
            "[nome]" "Você realmente tem um dom para trazer calma às pessoas. Obrigado por isso."
            camille "Obrigada. É bom saber que posso ajudar."

    # Cena 3: Finalizando o encontro
    scene bg jardim_universidade with dissolve
    show camille neutral at center
    narrator "Depois de algum tempo, Camille se levantou e olhou para o céu, respirando profundamente."

    camille "Obrigada por passar esse tempo comigo. Espero que você leve um pouco dessa calma com você."

    menu:
        "Agradecer a Camille pela experiência relaxante":
            $ points_camille += 1
            camille "Foi um prazer. Espero que possamos fazer isso novamente algum dia."
            "[nome]" "Com certeza. Foi uma experiência incrível."

        "Elogiar sua sabedoria e tranquilidade":
            $ points_camille += 1
            camille "Obrigada. Tento viver de acordo com o que acredito, e é bom saber que isso inspira os outros."
            "[nome]" "Você realmente é uma inspiração, Camille. Obrigado por compartilhar isso comigo."

        "Sugerir que vocês façam outra sessão de meditação no futuro":
            $ points_camille += 1
            camille "Adoraria. Sempre há algo novo para explorar na jornada interior."
            "[nome]" "Então está combinado. Mal posso esperar pela próxima vez."

    hide camille
    narrator "Passei uma tarde tranquila e introspectiva com Camille, aprendendo mais sobre sua visão de mundo e sua prática de meditação. Foi uma experiência que certamente ficará na memória."
    jump capitulo2_conclusao