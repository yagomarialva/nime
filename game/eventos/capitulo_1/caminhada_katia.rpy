# === CAMINHADA NA MADRUGADA COM KATIA ===
label capitulo1_caminhada_katia:
    scene bg campus_night with fade
    show katia neutral at center
    
    narrator "A batida abafada da festa finalmente ficou para trás. O ar frio da noite cortava nossos rostos, mas qualquer coisa era melhor que aquela iluminação estroboscópica."
    
    katia "Obrigada por me tirar de lá. Eu ia começar a chutar as caixas de som."
    
    narrator "Caminhamos mantendo uma distância segura. Silêncio absoluto, pontuado apenas pelos nossos passos no asfalto."
    
    katia "Você provavelmente acha que eu sou insuportável. Uma purista de cinema que odeia que as outras pessoas se divirtam."
    
    menu:
        "Não discordo":
            $ points_katia += 1
            mc "Você tem um complexo de superioridade como mecanismo de defesa. É meio óbvio."
            katia "Hmpf. Análise barata. Mas aceitável."
            
        "Exílio voluntário":
            $ points_katia += 3
            mc "Acho que você odeia as coisas populares antes que elas tenham a chance de decepcionar você."
            narrator "Ela parou de andar por uma fração de segundo. Um tropeço invisível."
            katia "Não me analise em voz alta."
            
        "Aceitar a fuga":
            $ points_katia += 2
            mc "Não ligo se você odeia as pessoas. Eu só queria fugir do cheiro de cerveja."
            katia "Pelo menos somos dois covardes convenientes."
            
    scene bg house_exterior_night with fade
    narrator "A república onde ela ficava estava escura."
    
    katia "Eu posso cruzar a porta sozinha. Não precisa ser cavalheiro. Eu odeio cavalheiros."
    narrator "Ela destrancou a porta. Mas antes de empurrá-la, soltou um longo e pesado suspiro."
    katia "Foi a caminhada mais silenciosa que eu tive na semana. Obrigada... Eu precisava."
    
    narrator "A porta se fechou. Fiquei sozinho do lado de fora, a noite parecendo um pouco menos vazia."
    jump capitulo1_quarta_escolha
