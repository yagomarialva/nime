label capitulo9_fogos_pre:
    scene bg campus_noite with fade
    
    narrator "O segundo dia do Festival chegou ao fim. As barracas estavam sendo desmontadas, e o cheiro de comida de rua misturava com o ar frio da noite."
    
    narrator "O evento principal, a queima de fogos, ia começar em trinta minutos."
    
    narrator "Eu estava sozinho perto da fonte do pátio central. Peguei o celular no bolso."
    
    mc "Acho que vou pro telhado do prédio de Administração ver os fogos. Mas... quem eu chamo pra ir comigo?"
    
    call screen hud_convite_fogos
    
    $ escolha_fogos = _return
    
    if escolha_fogos == "grupo":
        jump rota_amizade_fogos
    elif escolha_fogos == "larissa":
        jump rota_larissa_fogos
    elif escolha_fogos == "camille":
        jump rota_camille_fogos
    elif escolha_fogos == "samantha":
        jump rota_samantha_fogos
    elif escolha_fogos == "katia":
        jump rota_katia_fogos
    elif escolha_fogos == "nicole":
        jump rota_nicole_fogos
    elif escolha_fogos == "huey":
        jump rota_huey_fogos

label rota_amizade_fogos:
    narrator "Mandei mensagem no grupo da casa: 'Alguém afim de invadir o telhado da Adm pra ver os fogos?'"
    narrator "Cinco minutos depois, eu tinha seis garotas fazendo barulho e subindo as escadas de incêndio."
    
    scene bg ceu_estrelado with fade
    
    narrator "Nós sentamos na beirada do telhado. Katia estava reclamando da escada, Samantha estava comendo um crepe no palito, e Larissa tentava equilibrar Camille que estava quase caindo do parapeito."
    
    narrator "Os primeiros fogos estouraram."
    
    play sound "fireworks.ogg"
    
    narrator "O céu noturno se encheu de vermelho, azul e dourado. Olhei ao redor. Talvez eu não tenha escolhido uma única pessoa para focar meu coração hoje, mas ter essa família barulhenta do meu lado já era o melhor final possível para o festival."
    
    jump fim_capitulo9

label rota_larissa_fogos:
    narrator "Mandei mensagem pra Larissa. 'Quer ver os fogos do telhado da Adm? Prometo que não te desafio pra queda de braço.'"
    narrator "Ela respondeu: 'Tô subindo.'"
    
    scene bg ceu_estrelado with fade
    
    show larissa happy at center
    
    narrator "Ela chegou ofegante, com um copo de refrigerante e dois cachorros-quentes."
    
    larissa "Eu sabia que você ia esquecer de comer, então trouxe suprimentos."
    
    mc "Você é a melhor, Larissa."
    
    play sound "fireworks.ogg"
    
    narrator "Os fogos começaram. A luz colorida refletia nos olhos castanhos e no cabelo suado dela."
    
    larissa "Sabe... eu tô acostumada a carregar o peso do grupo todo. Sempre achei que romance me deixaria fraca."
    
    narrator "Ela encostou o ombro no meu."
    
    larissa "Mas sentar aqui com você... me faz sentir que eu posso abaixar a guarda de vez em quando."
    
    narrator "Eu peguei a mão dela. Dessa vez, não para uma luta de braço."
    
    mc "Pode abaixar. Eu cuido de você."
    
    jump fim_capitulo9

label rota_camille_fogos:
    narrator "Mandei mensagem pra Camille. 'As cartas prevêem a gente assistindo aos fogos juntos do telhado da Adm?'"
    narrator "Ela respondeu: 'A intuição confirmou. Subindo.'"
    
    scene bg ceu_estrelado with fade
    
    show camille neutral at center
    
    narrator "Ela apareceu silenciosamente na escada. O vento balançava o vestido esvoaçante dela."
    
    play sound "fireworks.ogg"
    
    narrator "As luzes coloridas pintaram o céu, mas Camille não olhou para cima. Ela estava olhando para mim."
    
    mc "Você tá perdendo o show."
    
    camille "Fogos de artifício são pólvora queimando. Bonitos, mas temporários. Eu estou observando algo muito mais raro."
    
    mc "O quê?"
    
    narrator "Ela deu um passo e encostou no meu peito. Senti o cheiro de sândalo e mar."
    
    camille "Aura. A sua está brilhando muito mais do que o céu agora. E eu acho que a minha está respondendo."
    
    narrator "Ela pegou minha mão e entrelaçou nossos dedos, sorrindo de forma gentil e enigmática."
    
    jump fim_capitulo9

