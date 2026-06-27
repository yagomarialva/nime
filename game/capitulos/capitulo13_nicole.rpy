label capitulo13_nicole:
    if status_nicole == "ruina":
        scene bg rua_noite with fade
        narrator "Nicole não sabia como ser pobre. E o orgulho dela a impediu de aceitar a derrota."
        narrator "Ela tentou dormir em hotéis que não podia pagar, foi expulsa, e teve um colapso nervoso nas ruas de madrugada."
        narrator "Quando tentei ajudá-la na rua, ela gritou histericamente que a culpa era minha por encobri-la. Os seguranças particulares da mãe dela chegaram logo em seguida e a jogaram num carro preto."
        narrator "Eu nunca mais vi a Nicole depois daquela noite de terror."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Nicole){/b}"
        return
        
    elif status_nicole == "amizade":
        scene bg flat_nicole with fade
        narrator "Fui visitá-la no luxuoso flat de cobertura."
        show nicole neutral at center
        narrator "Nicole estava com as roupas de grife novamente, segurando o cartão black recém-desbloqueado."
        nicole "A mamãe aceitou meu pedido de desculpas. Eu disse que você e as garotas da Rua Aurora me desencaminharam."
        mc "Você mentiu de novo para ela..."
        nicole "Foi o que garantiu a minha herança."
        narrator "Ela não conseguia olhar nos meus olhos por pura vergonha de sua covardia. Continuamos colegas distantes, mas o romance e o respeito mútuo estavam arruinados."
        call end_of_chapter_validation("capitulo14")
        
    elif status_nicole == "romance":
        scene bg cafe with fade
        narrator "O cheiro de grãos torrados e leite vaporizado enchia a cafeteria perto do campus."
        show nicole happy at center
        narrator "Nicole usava o avental verde da cafeteria. Ela estava limpando o balcão, rindo com os colegas de trabalho."
        narrator "Ela terminou o turno e correu até a minha mesa."
        show nicole blush
        nicole "Olha isso. Meu primeiro pagamento. Com dinheiro que eu mesma ganhei com minhas mãos."
        mc "Você foi incrível. E a sua mãe? Ela tentou te forçar de volta?"
        nicole "Ela ligou. E eu disse que estava processando-a por tentar trancar a minha matrícula de forma abusiva. Ela recuou."
        narrator "Ela tirou um pacotinho do bolso e colocou na minha frente."
        nicole "Eu gastei um terço do meu pagamento nisso. Abre."
        narrator "Era um pingente de prata simples. Nada comparado às joias que ela costumava usar, mas infinitamente mais valioso."
        nicole "Para lembrar de quem apostou em mim quando eu não valia um centavo."
        narrator "Nós dividimos um café barato e um beijo com sabor de liberdade total."
        call end_of_chapter_validation("capitulo14")
