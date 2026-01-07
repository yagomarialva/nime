# === EVENTO NICOLE E CAMILLE - MASTER EDITION ===
# Tema: Caos Controlado vs Fluxo Natural
# Dinâmica: A garota da planilha vs A garota dos cristais

label evento_nicole_camille:
    # Pequeno ganho de afinidade inicial
    $ points_nicole += 1
    $ points_camille += 1
    
    scene bg library with dissolve
    
    # Atmosfera
    narrator "A biblioteca deveria ser um templo de silêncio. Mas hoje, havia uma guerra fria acontecendo na mesa do canto."

    # Nicole já está lá, estressada. (Show, Don't Tell)
    show nicole angry at left
    
    # Som de clique de caneta frenético (se tiver sfx)
    narrator "*Click. Click. Click. Click.*"
    
    nicole "Isso não faz sentido estatístico. O desvio padrão está... Argh! Quem desenhou esse gráfico? Uma criança?"
    
    narrator "A garota cercada de planilhas parecia prestes a morder o monitor do laptop. A aura dela era puro cortisol."
    
    # O MC se aproxima
    mc "Com licença... essa mesa é compartilhada?"
    
    # Ela nem olha
    nicole "Desde que você não respire muito alto e não balance a mesa. Estou calculando a variância de... Esquece. Senta aí."
    
    # Camille entra. Não se apresenta, ela apenas AGE.
    show camille gentle at right with moveinright
    
    narrator "De repente, o cheiro de livros velhos foi substituído por... lavanda?"
    
    camille "Oh... a energia aqui está muito densa. Muito... quadrada."
    
    # Camille coloca um cristal em cima dos papéis da Nicole
    narrator "A recém-chegada tirou uma pedra roxa da bolsa e a colocou delicadamente sobre a planilha impressa da Nicole."
    
    # O conflito explode
    show nicole angry
    nicole "Ei! O que você pensa que está fazendo?"
    
    camille "Ametista. Transmuta energia negativa. Você está com uma nuvem cinza sobre a cabeça, querida. Bloqueia o fluxo criativo."
    
    nicole "Isso não é uma nuvem cinza, é um gráfico de dispersão! E você está colocando uma pedra suja em cima de dados confidenciais!"
    
    camille "Nada é sujo se vem da terra. E seus dados... eles parecem tristes."
    
    nicole "Dados não têm sentimentos! Dados têm precisão! Tira isso daí antes que eu chame a bibliotecária!"
    
    # MC precisa intervir
    narrator "Eu estava preso entre a Fúria da Lógica e a Calma do Caos."
    
    # === MENU DE ESCOLHA ===
    menu:
        "Defender a organização da Nicole (Apoiar Lógica)":
            $ points_nicole += 2
            
            mc "Olha, ela está certa. Biblioteca é lugar de estudo, e você está invadindo o espaço pessoal dela com... pedras."
            
            show nicole neutral
            nicole "Obrigada. Alguém com bom senso. O espaço pessoal é uma variável constante que deve ser respeitada."
            
            show camille sad
            camille "Oh... desculpe. Eu só queria ajudar. A tensão dela está vibrando tão alto que dá pra ouvir."

        "Defender a intenção da Camille (Apoiar Intuição)":
            $ points_camille += 2
            
            mc "Calma, Nicole. Ela só estava tentando ajudar. Você realmente parece que vai explodir a qualquer momento."
            
            show camille happy
            camille "Viu? Ele sente também. A empatia é uma forma de inteligência."
            
            show nicole angry
            nicole "Eu não vou 'explodir'. Estou apenas otimizando meu tempo. E 'boas intenções' não corrigem erros de amostragem."

        "Sugerir que a pedra serve de peso de papel (Neutro)":
            $ points_nicole += 1
            $ points_camille += 1
            
            mc "Ei, que tal um meio termo? A pedra segura os papéis para não voarem com o ar condicionado. Função e... energia?"
            
            show nicole thinking
            nicole "Hmmm. O sistema de ventilação aqui é instável... Suponho que um peso de papel geológico tenha utilidade prática."
            
            show camille happy
            camille "E enquanto segura o papel, purifica a intenção. Perfeito."

    # === TRANSIÇÃO ===
    narrator "Nicole suspirou, ajeitando os óculos. Ela não jogou a pedra fora, mas a empurrou para o canto da mesa, milimetricamente alinhada."
    
    nicole "Sou Nicole, a propósito. Análise de Dados. E se você for colocar mais pedras, me avise para eu recalcular o espaço disponível na mesa."
    
    show camille gentle
    camille "Camille. Conexões Energéticas. E não se preocupe, a ametista já está trabalhando. Seus ombros já desceram dois centímetros."
    
    show nicole blush
    nicole "Isso é... postura. Apenas corrigi minha postura ergonômica. Não tem nada a ver com sua pedra mágica."
    
    mc "Acho que vou ficar por aqui. Parece que o estudo vai ser interessante."
    
    # === FECHAMENTO (Sem melodrama) ===
    
    narrator "Não houve abraços nem choros. Apenas o som de teclas sendo batidas com um pouco menos de força, e o cheiro suave de lavanda se misturando ao pó."
    
    nicole "Você... não é totalmente inútil, Camille. O peso da pedra realmente impede as folhas de virarem."
    
    camille "E você tem uma mente brilhante, Nicole. Só precisa deixar a luz entrar nela às vezes."
    
    # Memória compartilhada realista
    $ add_shared_memory("science_vs_magic", ["nicole", "camille"], "O dia em que usamos um cristal místico como peso de papel.")

    return