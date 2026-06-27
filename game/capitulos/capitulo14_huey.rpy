label capitulo14_huey:
    scene bg atelie_huey with fade
    
    narrator "O ateliê estava sem móveis. Apenas o cheiro de aguarrás denunciava a história artística daquele lugar."
    
    show huey neutral at center
    
    if status_huey == "amizade":
        narrator "Huey enrolava cuidadosamente as telas encomendadas pela galeria de arte. Perfeitas. Sem cor."
        huey "Os parâmetros logísticos da mudança foram concluídos com sucesso."
        mc "Você vai ficar bem?"
        huey "Financeiramente, sim. Emocionalmente, neutra."
        narrator "O abraço de despedida foi frio. A amizade havia sobrevivido à academia, mas a magia dela estava lacrada naquelas caixas."
        
    elif status_huey == "romance":
        narrator "Huey segurava uma lata de spray verde na mão. O rosto dela estava, como sempre, sujo de tinta."
        show huey happy
        mc "Você percebe que a universidade vai cobrar a multa se você pintar a parede antes de entregarmos as chaves, né?"
        huey "As regras burguesas de locação de imóveis não contemplam a expressão artística plena."
        narrator "Ela apertou o spray e desenhou um coração caótico, cheio de curvas assimétricas e cores pingando, direto no meio da parede da sala."
        show huey blush
        huey "Eu tentei calcular você durante muito tempo."
        huey "Mas o amor é a única coisa que não entra em nenhum gráfico, em nenhuma perspectiva linear."
        mc "E que cor o amor tem pra você?"
        huey "Todas elas. Especialmente agora."
        narrator "Ela soltou a lata de spray no chão. Nossas mãos manchadas de tinta se entrelaçaram e nós deixamos a nossa última marca juntos na Rua Aurora."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
