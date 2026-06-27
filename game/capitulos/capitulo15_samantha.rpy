label capitulo15_samantha:
    if status_samantha == "amizade":
        scene bg pc_room with fade
        narrator "Abri meu e-mail. Havia uma mensagem não lida de Samantha."
        narrator "'Hey. O patch novo do nosso sistema de banco foi aprovado. Ganhei um bônus. É dinheiro o suficiente pra comprar aquele console que eu sempre quis. Mas eu chego do trabalho tão cansada que só durmo.'"
        narrator "Ela era a Lead Developer de uma megacorporação. O sonho de muitos. Mas a Sam que passava noites sem dormir criando mundos de RPG havia virado apenas uma linha de código num sistema chato."
        narrator "Respondi com um 'Parabéns!' genérico, fechei o e-mail e voltei para a minha rotina."
        jump creditos_finais
        
    elif status_samantha == "romance":
        scene bg estudio_samantha with fade
        narrator "O escritório do nosso estúdio indie estava uma zona. Caixas de pizza vazias e latas de energético se acumulavam."
        show samantha happy at center
        narrator "Samantha estava de pé na frente do telão, roendo as unhas."
        mc "Faltam dez segundos, Sam."
        samantha "Se o servidor cair de novo, eu juro que quebro o teclado."
        narrator "Dez. Nove. Oito... A contagem regressiva para o lançamento da sequência do nosso jogo. Nós fundamos a empresa com o dinheiro do primeiro sucesso."
        narrator "Zero."
        show samantha blush
        narrator "Os números na tela dispararam. Dez mil downloads no primeiro minuto. Cem mil."
        samantha "Nós... nós derrubamos o banco de dados da loja digital! O jogo é um sucesso explosivo!"
        mc "Conquista Desbloqueada: Bilionários Indies."
        narrator "Ela correu e pulou no meu colo com tanta força que a cadeira de rodinhas deslizou até bater na parede. Ela beijou meu rosto, meu pescoço, e minha boca de forma elétrica."
        samantha "O Player 1 não é nada sem o Player 2. Eu te amo, parceiro."
        narrator "E no brilho dos monitores comemorando o recorde mundial do nosso jogo, eu soube que tínhamos zerado a vida."
        jump creditos_finais
