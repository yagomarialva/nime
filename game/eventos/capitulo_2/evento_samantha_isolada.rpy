label evento_samantha_isolada:
    scene bg casa_interior with dissolve
    
    narrator "A porta do quarto da Samantha estava fechada. De fato, não vi a Samantha em nenhum cômodo da casa o dia inteiro."
    narrator "O único som que vazava por baixo da porta era o ruído abafado de cliques rápidos de teclado e luzes azuis intermitentes."
    
    mc "Ela vai acabar desmaiando se não comer nada."
    
    narrator "Bati na porta. Três toques leves."
    
    mc "Samantha? Eu guardei um pedaço de pizza pra você no microondas. Se quiser, é claro."
    
    narrator "Silêncio. Então, um arrastar de cadeira."
    
    samantha "Estou... ocupada defendendo o mid. Deixa o inventário aí na porta."
    
    menu:
        "Deixar a pizza e ir embora. (Poupar energia)":
            mc "Certo. Tá no chão. Não pisa em cima quando for pegar."
            samantha "Roger that."
            $ add_affinity_points("samantha", 5) # Ela gosta que respeitem o espaço dela
            
        "Ficar e tentar conversar pela porta. (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                mc "O mid pode esperar a fase de rotas. Você precisa de buffs reais de estômago."
                narrator "Fiquei ali, escorado na parede, usando o pouco de energia que eu tinha para arrancar alguma socialização dela."
                samantha "O mundo real... é muito ruidoso. Todo mundo exige atenção o tempo todo. O ping aqui fora é muito alto."
                mc "Você não precisa lidar com todo mundo. Lidando só comigo já é um ótimo tutorial pra iniciantes."
                narrator "A porta abriu uma frestinha. Olhos por trás de grossas lentes de grau espiaram pelo espaço."
                samantha "...Você tem um ponto. Entregue o loot."
                narrator "Entreguei o prato. Ela pegou rápido e quase sorriu."
                $ add_affinity_points("samantha", 15)
            else:
                mc "Eu ia bater papo... mas tô quase fechando o olho. Tenta sair um pouco depois."
                samantha "Eu ouvi os bocejos. Vá log out e durma."
                
    return
