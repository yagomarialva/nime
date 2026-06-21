label capitulo1_aula_professor_wendell:
    scene bg auditorium with fade
    
    narrator "Cheguei atrasado para o que deveria ser a nossa 'reunião de alinhamento' do edital."
    
    show professor_wendell neutral at center
    
    narrator "O Professor Wendell estava sentado de pernas cruzadas em cima da própria mesa."
    
    professor_wendell "A média acadêmica do nosso querido trio da Rua Aurora. Devo dizer, é uma tragédia grega."
    
    hide professor_wendell
    
    show nicole sad at right
    nicole "Isso é impossível! Eu gabaritei o teste de introdução metodológica!"
    
    narrator "Nicole analisava um boletim impresso freneticamente. O rosto pálido e a respiração curta denunciavam o pânico. O caos era o seu pior pesadelo."
    
    show katia neutral at left
    katia "Você gabaritou. Eu entreguei a prova em branco. Na média, nós reprovamos."
    
    nicole "Como você ousa entregar em branco?! Se perdermos a bolsa por sua causa..."
    
    katia "O professor pediu uma análise sobre a futilidade da arte moderna. O vazio da página era a minha análise. Se ele não entendeu, a falha é dele."
    
    narrator "Katia jogava as palavras como quem joga pedras na água, fingindo não se importar com as ondulações. Mas seus braços estavam cruzados com força demais."
    
    mc "Vocês duas vão acabar matando a gente antes mesmo do teto desabar."
    
    show professor_wendell happy at center
    professor_wendell "A Srta. Nicole exigiu as regras de correção. A Srta. Katia tentou desconstruir a nota através da performance."
    professor_wendell "E nenhum de vocês parou para pensar que a nota do grupo é uma só. Se um de vocês afundar, a casa inteira afunda."
    
    narrator "O sorriso dele desapareceu."
    
    professor_wendell "Vocês são brilhantes. E são covardes emocionais. Vocês preferem brigar a admitir que dependem uns dos outros para não morar na rua."
    professor_wendell "A nossa reunião acabou. Subam suas notas. Ou arrumem as malas."
    
    hide professor_wendell
    
    narrator "Ele pegou seu sobretudo e saiu. O silêncio que se seguiu foi insuportavelmente pesado. Uma estática quebrada."
    
    mc "A convivência aqui não vai ser mágica... vai ser um processo violento."
    
    $ add_shared_memory("first_house_meeting", ["nicole", "katia"], "O momento em que percebemos que a bolsa dependia de não nos matarmos.")
    
    return
