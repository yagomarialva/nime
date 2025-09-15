# === EVENTO HUEY E CAMILLE ===
# Artista vs. Espiritual

label evento_huey_camille:
    $ points_huey += 1
    scene bg galeria_arte with dissolve
    show huey gentle at left
    show camille gentle at right

    narrator "Huey me convidou para visitar uma exposição de arte contemporânea na galeria do centro. O ambiente estava silencioso e contemplativo."
    narrator "Camille apareceu de surpresa, carregando um caderno de anotações e com um ar sereno."

    huey "Obrigada por vir! Esta exposição é realmente especial... cada obra conta uma história única."
    huey "Preciso de sua opinião sobre algo importante. Estou trabalhando em uma série sobre conexões humanas."

    camille "Nossa, que sincronia! Eu também estava pensando sobre conexões... mas de uma perspectiva mais energética."
    camille "Senti uma energia muito forte vindo daqui... como se as obras estivessem vibrando com algo especial."

    huey "Energia? Camille, você também sente isso? É como se cada obra tivesse sua própria aura, sua própria emoção..."
    huey "Quando estou aqui, sinto que posso capturar não apenas o visual, mas também a essência que cada peça emana."

    camille "Huey, você entende exatamente o que eu sinto! A arte é sobre essa conexão profunda, sobre sentir além do que vemos."
    camille "Cada obra carrega a energia de quem a criou... e quando você se conecta com ela, consegue sentir essa essência."

    huey "Exato! É como se cada pincelada, cada cor, cada textura... tudo fosse uma forma de canalizar emoções e energias."
    huey "Quando pinto, sinto que estou traduzindo algo que existe além do mundo físico."

    camille "Huey, você descreveu perfeitamente! É exatamente isso que sinto quando medito ou quando me conecto com a natureza."
    camille "É sobre sentir a energia que permeia tudo... e a arte é uma forma linda de expressar essa conexão."

    narrator "Senti que havia uma conexão genuína entre elas. Ambas compartilhavam a mesma sensibilidade para perceber e expressar as energias sutis do mundo, apenas com linguagens diferentes."

    scene bg galeria_arte with dissolve
    menu:
        "Discutir como a arte captura emoções":
            $ points_huey += 3
            narrator "Concordei com a perspectiva de Huey sobre arte e emoção."
            huey "Exato! A arte é sobre traduzir o que sentimos em algo tangível!"
            huey "Cada cor, cada pincelada... tudo é uma forma de expressar emoções que não conseguimos dizer com palavras!"
            camille "Huey, você disse exatamente o que eu sinto! É como se a arte fosse uma linguagem universal das emoções!"

        "Explorar a energia que permeia a arte":
            $ points_camille += 3
            narrator "Concordei com a perspectiva de Camille sobre energia e arte."
            camille "Exato! Cada obra carrega a energia de quem a criou!"
            camille "Quando você se conecta com uma obra, consegue sentir a essência que o artista colocou nela!"
            huey "Nossa, Camille, você descreveu perfeitamente! É exatamente isso que sinto quando olho para uma pintura!"

        "Compartilhar experiências de conexão":
            $ points_huey += 2
            $ points_camille += 2
            narrator "Sugeri que compartilhassem suas experiências de conexão com a arte."
            huey "Que ideia linda! É fascinante como cada uma de nós sente e expressa essas conexões!"
            camille "Sim! E é incrível como chegamos ao mesmo lugar por caminhos diferentes!"
            huey "É como se fôssemos duas artistas da mesma alma, apenas usando linguagens diferentes!"

    # Cena adicional 2 – Workshop prático
    hide huey
    hide camille
    scene bg galeria_arte with dissolve
    show huey gentle at left
    show camille gentle at right

    narrator "Decidimos colocar a teoria em prática. Huey propôs um workshop de pintura para explorar juntas a conexão entre arte e energia."

    huey "Vamos pintar! Vou te mostrar como sinto a energia fluir através das cores e formas!"
    huey "Camille, você vai ver como é diferente quando você se conecta com a essência criativa!"

    camille "Que ideia maravilhosa! E antes de começar, vamos meditar um pouco? Para alinhar nossa energia criativa?"
    camille "A arte flui melhor quando estamos conectadas com nossa essência mais profunda."

    huey "Meditar? Camille, que ideia linda! É exatamente isso que faço antes de pintar!"
    huey "Sinto que preciso me conectar com algo maior antes de colocar a tinta na tela..."

    camille "Huey, você entende perfeitamente! A arte começa com essa conexão interior, com a energia que você canaliza."
    camille "Quando você está alinhada com sua essência, a obra ganha vida própria!"

    narrator "O workshop começou, e foi fascinante ver como Huey e Camille complementavam perfeitamente suas abordagens sensíveis."

    huey "Nossa... quando me conecto assim, sinto que as cores escolhem a si mesmas!"
    huey "É como se a obra já existisse em algum lugar e eu apenas a estivesse revelando..."

    camille "Exato! Huey, você está canalizando a energia criativa perfeitamente!"
    camille "Sinto a energia fluindo através de você... é lindo de ver!"

    narrator "Huey e Camille trabalhavam em perfeita sintonia, cada uma contribuindo com sua sensibilidade única para a criação."

    menu:
        "Focar na conexão emocional com a arte":
            $ points_huey += 3
            narrator "Concordei com a abordagem emocional de Huey."
            huey "Exato! A arte é sobre conectar-se com as emoções mais profundas!"
            huey "Cada pincelada é um sentimento, cada cor é uma emoção traduzida em forma!"
            camille "Huey, você expressou perfeitamente! É exatamente isso que sinto quando me conecto com a energia criativa!"

        "Explorar a energia espiritual na criação":
            $ points_camille += 3
            narrator "Concordei com a abordagem espiritual de Camille."
            camille "Exato! A arte é sobre canalizar a energia universal!"
            camille "Quando você se conecta com essa energia, a obra ganha vida própria!"
            huey "Nossa, Camille, você descreveu exatamente o que sinto quando estou no meu estado criativo!"

        "Combinar sensibilidade artística e espiritual":
            $ points_huey += 2
            $ points_camille += 2
            narrator "Sugeri que combinassem ambas as abordagens sensíveis."
            huey "Que ideia linda! Podemos explorar como a sensibilidade artística e espiritual se complementam!"
            camille "Sim! É fascinante como chegamos ao mesmo lugar por caminhos diferentes!"
            huey "É como se fôssemos duas almas gêmeas da criatividade!"

    # Cena adicional 3 – Reflexão
    hide huey
    hide camille
    scene bg galeria_arte with dissolve
    show huey gentle at left
    show camille gentle at right

    narrator "Após o workshop, decidimos refletir sobre a conexão especial que havíamos descoberto."

    huey "Nossa... nunca pensei que encontraria alguém que sentisse a arte da mesma forma que eu."
    huey "Camille, você realmente entende o que é canalizar emoções através da criação!"

    camille "Huey, eu que fico impressionada! Sua sensibilidade para capturar a essência das coisas..."
    camille "É como se você conseguisse traduzir em cores e formas o que eu sinto apenas como energia."

    huey "Camille, você descreveu perfeitamente! É exatamente isso que sinto quando pinto!"
    huey "É como se estivéssemos falando a mesma língua, apenas usando meios diferentes!"

    camille "Sim! E é incrível como chegamos ao mesmo lugar por caminhos diferentes."
    camille "Você através da arte, eu através da meditação... mas ambas sentimos a mesma conexão profunda."

    narrator "Era como se tivessem encontrado uma alma gêmea sensível. Ambas compartilhavam a mesma capacidade de perceber e expressar as energias sutis do mundo."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    huey "Camille... obrigada por me mostrar que há mais na arte do que apenas técnica."
    huey "Você me ensinou que a energia espiritual pode ser tão poderosa quanto a expressão artística."

    camille "Huey... obrigada por me mostrar que a arte pode ser tão profunda!"
    camille "Você me ensinou que cada pincelada pode carregar a mesma energia que sinto na meditação!"

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas almas da mesma essência - ambas sensíveis e conectadas com as energias sutis do mundo."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração em arte espiritual":
            $ points_huey += 2
            $ points_camille += 2
            narrator "Sugeri que Huey e Camille colaborassem em um projeto de arte espiritual."
            huey "Que ideia maravilhosa! Podemos criar um workshop que combine meditação e pintura!"
            camille "Nossa, que lindo! Eu posso guiar as práticas de conexão energética, e você pode ensinar a expressar isso através da arte!"
            huey "Exato! Meditação para conectar, arte para expressar! Seria uma experiência completa!"

        "Perguntar sobre suas práticas criativas":
            $ points_huey += 1
            $ points_camille += 1
            narrator "Perguntei sobre as práticas criativas de cada uma."
            huey "Bem... sempre medito antes de pintar, para me conectar com a energia criativa."
            huey "E você, Camille? Como você canaliza essa energia que sente?"
            camille "Eu medito e sinto a energia fluir... mas nunca pensei em expressá-la através da arte como você faz!"

        "Refletir sobre a conexão especial":
            $ points_huey += 1
            $ points_camille += 1
            narrator "Sugeri que refletissem sobre a conexão especial que haviam descoberto."
            huey "Nunca pensei que encontraria alguém que sentisse a arte da mesma forma que eu..."
            camille "E eu nunca imaginei que encontraria alguém que canalizasse energia através da arte como você!"
            huey "É como se fôssemos duas almas gêmeas da sensibilidade... N-não é como se eu estivesse sendo sentimental ou qualquer coisa assim!"

    # Memória compartilhada especial
    $ add_shared_memory("sensitive_souls_connection", ["huey", "camille"], "O momento em que descobrimos nossa conexão especial como almas sensíveis e criativas")

    hide huey
    hide camille
    scene bg galeria_arte with dissolve

    narrator "O sol começava a se pôr sobre a galeria, mas a conversa continuava inspiradora."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Huey e Camille haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."

    jump capitulo1_terceira_escolha
