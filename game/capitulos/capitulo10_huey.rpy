label capitulo10_huey:
    scene bg biblioteca with dissolve
    
    narrator "A prova de Estrutura de Dados e Análise Algorítmica era o terror da faculdade. Mas Huey geralmente sorria diante dela."
    narrator "Não hoje."
    
    show huey sad at center
    
    narrator "Ela estava parada na frente da lousa do grupo de estudos, encarando um quadro cheio de equações apagadas pela metade."
    
    mc "Huey? A prova é daqui a dois dias. Seus resumos estatísticos sumiram da mesa."
    
    huey "Meu processamento analítico foi comprometido."
    
    mc "O quê? Como assim?"
    
    narrator "Ela virou pra mim. Os olhos, geralmente afiados e focados, estavam desfocados e marejados."
    
    huey "A equação preditiva para a prova é simples. O problema é a variável externa que eu introduzi no meu ecossistema diário."
    
    mc "Que variável?"
    
    huey "Você."
    
    narrator "Dei um passo para trás, surpreso."
    
    huey "Meu coração bate em uma frequência de 120bpm quando você está na sala. Isso reduz a oxigenação do meu córtex pré-frontal. Eu não consigo focar nas fórmulas porque meu cérebro insiste em recalcular os cenários de interação com você."
    
    mc "Eu tô... atrapalhando seus estudos?"
    
    huey "Sim. E o mais ilógico de tudo..."
    
    narrator "Ela andou até mim, parando a centímetros de distância."
    
    huey "É que eu não quero consertar esse erro de sistema. Eu quero manter a variável."
    
    mc "Huey..."
    
    narrator "Segurei a mão dela. Estava fria. Ela estava genuinamente em pânico com os próprios sentimentos."
    
    mc "Sentimentos não são algoritmos, Huey. Eles não precisam ser resolvidos ou quantificados. Você só precisa aceitá-os."
    
    mc "Nós vamos sentar agora, e eu vou segurar a sua mão enquanto você resolve a primeira equação daquela lousa. E eu prometo que, quando o seu coração estabilizar, você vai ver que eu não sou um bug. Eu sou uma feature."
    
    narrator "O primeiro sorriso genuíno da noite apareceu no rosto dela."
    
    huey "Uma feature. Eu aprecio a analogia de software."
    
    $ init_simon_game()
label loop_simon_huey:
    call screen minigame_simon
    
    if _return == "lose":
        huey "Meus BPMs voltaram a subir. O estresse cardiovascular é inevitável."
        mc "Respira. Olha pra sequência de novo. Nós vamos abaixar isso."
        $ init_simon_game()
        jump loop_simon_huey
        
    scene black with fade
    
    narrator "Ela estudou com a minha mão sobre a dela. O ritmo cardíaco dela se acalmou, e a genialidade voltou a fluir livremente."
    narrator "Na prova, ela tirou 10. A maior nota da turma."
    
    scene bg sala_jantar with dissolve
    
    show huey gentle at center
    
    narrator "Quando ela chegou em casa, não disse nada. Apenas andou até mim no sofá, tirou os óculos e sentou no meu colo."
    
    mc "Isso é novo."
    
    huey "Atualização de firmware. Contato físico foi classificado como prioridade de Nível 1."
    
    narrator "E então ela me beijou, um beijo curioso no início, mas que rapidamente encontrou um ritmo perfeito."
    
    huey "A variável foi integrada com sucesso. Obrigado, player."
    
    call end_of_chapter_validation("capitulo11")
