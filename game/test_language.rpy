# Teste do Sistema de Idiomas
# Arquivo para testar se as traduções estão funcionando

label test_language:
    scene bg city with fade
    
    # Teste de tradução
    narrator "Testando sistema de idiomas..."
    
    # Teste de personagens
    show nicole neutral at center
    nicole "Olá! Sou Nicole."
    hide nicole
    
    # Teste de menu
    menu:
        "Opção 1":
            narrator "Você escolheu a opção 1."
        "Opção 2":
            narrator "Você escolheu a opção 2."
    
    return