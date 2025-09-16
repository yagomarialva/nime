# === ÚLTIMA ATUALIZAÇÃO - FIM DO CONTEÚDO ATUAL ===
label ultima_atualizacao:
    scene bg campus_sunset with fade
    
    narrator "Você chegou ao fim do conteúdo disponível até o momento."
    
    show professor_wendell neutral at center
    professor_wendell "Parabéns por ter chegado até aqui, querido aluno!"
    professor_wendell "Você completou uma jornada incrível de descobertas, conexões e crescimento pessoal."
    
    hide professor_wendell with dissolve
    
    narrator "A história que você viveu até agora foi apenas o começo de uma aventura muito maior."
    narrator "Cada escolha que você fez, cada pessoa que conheceu, cada momento compartilhado..."
    narrator "Tudo isso moldou sua jornada de uma forma única e especial."
    
    # Mostrar resumo das conexões formadas
    narrator "📊 RESUMO DA SUA JORNADA:"
    narrator "• Você conheceu pessoas incríveis com personalidades únicas"
    narrator "• Formou conexões especiais baseadas em suas escolhas"
    narrator "• Descobriu diferentes aspectos de si mesmo através das interações"
    narrator "• Participou de eventos que moldaram sua personalidade"
    
    show professor_wendell neutral at center
    professor_wendell "Mas esta é apenas uma pausa na sua jornada, não o fim."
    professor_wendell "Novos capítulos estão sendo desenvolvidos com muito carinho e dedicação."
    professor_wendell "Cada atualização trará novas aventuras, novos desafios e novas oportunidades de crescimento."
    
    hide professor_wendell with dissolve
    
    narrator "🔮 O QUE VIRÁ A SEGUIR:"
    narrator "• Novos capítulos com histórias ainda mais profundas"
    narrator "• Desenvolvimento dos relacionamentos que você começou a construir"
    narrator "• Novos eventos e situações que testarão suas escolhas"
    narrator "• Revelações surpreendentes sobre os personagens"
    narrator "• Finais alternativos baseados em suas decisões"
    
    show professor_wendell neutral at center
    professor_wendell "Fique atento para as próximas atualizações!"
    professor_wendell "Sua jornada na Faculdade Solária está apenas começando."
    professor_wendell "Obrigado por fazer parte desta história conosco."
    
    hide professor_wendell with dissolve
    
    narrator "Enquanto isso, você pode:"
    narrator "• Rejogar os capítulos disponíveis para explorar diferentes caminhos"
    narrator "• Experimentar escolhas diferentes para ver novos diálogos"
    narrator "• Aprofundar seus relacionamentos com personagens específicos"
    narrator "• Descobrir todas as possibilidades que o jogo oferece"
    
    # Momento especial de reflexão
    call emotional_moment("gratitude", None, "Gratidão pela jornada compartilhada") from _call_emotional_moment_ultima_atualizacao
    
    narrator "Obrigado por ter escolhido viver esta história conosco."
    narrator "Sua jornada na Faculdade Solária continuará em breve..."
    
    # Opções finais
    menu:
        "Voltar ao menu principal":
            return
            
        "Refletir sobre a jornada":
            narrator "Você se senta em um banco do campus, observando o pôr do sol."
            narrator "Cada memória, cada sorriso, cada momento especial..."
            narrator "Tudo isso fez parte de uma experiência única e inesquecível."
            narrator "E você sabe que, quando as atualizações chegarem, estará pronto para continuar."
            jump ultima_atualizacao
