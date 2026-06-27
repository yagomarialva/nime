label capitulo14_camille:
    scene bg casa_interior with fade
    
    narrator "A sala que Camille costumava encher de fumaça de sálvia estava estranhamente limpa."
    
    show camille neutral at center
    
    if status_camille == "amizade":
        narrator "Ela estava checando e-mails no celular, já vestida com roupas de escritório."
        camille "O táxi já está chegando. Tenho uma reunião amanhã de manhã."
        mc "Boa sorte no mundo corporativo. Espero que não te engula."
        camille "É só trabalho. Eu sobrevivo."
        narrator "Demos um abraço educado. Camille entrou no carro e partiu para sua vida pragmática, deixando o esoterismo e o nosso romance no passado."
        
    elif status_camille == "romance":
        narrator "Camille acendeu um único palito de incenso de lavanda."
        show camille happy
        mc "Achei que você não ia mais acender essas coisas."
        camille "Eu não acendo pela magia. Acendo porque o cheiro me lembra a primeira noite que eu conversei com você."
        narrator "Ela andou pelo cômodo vazio, tocando as paredes."
        show camille blush
        camille "Eu cheguei aqui achando que o universo me diria o que fazer através das estrelas."
        camille "Mas a verdade é que você foi a minha âncora. Você não me deixou flutuar para longe e nem me deixou afundar."
        mc "Você também ancorou todo mundo aqui."
        narrator "Ela fechou os olhos e encostou a cabeça no meu peito, respirando o cheiro do incenso misturado com o momento perfeito."
        camille "Nossas auras estão irremediavelmente entrelaçadas. Eu te amo."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
