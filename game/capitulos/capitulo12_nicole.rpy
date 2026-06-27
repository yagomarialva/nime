label capitulo12_nicole:
    scene bg cozinha with fade
    
    narrator "Ouvi um barulho de vidro quebrando vindo da cozinha."
    
    narrator "Quando entrei, encontrei Nicole no chão, cercada por caquinhos de um copo de cristal que ela mesma havia comprado. Ela segurava o celular, tremendo."
    
    show nicole sad at center
    
    mc "Nicole! Você se cortou? O que aconteceu?"
    
    nicole "O flat... Ela descobriu que o contrato do flat foi cancelado há meses. Ela me ligou gritando."
    
    narrator "Nicole respirava com dificuldade, entrando em pânico."
    
    nicole "Ela cortou o cartão. Ela ligou pra reitoria e cortou o pagamento da mensalidade. Ela disse que eu vou voltar pra casa amanhã, ou vou morar na rua."
    
    nicole "Eu não sei fazer nada, player! Eu não tenho dinheiro pra pagar a faculdade, eu não tenho dinheiro pra comer! Eu não sei ser pobre!"
    
    menu:
        "Você não precisa do dinheiro dela. Vamos arrumar um emprego juntas, e processá-la pela autonomia.":
            $ store.status_nicole = "romance"
            mc "Ei, olha pra mim. Você é a garota mais inteligente que eu conheço. Você fez projetos incríveis nesse semestre."
            mc "Vamos arrumar um emprego de meio período, mesmo que pague pouco. E eu ajudo você com a papelada pra se emancipar financeiramente. Nós vamos sobreviver juntas."
            
            show nicole blush
            nicole "Trabalhar... num café? Ou num caixa de supermercado?"
            mc "Sim. É trabalho honesto. Você aguenta, e eu estarei lá."
            narrator "Ela respirou fundo, a expressão de terror dando lugar à determinação arrogante de sempre. O abraço dela foi o mais apertado de todos."
            
        "Ceder ao controle: Peça desculpas. Volte pra casa dela. A faculdade é cara demais.":
            $ store.status_nicole = "amizade"
            mc "Nicole, sejamos realistas. Sem a mensalidade, você perde o diploma. Liga pra ela, peça desculpas e aceite voltar pro flat."
            
            show nicole neutral
            nicole "Abaixar a cabeça... É, acho que era só ilusão achar que eu poderia ter minha própria vida."
            narrator "Ela juntou os cacos de vidro com o rosto inexpressivo. A Nicole independente morreu ali. Ela sobreviveria, mas seria um fantoche para sempre."
            
        "Rejeição: Você mereceu. Mentiu esse tempo todo e achou que nunca iam descobrir.":
            $ store.status_nicole = "ruina"
            mc "Você esperava o quê? Que viver uma mentira fosse durar pra sempre? O castigo chegou."
            
            show nicole angry
            nicole "Você está me dando lição de moral agora?! Você, que me encobriu?!"
            narrator "Ela jogou um caco de vidro na parede."
            nicole "Eu não preciso de um covarde me julgando. Sai da minha frente. Pega as suas coisas e me deixa em paz!"
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
