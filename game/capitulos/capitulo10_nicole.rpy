label capitulo10_nicole:
    scene bg sala_jantar with dissolve
    
    narrator "A casa estava em silêncio. Faltava um dia para a prova final, mas Nicole estava na cozinha pintando as unhas."
    
    show nicole neutral at center
    
    mc "Eu achei que 'Relações Internacionais' fosse um curso difícil, mas pelo visto é só fazer francesinha nas unhas."
    
    narrator "Nicole não riu da piada. Ela continuou focada no pincel do esmalte."
    
    nicole "Minha mãe ligou. Ela disse que se eu tirar nota máxima nas provas, ela vai liberar meu cartão sem limites e pagar o aluguel de um flat mobiliado de luxo perto do campus."
    
    mc "Espera... você iria embora da Rua Aurora?"
    
    nicole "É a chance de sair desse cheiro de reforma e do banheiro compartilhado. É a vida que eu tinha antes."
    
    mc "E é isso que você quer?"
    
    narrator "A mão dela tremeu, borrando a unha."
    
    nicole "Por isso eu não estou estudando. Se eu tirar um 8, eu perco a oferta dela. Eu fico presa aqui."
    
    mc "Presa aqui com a gente. Você está se autossabotando para não ir embora."
    
    narrator "Ela largou o esmalte e cruzou os braços defensivamente."
    
    nicole "Não seja presunçoso. Eu só estou com preguiça."
    
    mc "Nicole... olha pra mim."
    
    narrator "Caminhei até ela e segurei suas mãos, ignorando o esmalte fresco."
    
    mc "Sua mãe sempre usou dinheiro pra te controlar. O flat de luxo é só mais uma corrente. Tirar uma nota ruim de propósito só prova que ela ainda controla suas escolhas."
    
    nicole "E o que eu devo fazer? Desafiar ela? Passar o resto da vida numa república caindo aos pedaços?"
    
    mc "Sim. Porque aqui é o SEU lar. E nós somos a sua família agora. Você tira 10 nessa prova e esfrega na cara dela que você escolheu ficar na Rua Aurora, não por necessidade, mas porque aqui você tem a gente."
    
    narrator "Uma lágrima teimosa fugiu dos olhos dela. Ela apertou minhas mãos."
    
    nicole "Você é irritantemente convincente. Pega meus livros. Vamos estudar."
    
label loop_diplomacia_nicole:
    narrator "O telefone de Nicole tocou. Era a mãe dela."
    nicole "Ela tá ligando de novo pra confirmar. O que eu falo pra ela, sem ela surtar e cancelar tudo?!"
    
    $ init_diplomacy_game()
    call screen minigame_diplomacy
    
    if _return == "lose":
        narrator "A ligação virou uma briga aos gritos ou um silêncio mortal. Nicole perdeu todo o foco dos estudos."
        mc "Erramos a mão. A diplomacia falhou. A barra de paciência dela zerou ou o tempo acabou. Vamos dar load e tentar de novo!"
        jump loop_diplomacia_nicole
    
    if _return == "win":
        nicole "Mãe, morar na Rua Aurora está construindo meu capital social e alianças políticas para o futuro."
        narrator "Houve um silêncio na linha."
        nicole "Ela... ela acreditou. Ela adorou a ideia de 'capital social'."
        mc "O jogo virou. Política externa impecável!"
            
    scene black with fade
    
    narrator "E assim ela fez. A prova foi destruída pela perfeição acadêmica e arrogante de Nicole. Ela enviou o print do 10 para a mãe, junto com um 'Não vou me mudar'."
    
    scene bg quarto with dissolve
    
    show nicole happy at center
    
    narrator "À noite, eu encontrei um envelope na minha porta. Nicole me puxou para o corredor."
    
    nicole "Eu disse não pro flat."
    
    mc "Eu sei. A casa toda celebrou."
    
    nicole "O flat ia ser chato de qualquer forma. Ia ser espaçoso demais."
    
    narrator "Ela diminuiu a distância entre nós, pressionando as costas contra a porta do meu quarto."
    
    nicole "Eu me acostumei com lugares apertados. E com pessoas específicas."
    
    narrator "Ela sorriu, o batom vermelho desenhando um flerte descarado, e me beijou profundamente, de forma possessiva."
    
    nicole "Você me fez ficar. Agora você vai ter que me aturar."
    
    call end_of_chapter_validation("capitulo11")
