label capitulo13_harem:
    if status_harem == "ruina":
        scene bg rua_aurora with fade
        narrator "O conselho de ética julgou apenas um culpado pelos problemas da casa: Eu."
        narrator "Fui expulso imediatamente da universidade sob acusações falsas de organizar orgias no campus."
        narrator "Quando cheguei em casa para pegar minhas coisas, Samantha estava na porta. Katia, Nicole, Camille, Larissa e Huey observavam do andar de cima."
        narrator "Elas jogaram minhas caixas na calçada e trancaram a porta. A covardia que eu mostrei no tribunal destruiu a confiança delas."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Harém){/b}"
        return
        
    elif status_harem == "amizade":
        scene bg rua_aurora with fade
        narrator "Nós fomos derrotados pelo conselho. O edital foi cancelado."
        narrator "A fraternidade de elite assumiu a posse da casa em 30 dias. Nós passamos aquele mês empacotando silenciosamente a vida incrível que tínhamos construído."
        narrator "Larissa foi para o alojamento de atletas. Nicole voltou ao luxo da família. As outras se espalharam por repúblicas apertadas."
        narrator "O grupo no WhatsApp foi a única coisa que restou, e logo morreu. A magia do harém e da união desapareceu com a demolição emocional da nossa casa."
        call end_of_chapter_validation("capitulo14")
        
    elif status_harem == "romance":
        scene bg casa_interior with fade
        narrator "O conselho de ética não pôde negar os números. Nossas notas excelentes e as vitórias do semestre provaram que a casa na Rua Aurora não era um problema, mas uma incubadora de talentos excêntricos."
        narrator "O Edital foi renovado, e a fraternidade arquivou o processo com o rabo entre as pernas."
        
        show katia happy at left
        show nicole happy at right
        narrator "Katia estourou uma garrafa de espumante barato. Nicole não reclamou da marca, apenas pegou uma taça."
        
        hide katia
        hide nicole
        show larissa happy at left
        show samantha happy at right
        narrator "Larissa e Samantha me puxaram para o meio da sala, ligando as luzes estroboscópicas."
        
        hide larissa
        hide samantha
        show camille blush at left
        show huey blush at right
        narrator "Camille espalhava fumaça de sálvia doce enquanto Huey pintava freneticamente a cena em uma tela no canto da sala."
        
        narrator "Uma por uma, elas me deram um beijo ao som da música alta, sem ciúmes, sem limites, apenas com o amor compartilhado que nos uniu na loucura e na paz."
        narrator "Nós sobrevivemos como um ecossistema perfeito. A nossa família."
        call end_of_chapter_validation("capitulo14")
