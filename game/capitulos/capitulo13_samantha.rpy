label capitulo13_samantha:
    if status_samantha == "ruina":
        scene bg quarto_samantha with fade
        narrator "Samantha tomou uma decisão drástica."
        narrator "Ela não apenas deletou o repositório do jogo. Ela trancou a matrícula na faculdade."
        narrator "Quando fui procurá-la, seus pais disseram que ela não queria receber ninguém, muito menos eu."
        narrator "Eu a chamei de dramática, e ela me provou que a dor que ela sentia era real o suficiente para queimar os próprios sonhos."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Samantha){/b}"
        return
        
    elif status_samantha == "amizade":
        scene bg quarto_samantha with fade
        narrator "O jogo dela foi deletado da internet. A poeira dos haters baixou."
        show samantha neutral at center
        narrator "Ela conseguiu um estágio numa megaempresa corporativa de desenvolvimento de software de banco. Segurança, anonimato, e tédio absoluto."
        samantha "Meu chefe é péssimo, mas o salário cai na conta. É uma vida segura."
        mc "Se você está feliz com isso..."
        narrator "Ela não estava feliz. Mas estava segura. Nós mantivemos a amizade, mas a empolgação da criadora de mundos que eu amava havia sido formatada."
        call end_of_chapter_validation("capitulo14")
        
    elif status_samantha == "romance":
        scene bg quarto_samantha with fade
        narrator "O quarto dela parecia uma base de operações militar. Nós passamos 48 horas seguidas online."
        show samantha happy at center
        narrator "Eu fui o escudo dela. Banei trolls, moderei o chat de lançamento, e fiz o filtro humano para que apenas a verdadeira comunidade de gamers chegasse até ela."
        samantha "Olha o gráfico da Steam... as avaliações positivas estão engolindo o review bomb!"
        narrator "A barra de avaliações virou de 'Neutras' para 'Extremamente Positivas'."
        show samantha blush
        samantha "Eles estão adorando o combate! Eles viram o que eu construí!"
        mc "Eles viram quem você é, Sam. Uma dev genial."
        narrator "Ela empurrou a cadeira gamer pra trás, pulou em cima de mim e me beijou com a euforia de mil conquistas de platina sendo debloqueadas ao mesmo tempo."
        samantha "Eu não teria conseguido lançar se você não estivesse aqui sendo o meu tank."
        mc "Pra isso que serve um player 2."
        call end_of_chapter_validation("capitulo14")
