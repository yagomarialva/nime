label capitulo13_katia:
    if status_katia == "ruina":
        scene bg sala_reuniao with fade
        narrator "Eu não achei que o orgulho de Katia a faria tomar uma atitude suicida."
        narrator "Ela foi até o gabinete do reitor sozinha e invadiu a sala com um pé de cabra, destruindo o próprio ofício de cancelamento."
        narrator "Ela foi expulsa da universidade, presa por invasão de propriedade e perdeu o futuro na advocacia."
        narrator "O último olhar dela para mim, antes de ser levada pelos seguranças do campus, foi de puro ódio."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Katia){/b}"
        return
        
    elif status_katia == "amizade":
        scene bg biblioteca with fade
        play music "music/biblioteca.mp3" fadein 1.0
        narrator "O reitor venceu. O Grêmio Estudantil e o Clube de Cinema foram dissolvidos para sempre."
        show katia neutral at center
        narrator "Katia mudou-se para os fundos da biblioteca. Cercada por pilhas de códigos civis e livros de doutrina, ela estudava como uma máquina."
        katia "Oi. O que você quer? Eu tenho que ler mais três acórdãos."
        mc "Nada... só vim ver como você estava."
        narrator "A chama da liderança dela havia sido apagada. Ela seria uma ótima advogada civil, mas a alma política dela estava morta."
        call end_of_chapter_validation("capitulo14")
        
    elif status_katia == "romance":
        scene bg pátio with fade
        narrator "O pátio principal estava tomado. Centenas de alunos protestavam contra as medidas autoritárias do reitor."
        show katia happy at center
        narrator "Com um megafone em mãos e comigo ao lado dela cobrindo os flancos e organizando a logística, Katia era uma força da natureza."
        narrator "Acovardado pela pressão e pelos jornalistas cobrindo a manifestação, o reitor apareceu na janela e cedeu. O Grêmio estava salvo."
        show katia blush
        narrator "Katia desceu da caçamba do caminhão de som, ofegante."
        katia "Nós conseguimos... Você viu aquilo? Eu não teria organizado metade das lideranças sem você nos bastidores."
        mc "Todo líder político precisa de um excelente chefe de gabinete."
        katia "E de um parceiro pro resto da vida também."
        narrator "Ela largou o megafone no chão, puxou a gola da minha camisa e me beijou na frente das câmeras da universidade inteira."
        call end_of_chapter_validation("capitulo14")
