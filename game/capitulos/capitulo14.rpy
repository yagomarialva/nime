label capitulo14:
    if "capitulo14" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo14")
        
    scene bg auditorio with fade
    
    narrator "O calor dentro do auditório da universidade era sufocante, mas ninguém se importava."
    
    narrator "Nós vestíamos becas pretas e capelos que não paravam quietos na cabeça. O burburinho de centenas de alunos preenchia o salão."
    
    narrator "Depois de anos de provas exaustivas, crises existenciais, brigas por pizza na geladeira e desastres quase fatais... nós finalmente chegamos ao fim."
    
    show professor_wendell neutral at center
    
    narrator "O Professor Wendell se aproximou do púlpito no palco principal. Ele pigarreou, ajustando os óculos."
    
    wendell "Caros alunos. Quando vocês entraram por aquelas portas há alguns anos, vocês eram blocos de argila."
    
    wendell "E a faculdade... bem, a faculdade foi a marreta."
    
    narrator "O auditório riu."
    
    wendell "Nós moldamos vocês com pressão. Mas alguns de vocês não apenas resistiram à pressão, como criaram sistemas de sobrevivência inteiramente novos."
    
    narrator "Ele olhou diretamente para a nossa fileira. As meninas da Rua Aurora estavam sentadas lado a lado, sorrindo."
    
    wendell "Vocês aprenderam que o brilhantismo acadêmico não significa nada sem a empatia humana. Que a convivência, por mais peculiar e caótica que seja, é o que nos mantém sãos."
    
    wendell "Vocês sobreviveram. E agora, o mundo lá fora é de vocês."
    
    narrator "Aplausos ensurdecedores tomaram conta do lugar."
    
    hide professor_wendell
    scene bg pátio with fade
    
    narrator "No pátio, nós nos juntamos para a tradicional foto. Larissa, Camille, Samantha, Katia, Nicole, Huey e eu."
    
    narrator "No 'três', jogamos os capelos para o alto. O clique da câmera eternizou o fim de uma era."
    
    scene bg rua_aurora with dissolve
    
    narrator "Depois da cerimônia, o inevitável bateu à porta."
    
    narrator "Era hora de empacotar as coisas e trancar a casa na Rua Aurora para sempre."
    
    if escolha_fogos == "larissa":
        jump capitulo14_larissa
    elif escolha_fogos == "camille":
        jump capitulo14_camille
    elif escolha_fogos == "samantha":
        jump capitulo14_samantha
    elif escolha_fogos == "katia":
        jump capitulo14_katia
    elif escolha_fogos == "nicole":
        jump capitulo14_nicole
    elif escolha_fogos == "huey":
        jump capitulo14_huey
    elif escolha_fogos == "harem" or escolha_fogos == "grupo":
        jump capitulo14_harem
