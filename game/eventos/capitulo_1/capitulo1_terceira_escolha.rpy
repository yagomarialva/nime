label capitulo1_terceira_escolha:
    play music campus_ambient fadein 2.0
    
    scene bg cozinha_escura with fade
    
    narrator "O primeiro jantar oficial na Rua Aurora, 57. A ideia era minha, uma tentativa fútil de pacificar o ambiente após a reunião com Wendell."
    
    narrator "A cozinha cheirava a macarrão instantâneo e tensão."
    
    show nicole sad at right
    
    nicole "Se nós três dividirmos a conta de luz baseado na metragem quadrada dos quartos que ocupamos, é o método mais justo."
    
    narrator "Nicole empurrou uma planilha impressa pelo balcão. Ela sequer tocou no prato de comida."
    
    show katia neutral at left
    
    katia "Metragem quadrada? Eu durmo no menor quarto e a porta não fecha. Você quer cobrar impostos sobre o ar que eu respiro também, ditadora?"
    
    nicole "Estou tentando impedir que nós sejamos despejados! Você acha que o mundo funciona à base de ironia e rebeldia? As contas chegam, Katia!"
    
    katia "O mundo funciona à base de privilégios. Alguns de nós estão aqui para sobreviver, não para brincar de casinha perfeitinha no The Sims."
    
    narrator "A faísca foi instantânea. Nicole recuou como se tivesse levado um tapa. A máscara de perfeição dela rachou por um milissegundo."
    
    narrator "O silêncio engoliu a cozinha. Ambas olharam para mim, esperando que eu tomasse partido. A panela de pressão estava prestes a estourar."
    
    menu:
        "Ficar do lado de Nicole. A casa precisa de regras.":
            $ points_nicole += 5
            $ points_katia -= 5
            mc "Katia, ela tem razão. A gente não vai durar um mês sem planejamento financeiro."
            narrator "Nicole soltou a respiração que estava segurando. Ela não sorriu, mas o olhar dela era de pura gratidão."
            nicole "Obrigada por entender o mínimo de responsabilidade adulta."
            katia "Ótimo. O contador e a síndica se encontraram. Façam bom proveito da burocracia."
            narrator "Katia pegou seu prato e subiu as escadas batendo o pé."
            
        "Ficar do lado de Katia. As regras da Nicole são absurdas.":
            $ points_katia += 5
            $ points_nicole -= 5
            mc "Nicole, você tá sufocando todo mundo. Metragem quadrada? Relaxa, a gente divide em três partes iguais e pronto."
            narrator "Katia deu um sorriso de canto, um misto de surpresa e vitória."
            katia "Viu? A voz da razão não usa planilhas de Excel."
            narrator "A expressão de Nicole fechou completamente. Ela pegou a planilha com as mãos tremendo levemente."
            nicole "Certo. Quando não tivermos dinheiro para pagar a energia, não venham chorar na minha porta."
            narrator "Ela saiu da cozinha como uma tempestade gelada."
            
        "Tentar mediar a situação. (Gastar 20 Energia)":
            if store.player_stats["energy"] >= 20:
                $ update_player_stat("energy", -20)
                $ points_katia += 2
                $ points_nicole += 2
                mc "As duas parem com isso! Nicole, a divisão será em três partes iguais. Katia, em troca, nós seguimos o cronograma de limpeza da sala de estar para compensar o quarto pequeno."
                narrator "Eu coloquei a mão sobre a planilha, parando a discussão antes que ficasse pior. Me custou toda a energia social que me restava."
                narrator "As duas se entreolharam. O ódio mútuo ainda estava lá, mas o acordo era lógico demais para ser refutado."
                nicole "...Aceitável. Vou revisar o cronograma."
                katia "...Desde que eu não tenha que lavar o banheiro."
            else:
                mc "Eu ia tentar mediar isso... mas minha cabeça tá explodindo de cansaço. Só parem de gritar."
                narrator "Ambas me ignoraram. A discussão continuou até que a exaustão venceu e todas foram para seus quartos, odiando umas às outras um pouco mais."
    
    hide nicole
    hide katia
    
    narrator "O jantar acabou com a comida fria e as portas batendo. Ninguém disse boa noite."
    
    return
