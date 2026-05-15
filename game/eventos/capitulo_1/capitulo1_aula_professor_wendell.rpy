# === AULA COM O PROFESSOR WENDELL - A SALA DO CAOS ===
label capitulo1_aula_professor_wendell:
    scene bg auditorium with fade
    
    narrator "Cheguei atrasado. O cronograma dizia 'Eletiva: Conexões Humanas', mas o que encontrei ao abrir a porta foi o mais puro caos."
    narrator "Não havia ninguém sentado. As mesas haviam sido empurradas contra a parede."
    
    show professor_wendell neutral at center
    
    narrator "O Professor Wendell estava sentado de pernas cruzadas em cima da própria mesa, balanceando um diapasão na mão."
    narrator "No centro do chão vazio da sala, ele havia desenhado um enorme círculo com giz branco."
    
    professor_wendell "O paradoxo do ouriço de Schopenhauer. Alguém me explique como não morrer congelado sem ser devorado por espinhos."
    
    hide professor_wendell
    
    narrator "Ele não estava dando uma aula. Ele estava assistindo a um incêndio forestal."
    
    show larissa angry at left
    larissa "Isso não faz o menor sentido! Não tem exercício prático? Não tem objetivo?"
    larissa "Qual a utilidade funcional de ficar debatendo um bicho imaginário?!"
    
    narrator "Larissa andava de um lado pro outro fora do círculo de giz, batendo a ponta do pé com força no chão falso de madeira. Ela precisava de movimento. O impasse a estava enlouquecendo."
    
    show nicole sad at right
    nicole "O problema não é a falta de prática! O problema é que a variável do 'congelamento' não está quantificada! Como vamos ser avaliados por algo sem critério?!"
    
    narrator "Nicole analisava a lousa freneticamente. O rosto pálido e a respiração curta denunciavam o pânico. O caos era o seu pior pesadelo."
    
    show katia neutral at left
    katia "Vocês são tão... previsíveis."
    katia "Estão discutindo a regra do jogo sem perceber que o tabuleiro já está viciado. Espinhos ou frio, o fim é a dor. Que exercício medíocre."
    
    narrator "Katia jogava as palavras como quem joga pedras na água, fingindo não se importar com as ondulações. Mas seus braços estavam cruzados com força demais."
    
    hide larissa
    hide nicole
    hide katia
    
    narrator "Olhei para o fundo da sala. Atrás de uma prateleira de livros derrubada, Camille mantinha os olhos fechados, tentando, em vão, filtrar a energia pesada e descontrolada do ambiente."
    narrator "No canto oposto, Huey rascunhava algo freneticamente em um bloco, os nós dos dedos brancos. E Samantha..."
    narrator "Samantha estava sentada no chão, os fones de ouvido maiores que a própria cabeça apertados sobre os ouvidos, lutando contra o pânico social que ameaçava engoli-la."
    
    mc "Eles não vão chegar a um acordo. Nunca."
    
    show professor_wendell happy at center
    professor_wendell "Fascinante. Simplesmente fascinante."
    
    narrator "Wendell finalmente desceu da mesa e caminhou até o centro do círculo de giz."
    
    professor_wendell "A Srta. Larissa atacou o problema. A Srta. Nicole exigiu as regras. A Srta. Katia tentou desconstruir a dor."
    professor_wendell "E todos vocês... todos vocês continuam isolados em suas próprias trincheiras."
    
    narrator "O sorriso dele desapareceu."
    
    professor_wendell "Vocês são brilhantes. E são covardes."
    professor_wendell "Não quero que tentem ler a mente uns dos outros. Quero que se perdoem por ferir e por queimar."
    
    professor_wendell "A nossa aula acabou."
    
    hide professor_wendell
    
    narrator "Ele pegou seu sobretudo e saiu, deixando vinte alunos sozinhos com ecos e atritos."
    narrator "O silêncio que se seguiu foi insuportavelmente pesado. Uma estática quebrada."
    
    mc "A conexão aqui não vai ser mágica... vai ser um processo violento."
    
    # Memória compartilhada refatorada (sem "amigos felizes")
    $ add_shared_memory("first_group_meeting", ["nicole", "camille", "katia", "huey", "samantha", "larissa"], "O momento em que percebi o quão isolados todos realmente estavam.")
    
    jump capitulo1_terceira_escolha
