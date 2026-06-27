label capitulo12_samantha:
    scene bg quarto_samantha with fade
    
    narrator "O quarto da Samantha estava escuro, iluminado apenas pelos monitores exibindo milhares de linhas de comentários em um fórum."
    
    show samantha sad at center
    
    narrator "Ela estava encolhida na cadeira, tremendo levemente."
    
    mc "Sam? O que aconteceu?"
    
    samantha "Vazaram a versão alpha do meu jogo. E os fóruns... eles descobriram que a dev principal é uma mulher."
    
    narrator "Eu olhei para as telas. Havia centenas de comentários destilando ódio gratuito, xingamentos pesados e ameaças de derrubar os servidores do jogo."
    
    samantha "Eles estão destruindo três anos da minha vida. Eles dizem que o jogo é lixo."
    
    narrator "Ela levou o dedo até o teclado, o cursor pairando sobre o botão de 'Delete Repository'."
    
    samantha "Vou apagar tudo. Eu vou fechar os servidores e desistir. Eu não aguento isso, player."
    
    menu:
        "Eles são bots na sua raid. Vamos filtrar o hate e focar nos comentários de quem realmente jogou.":
            $ store.status_samantha = "romance"
            mc "Tira a mão desse botão. Você não vai dar o 'GG' pra um bando de trolls anônimos."
            mc "Vamos ler os reviews de quem jogou de verdade. O jogo é bom, Samantha. Eu sei, eu vi você codando."
            
            show samantha blush
            samantha "Você... você me ajuda a criar os filtros no servidor?"
            mc "Eu serei seu tank e seu moderador."
            narrator "Ela soltou um riso nervoso, enxugando as lágrimas e segurando a minha mão."
            
        "Fugir do problema: Apaga logo isso. É melhor pra sua saúde mental. Desista de ser indie.":
            $ store.status_samantha = "amizade"
            mc "Não vale a pena. Deleta e vai procurar emprego numa grande empresa. Você vai ter paz."
            
            show samantha neutral
            samantha "É... A paz do anonimato corporativo. Ok."
            narrator "Ela pressionou o Delete. O trabalho da vida dela sumiu. Ela suspirou, derrotada, escolhendo a segurança ao invés do sonho."
            
        "Minimizar a dor dela: É só a internet, Sam. Fecha a aba e para de chorar à toa.":
            $ store.status_samantha = "ruina"
            mc "Não seja dramática. Haters existem em todo lugar. Só ignora."
            
            show samantha angry
            samantha "Dramática?! Tem gente ameaçando vazar meu endereço, seu imbecil!"
            narrator "Ela bateu na mesa."
            samantha "Você não entende nada. Sai do meu quarto, agora!"
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
