# === EVENTO BIBLIOTECA: NICOLE E CAMILLE ===
# Tema: O medo do imprevisível (Planilhas vs. Cristais)

label evento_nicole_camille:
    # Pequeno ganho de afinidade inicial
    $ points_nicole += 1
    $ points_camille += 1
    
    scene bg library with dissolve
    
    narrator "O ar na biblioteca estava denso de mofo de papel envelhecido e poeira suspensa na luz pálida da tarde. Estática de sussurros compunha o ambiente falso de silêncio."

    show nicole angry at left
    
    narrator "Na mesa de mogno do fundo, uma sinfonia ansiosa. Nicole batia a tampa da caneta esferográfica sobre uma folha lotada de vetores tridimensionais complexos."
    
    nicole "A probabilidade do erro estrutural aumenta a cada nova variante humana introduzida. Nada obedece à equação. Tudo quebra."
    
    show camille neutral at right
    
    narrator "A cadeira metálica arrastou bruscamente quando Camille forçou passagem pelo corredor de mesas, carregando incensos apagados em uma das mãos."
    narrator "Ela sentou sem cumprimentar, os olhos opacos voltados para as folhas agitadas de Nicole."
    
    camille "Variantes humanas quebram equações porque se recusam a fluir na malha cósmica. Sua tensão magnética está encurvando o papel, sabia?"
    
    narrator "Nicole parou a caneta suspensa no ar. Seu rosto contraiu como quem provou vinagre."
    
    nicole "Tensão magnética não deforma papel em níveis atômicos, a menos que eu fosse um gerador de nêutrons. Você e suas desculpas pseudocientíficas para não resolver problemas empíricos é que me dão náusea."
    
    camille "Seus problemas 'empíricos' são caixinhas desesperadas. Você tenta quantificar a dor de existir como se ela fosse previsível, só porque você tem muito medo."
    
    narrator "Camille pegou e soltou bruscamente um pedaço de quartzo lapidado pesado em cima da planilha de cálculos principal."
    
    nicole "Tira a pedra polida da mesa. Você está distorcendo meu campo de visão empírico e contaminando o material de trabalho."
    
    camille "Tentei ancorar a poeira psíquica. Mas a estática da sua ansiedade é uma barreira de vidro blindado."
    
    mc "Acho que as duas tentam aterrissar o colapso nervoso de si mesmas com métodos que não funcionaram."
    
    narrator "As pálpebras de Camille cederam e piscaram por choque. O maxilar de Nicole trancou ao ouvir minha voz vazia na discussão ininterrupta das duas."
    narrator "Eram duas frentes lutando em vão contra o medo crônico do imponderável: Controle matemático versus Aceitação cósmica abstrata. Ambas falhas."
    
    menu:
        "Proteger as raízes lógicas (Nicole)":
            $ points_nicole += 2
            mc "Pelo menos a fobia da Nicole gera um dado que podemos ler. Cristal no topo de papel só pesa as folhas."
            nicole "Obrigada. Funcionalidade supera fuga espiritual."
            camille "Meros dados estéreis são túmulos pra sua mente, Nicole. Mas divirtam-se medindo cadáveres lógicos."
            
        "Ancorar no escudo espiritual (Camille)":
            $ points_camille += 2
            mc "As respostas lógicas parecem estar destruindo a estrutura mental dela mais rápido que uma distração com quartzo."
            camille "A matemática sempre encontra o teto limitante."
            nicole "Isso é só ignorância defensiva para quem nunca soube lidar com equações frias da vida."
            
        "Apatia para ambas as fugas":
            $ points_nicole += 1
            $ points_camille += 1
            mc "A estática daqui só prova que nenhuma das duas obteve sucesso em acalmar a si mesmas. Parem de ditar regras e só se acostumem com a bagunça."
            narrator "O silêncio doeu. A pedra de quartzo ficou repousando em cima do gráfico enquanto ambas desistiram de tentar provar o contrário da afirmação violenta de desistência."
    
    narrator "Camille se reacomodou, olhando pela janela para a fachada envernizada. Nicole agarrou outra folha inteiramente limpa e forçou outro número que não faria diferença no universo."
    narrator "Permanceram perto, apenas como satélites desorientados sem rota, exilando a dor em seus próprios métodos quebrados."
    
    # Memória compartilhada renomeada
    $ add_shared_memory("science_vs_magic", ["nicole", "camille"], "O momento onde o desespero por controle empírico esbarrou na ilusão do conforto místico.")

    return