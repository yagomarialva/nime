# === ESCAPE SILENCIOSO COM NICOLE ===
label capitulo1_caminhada_nicole:
    scene bg campus_night with fade
    show nicole sad at center
    
    narrator "Assim que a porta do pavilhão se fechou atrás de nós, vi os ombros tensionados de Nicole caírem, como se a gravidade do mundo a puxasse para baixo."
    
    nicole "Oitenta e cinco decibéis. Aquele é o limite saudável antes do dano coclear permanente."
    nicole "Estávamos pelo menos nos cento e dez."
    
    narrator "Caminhamos sobre a grama orvalhada do campus. Não era um flerte noturno; era uma evacuação tática de emergência."
    
    nicole "Eu planejei toda a minha semana com precisão metodológica."
    nicole "Mas... nada avisou na grade que as pessoas universitárias seriam tão esmagadoramente improdutivas."
    
    menu:
        "O caos é incontrolável":
            $ points_nicole += 3
            mc "O Professor Wendell meio que avisou. Estamos aqui para colidir. Não para sermos eficientes."
            nicole "Colisões quebram estruturas. Eu não gosto de coisas quebradas."
            
        "Apoiar o esgotamento dela":
            $ points_nicole += 2
            mc "Não dava para aguentar. Você parecia prestes a explodir e eu ofereci um caminho de fuga."
            nicole "Obrigada pela sua intervenção empírica. Foi pragmático de sua parte."
            
        "Lembrar do próprio desconforto":
            $ points_nicole += 1
            mc "Eu estava tendo um colapso induzido pelo barulho também."
            nicole "Então foi uma aliança de auto-preservação puramente simbiótica. Entendido."
            
    scene bg house_exterior_night with fade
    narrator "Paramos a quinze metros do portão da república dela."
    
    nicole "Meu perímetro seguro começa daqui."
    narrator "Ela checou freneticamente o celular, ativando seus alarmes para o dia seguinte, refazendo seus laços com a ordem."
    nicole "Sua presença não quebrou meu fluxo de pensamentos. Diria até que... organizou um pouco a estática da noite."
    
    narrator "Sem esperar resposta, ela cruzou o portão. Deixando uma aura fria, calculada e insanamente fragil."
    jump capitulo1_quarta_escolha
