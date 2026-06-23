# Minigame do Pincel (Comédia)
screen minigame_pincel():
    modal True
    zorder 200
    
    default clicks_necessarios = 20
    default clicks_atuais = 0
    default tempo_restante = 5.0
    
    timer 0.1 repeat True action If(tempo_restante > 0, SetScreenVariable("tempo_restante", tempo_restante - 0.1), Return(False))
    
    add Solid("#000000cc")
    
    vbox:
        xalign 0.5
        yalign 0.1
        text "Arranque o pincel da mão do Professor Wendell!" size 40 color "#ffffff" bold True
        text "Puxões: [clicks_atuais] / [clicks_necessarios]" size 30 color "#ffcc00"
        text "Tempo: [tempo_restante:.1f]s" size 30 color "#ff5555"
        
    imagebutton:
        idle "gui/button/choice_idle_background.png"
        hover "gui/button/choice_hover_background.png"
        xalign 0.5
        yalign 0.5
        action If(clicks_atuais < clicks_necessarios, SetScreenVariable("clicks_atuais", clicks_atuais + 1), Return(True))
        
    if clicks_atuais >= clicks_necessarios:
        timer 0.1 action Return(True)

label capitulo8_inspecao:
    scene bg casa_interior with fade
    
    narrator "Chegou a tarde de sexta-feira. O prazo final."
    narrator "Nossas roupas estavam manchadas de tinta branca e marfim. Nossas mãos tinham calos, e o cansaço era visível nos nossos olhos."
    
    narrator "Mas a Rua Aurora, 57 nunca esteve tão linda."
    
    show professor_wendell neutral at center
    
    narrator "O Professor Wendell entrou pela porta da frente. Ele cheirou o ar, esperando mofo e fumaça."
    
    professor_wendell "Cheiro de... lavanda e tinta fresca?"
    
    mc "Camille providenciou a lavanda. Larissa providenciou a lixa na parede."
    
    narrator "Wendell andou pelo corredor, vistoriando tudo. O papel de parede velho havia sumido, substituído por paredes brancas lisas. O assoalho rangente tinha recebido óleo de peroba."
    
    show katia neutral at left
    show huey neutral at right
    
    professor_wendell "Os ângulos... as sombras... O defeito estrutural visual do corredor foi ocultado com gesso e ilusão de ótica?"
    
    huey "Geometria básica aplicada à percepção espacial, professor."
    
    professor_wendell "Isso é um trabalho de nível de Mestrado. E de muito suor."
    
    narrator "Ele parou na sala e segurou firme a prancheta de avaliação. Com a outra mão, ele destampou um pincel marcador vermelho."
    
    narrator "Ele se virou para o papel, pronto para fazer um X gigantesco na folha de inspeção."
    
    mc "Ele vai fechar a casa! Não!"
    
    narrator "A fadiga me cegou. Eu não ia deixar aquela burocracia vencer. Pulei na direção dele."
    
    professor_wendell "O que significa isso?!"
    
    narrator "O pincel desceu em direção ao papel."
    
    call screen minigame_pincel
    
    if _return:
        narrator "Num salto digno de cinema, eu agarrei a mão dele e puxei o pincel vermelho com toda a minha força."
        
        narrator "Nós dois tropeçamos. O pincel voou longe e bateu no rodapé que nós tínhamos acabado de envernizar."
        
        show katia angry at left
        show larissa sad at right
        
        katia "Ficou louco?!"
        
        narrator "Katia e Larissa pularam em cima de mim, imobilizando meus braços e me arrastando para longe da prancheta do professor."
        
        larissa "Desculpa, professor! Ele bebeu muito café, não dorme há dois dias por causa do gesso!"
        
        mc "Me soltem! Ele ia cancelar o edital! Ele ia marcar o X vermelho de 'Interditado'!"
        
        narrator "O Professor Wendell ajeitou os óculos, olhou para o formulário no chão, olhou para mim sendo imobilizado por duas garotas... e o rosto dele ficou vermelho."
        
        narrator "Ele cobriu a boca. Seus ombros começaram a tremer."
        
        professor_wendell "Pff... HAHAHAHAHA!"
        
        narrator "O professor Wendell, o homem mais sério e burocrático do campus, teve uma crise de risos. Ele ria tanto que precisou se apoiar na parede limpa, enxugando uma lágrima."
        
        professor_wendell "Ai, meu Deus... Um ataque terrorista por causa de um formulário da prefeitura."
        
        mc "Mas o despejo..."
        
        professor_wendell "Eu não ia cancelar o edital, seu moleque dramático! Eu ia marcar o X na caixa de 'Aprovação Estética Total'!"
        
        professor_wendell "Eu sempre vi grupos neste Edital se destruírem na primeira briga por pratos sujos na pia. Vocês quase tiveram a casa inteira queimada... e a reconstruíram com as próprias mãos em uma semana."
        
        professor_wendell "Isso vai além de estética. É a prova cabal de que a Rua Aurora, 57 pertence a vocês. O Edital está renovado para mais um semestre."
        
        narrator "O silêncio na sala foi absoluto por três segundos."
        
        show nicole happy at left
        show samantha happy at right
        
        nicole "NÓS CONSEGUIMOS!"
        
        narrator "Samantha começou a pular. Katia soltou meus braços e deu um soco no ar. Larissa e Camille se abraçaram."
        
        mc "Aí! É... me desculpe por voar na sua mão, professor."
        
        professor_wendell "Só peguem o meu pincel ali no canto. O mérito é de vocês. Celebrem. Só não coloquem fogo na casa de novo."
        
    else:
        narrator "Tentei agarrar o pincel dele, mas tropecei nas latas de tinta e caí de cara no chão."
        narrator "As meninas me agarraram imediatamente, morrendo de vergonha."
        professor_wendell "Isso foi um salto... excêntrico. De qualquer forma..."
        professor_wendell "Eu marquei o 'X' na 'Aprovação Estética Total'. O Edital está renovado para mais um semestre."
        narrator "O alívio foi tanto que a vergonha passou rápido. Comemoramos a nossa vitória, mesmo com a minha falha épica."
        
    hide professor_wendell
    
    narrator "Wendell foi embora, sorrindo sozinho na calçada."
    
    scene bg sala_jantar with dissolve
    
    narrator "Naquela noite, arrastamos os móveis reformados para o canto. A sala de jantar virou uma pista de dança improvisada. Pedimos pizza, abrimos refrigerante barato e rimos até o estômago doer."
    
    narrator "Não tinha mais cheiro de fumaça. Só o cheiro do nosso lar, que nós construímos de novo."
    
    scene black with fade
    
    narrator "Fim do Capítulo 8."
    
    call end_of_chapter_validation("capitulo9") from _call_end_of_chapter_validation_4
