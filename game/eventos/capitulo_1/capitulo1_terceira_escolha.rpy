# === TERCEIRA ESCOLHA - A FESTA DA FUMAÇA E DO RUÍDO ===
label capitulo1_terceira_escolha:
    play music party fadein 2.0
    
    scene bg campus_evening with fade
    
    narrator "O sol despencou no horizonte sem qualquer aviso decoroso. O céu da Solária sangrava em um tom alaranjado doente."
    narrator "A noite engoliu o campus com a agressividade habitual das noites universitárias."
    
    scene bg campus_night with fade
    narrator "Ouvi o grave pulsante muito antes de ver o pavilhão do centro estudantil. O ar cheirava a cerveja quente, suor de ansiedade e fumaça artificial."
    narrator "A infame festa de recepção dos calouros. Um rito de passagem onde todos tentam provar que não estão desesperados por aprovação."
    
    scene bg festa_boas_vindas with dissolve
    narrator "A música estava tão alta que meus pensamentos se transformaram em estática."
    
    # As garotas isoladas e desconfortáveis
    narrator "Abri caminho pela multidão de corpos amontoados. Foi quando percebi: não existia roda. Não existia o grupo perfeito."
    narrator "Todas aquelas figuras fragmentadas, as garotas que encontrei ao longo da semana, estavam dolorosamente espalhadas pelos cantos da festa, como detritos deixados na areia após a maré recuar."
    
    mc "Miseráveis e teimosas demais para simplesmente irem embora."
    
    # === INTERAÇÃO COM NICOLE ===
    narrator "Encostada na mesa de bebidas, longe das caixas de som, encontrei Nicole. Ela mexia distraidamente em um copo plástico, o nariz sutilmente enrugado."
    
    show nicole neutral at center
    
    nicole "O volume excedeu os limites regulamentares há trinta minutos. As vibrações daquele alto-falante estão provocando uma microfissura no gesso."
    
    menu:
        "Tentar ser otimista":
            $ points_nicole += 1
            mc "É uma festa de recepção. Acho que o objetivo estrutural é surdez coletiva, não?"
            nicole "Hum. Racionalização interessante da auto-sabotagem humana."
            
        "Concordar silenciosamente":
            $ points_nicole += 3
            narrator "Fiquei ao lado dela, encarando a mesma fissura imaginária no gesso. O silêncio compartilhado era muito melhor que gritar frivolidades."
            nicole "Obrigada por não perguntar se estou me divertindo."
            
    hide nicole with dissolve
    
    # === INTERAÇÃO COM KATIA ===
    narrator "Perto da saída de emergência, longe dos estroboscópios estúpidos, uma figura usava o celular como escudo luminoso."
    
    show katia sad at center
    
    katia "Aquela iluminação estroboscópica na pista de dança é amadora. A taxa de quadros visuais cria uma narrativa visual barata que dá náuseas."
    
    menu:
        "Discutir cinema":
            $ points_katia += 1
            mc "Se o diretor iluminador é ruim, a gente critica a película?"
            katia "Sim... Quer dizer, não seja estúpido. Isto nem de longe é uma película."
            
        "Reconhecer seu isolamento":
            $ points_katia += 3
            mc "Você está praticamente com a mão na maçaneta da saída e não vai embora. Críticos gostam de sofrer pela arte?"
            katia "Hmpf. Não critique as minhas escolhas masoquistas."
            narrator "Katia apertou os braços em torno do próprio corpo, mas relaxou levemente os ombros pela primeira vez na noite."
            
    hide katia with dissolve
    
    # === INTERAÇÃO COM LARISSA ===
    narrator "Encontrei Larissa no corredor lateral. Ela não parava de girar um copo vazio de plástico. Ao invés da explosão da quadra, ela parecia uma fera enjaulada em um zoológico."
    
    show larissa sad at center
    
    larissa "Sabe o esgotamento aeróbico? Aquele momento que falta oxigênio porque tem gente demais sugando o mesmo ar... É assim que me sinto agora."
    
    menu:
        "Puxá-la para dançar":
            $ points_larissa += 1
            mc "Gastar energia física resolve tudo, não? Vá se mexer."
            larissa "Eu... eu não sei como me mexer nesse tipo de caos, pra falar a verdade."
            
        "Entender a claustrofobia":
            $ points_larissa += 3
            mc "Excesso de estímulos, falta de direcionamento. Você costuma correr em pistas desenhadas, não em labirintos de bêbados."
            larissa "Isso... é exatamente isso."
            narrator "Larissa apertou o copo plástico até esmagado e, por um instante, seu sorriso hiperativo desapareceu."
            
    hide larissa with dissolve
    
    # === INTERAÇÃO COM HUEY ===
    narrator "Huey estava sentada na escada para o segundo andar. Ela traçava na calça jeans a fumaça projetada pelas luzes, os olhos vazios e distantes."
    
    show huey neutral at center
    
    huey "Há muitas cores primárias aqui. E tão sufocante. Cadê os tons pastéis? Cadê a respiração das linhas...?"
    
    menu:
        "Questionar o olhar dela":
            $ points_huey += 1
            mc "Sempre vendo arte, até no barulho?"
            huey "Dói olhar pra isso tudo. Não é um quadro bem planejado."
            
        "Sentar de forma silenciosa e densa":
            $ points_huey += 3
            narrator "Sentei no degrau abaixo do dela. O grave da música fez meu peito tremer, mas ficar ali parou uma fração do barulho mental."
            huey "Obrigada. Às vezes o mundo é muito vívido. Você ajuda a diluir um pouco das tintas."
            
    hide huey with dissolve
    
    # === INTERAÇÃO COM SAMANTHA ===
    narrator "Atrás do totem de som quebrado, no escuro, encontrei a pior das vítimas."
    
    show samantha sad at center
    
    samantha "M-minha stamina esgotou. A bateria social zerou no lobby. Eu preciso da tela de save."
    
    menu:
        "Tratar como piada de jogador":
            $ points_samantha += 1
            mc "Vamos usar um poção de vigor, mestre de RPG?"
            samantha "Isso quebra minha imersão... não funciona. Socorro..."
            
        "Oferecer o cobertor do silêncio":
            $ points_samantha += 3
            mc "O volume das notificações foi pro mudo."
            narrator "Fiquei parado entre a caixa de som e ela, criando uma parede humana improvisada. Samantha bufou exausta, encostando a testa contra os próprios joelhos."
            samantha "O-obrigada... Apenas fique aqui."
            
    hide samantha with dissolve
    
    # === INTERAÇÃO COM CAMILLE ===
    narrator "Camille estava parada na sacada, os olhos perdidos na poluição luminosa da universidade que apagava as estrelas."
    
    show camille sad at center
    
    camille "Pessoas demais projetando desejos vazios e vazamentos emocionais ao mesmo tempo... A estática é ensurdecedora."
    
    menu:
        "Zombar levemente com lógica cósmica":
            $ points_camille += 1
            mc "É só música eletrônica barata e hormônios, Camille. Não é uma fusão estelar."
            camille "O vazio ecoa mais alto que as pulsações cósmicas, às vezes..."
            
        "Ancorar a gravidade dela":
            $ points_camille += 3
            mc "Não tente abrigar toda essa estática. Feche a porta."
            camille "Eu ainda não sei como... mas sua gravidade é estranhamente silenciosa no meio disso tudo."
            narrator "Por um instante infimo, a feição celestial dela caiu, mostrando apenas uma garota sufocada por falsas expectativas."
            
    hide camille with dissolve
    
    # === MOMENTO DE DECISÃO ===
    scene bg festa_boas_vindas with fade
    
    narrator "O relógio passava absurdamente devagar. Eu não suportava mais o oxigênio reciclável daquela sala."
    narrator "Olhei em volta. Algumas daquelas pessoas isoladas pareciam a um passo de despencar do precipício invisível que construíram para si mesmas."
    narrator "Eu não ia salvar ninguém. Mas talvez eu pudesse fabricar um pretexto para que um de nós pudesse fugir sentindo menos culpa."
    
    menu:
        "Nicole estava prestes a queimar uma planilha de desespero. Vou acompanhá-la.":
            $ add_shared_memory("evening_walk_nicole", ["nicole"], "Ofereceu uma desculpa silenciosa para escapar do caos e preservar a estrutura dela.")
            $ points_nicole += 5
            jump capitulo1_caminhada_nicole
            
        "Katia ia arrancar o olho do técnico de luz. É melhor eu tirá-la daqui.":
            $ add_shared_memory("evening_walk_katia", ["katia"], "Salvação relutante e silenciosa sob as luzes estroboscópicas que a incomodavam.")
            $ points_katia += 5
            jump capitulo1_caminhada_katia
            
        "Se ficasse mais, Larissa ia bater a cabeça numa parede.":
            $ add_shared_memory("evening_walk_larissa", ["larissa"], "Guiei a energia exausta dela para longe do labirinto social da festa.")
            $ points_larissa += 5
            jump capitulo1_caminhada_larissa
            
        "A fumaça ia esmagar as aquarelas mentais da Huey.":
            $ add_shared_memory("evening_walk_huey", ["huey"], "Providenciou uma moldura vazia de silêncio para aliviar a exaustão sensorial dela.")
            $ points_huey += 5
            jump capitulo1_caminhada_huey
            
        "A bateria social de Samantha zerou. Ela precisa extrair.":
            $ add_shared_memory("evening_walk_samantha", ["samantha"], "Agir como um NPC condutor para salvá-la do esgotamento no mundo real.")
            $ points_samantha += 5
            jump capitulo1_caminhada_samantha
            
        "A estática ia desabar o cosmos da Camille.":
            $ add_shared_memory("evening_walk_camille", ["camille"], "Serviu como âncora gravitacional antes que o excesso de caos emocional a rompesse.")
            $ points_camille += 5
            jump capitulo1_caminhada_camille