label rota_samantha_fogos:
    narrator "Mandei mensagem pra Samantha. 'Telhado da Adm em 5 min? O ping lá é ótimo pra ver os fogos.'"
    narrator "Ela respondeu: 'Tô dando respawn no telhado agora.'"
    
    scene bg ceu_estrelado with fade
    
    show samantha happy at center
    
    narrator "Ela estava encostada na grade, com o Nintendo Switch na mão, mas a tela estava apagada."
    
    samantha "Eu pausei o jogo. Sinta-se honrado."
    
    play sound "fireworks.ogg"
    
    narrator "Os fogos estouraram em luzes azuis e verdes."
    
    mc "Lindos gráficos, não acha?"
    
    samantha "O ray tracing do mundo real é insuperável. Mas sabe..."
    
    narrator "Ela se aproximou, ficando bem colada em mim."
    
    samantha "Mesmo com o melhor hardware do mundo, jogar coop é sempre melhor do que jogar single player."
    
    mc "Isso é um convite pro Player 2?"
    
    samantha "Isso é um convite pra você não largar mais o controle."
    
    narrator "Ela segurou minha mão e encostou a cabeça no meu ombro. Assistimos aos fogos como a melhor dupla do servidor."
    
    jump fim_capitulo9

label rota_katia_fogos:
    narrator "Mandei mensagem pra Katia. 'Preciso de você no telhado da Adm. Emergência burocrática.'"
    narrator "Ela respondeu: 'Se for mentira, eu te jogo lá de cima.'"
    
    scene bg ceu_estrelado with fade
    
    show katia angry at center
    
    narrator "Ela chegou bufando e cruzando os braços."
    
    katia "Cadê a emergência? Eu tava no meio de um relatório pro Grêmio!"
    
    play sound "fireworks.ogg"
    
    narrator "O primeiro foguete estourou em um grande coração dourado no céu."
    
    mc "A emergência é que você não parou de trabalhar o festival inteiro. Pela sua saúde mental, te intimei a assistir os fogos."
    
    narrator "A expressão raivosa dela vacilou. Ela olhou para o céu colorido, e os ombros dela finalmente relaxaram."
    
    show katia blush at center
    
    katia "Seu idiota. Me arrastou pra cima só pra isso."
    
    mc "Funcionou, não funcionou?"
    
    narrator "Ela não me xingou. Em vez disso, ela deu um passo tímido e encostou o lado do braço no meu."
    
    katia "Obrigada. Mas eu ainda vou fingir que te odeio amanhã de manhã."
    
    mc "Eu não esperaria nada menos que isso."
    
    narrator "Katia escondeu o rosto vermelho virando pro céu, mas eu podia ver o sorriso sincero que ela tentava disfarçar."
    
    jump fim_capitulo9

label rota_nicole_fogos:
    narrator "Mandei mensagem pra Nicole. 'As luzes não estão tão boas aqui embaixo. Aceita camarote VIP no telhado da Adm?'"
    narrator "Ela respondeu: 'Com o meu look, eu mereço o lugar mais alto do campus.'"
    
    scene bg ceu_estrelado with fade
    
    show nicole happy at center
    
    narrator "Ela chegou impecável, ajeitando o casaco fino que esvoaçava com o vento frio."
    
    nicole "Nada mal para um camarote, assistente geral."
    
    play sound "fireworks.ogg"
    
    narrator "Os fogos começaram a iluminar o rosto perfeito dela. Ela estava maravilhosa."
    
    mc "Você desfilou incrível hoje."
    
    nicole "Saber brilhar é fácil. Difícil é encontrar alguém que brilhe do seu lado sem tentar apagar a sua luz."
    
    narrator "Ela se aproximou, envolvendo meu braço com as duas mãos e encostando a cabeça no meu ombro."
    
    nicole "Você é o acessório perfeito pra essa noite. Talvez pro resto do semestre também."
    
    mc "Eu me sinto lisonjeado, majestade."
    
    narrator "Ela riu baixo, e ficamos ali, dividindo a vista e o calor no meio da noite fria."
    
    jump fim_capitulo9

label rota_huey_fogos:
    narrator "Mandei mensagem pra Huey. 'A trigonometria dos fogos é melhor vista do telhado da Adm. Quer calcular a parábola comigo?'"
    narrator "Ela respondeu: 'A altitude aumenta a precisão visual. Aceito.'"
    
    scene bg ceu_estrelado with fade
    
    show huey neutral at center
    
    narrator "Ela chegou em silêncio e parou exatamente do meu lado."
    
    play sound "fireworks.ogg"
    
    narrator "Explosões perfeitamente simétricas coloriram o céu noturno."
    
    huey "Combustão controlada de nitrato de potássio, enxofre e carvão. Fascinante."
    
    mc "Eu prefiro focar nas cores, mas a química também é legal."
    
    narrator "Huey virou o rosto para mim. Os olhos vermelhos dela refletiam o brilho dos fogos de forma hipnótica."
    
    huey "Sabe o que é mais fascinante que a combustão?"
    
    mc "O quê?"
    
    huey "A variabilidade das minhas reações cardiovasculares quando você está próximo."
    
    narrator "Ela pegou a minha mão, com cuidado, e apertou de leve."
    
    huey "Meu sistema operacional costumava rejeitar interações prolongadas. Com você, eu quero recalibrar meus protocolos. Definitivamente."
    
    narrator "Eu sorri e apertei a mão dela de volta. A engenharia dos nossos sentimentos estava finalmente se encaixando."
    
    jump fim_capitulo9

label fim_capitulo9:
    scene black with fade
    
    narrator "Fim do Capítulo 9."
    
    call end_of_chapter_validation("capitulo10") from _call_end_of_chapter_validation_5
