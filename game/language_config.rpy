# Sistema de Idiomas Simples - NIME
# Configuração básica para português e inglês

# Definir variável persistente
default persistent.language = "en"

init python:
    # Configuração de idiomas disponíveis
    available_languages = {
        "pt": "Português",
        "en": "English"
    }
    
    # Idioma padrão
    default_language = "en"
    
    # Função para trocar idioma
    def change_language(lang):
        if lang in available_languages:
            persistent.language = lang
            if lang == "en":
                renpy.change_language("english")
            else:
                renpy.change_language("portuguese")
            # Salva as preferências
            renpy.save_persistent()
    
    # Função para trocar idioma e fechar o modal
    def change_language_and_close(lang):
        change_language(lang)
        renpy.hide_screen("language_selection")
    
    # Função para obter idioma atual
    def get_current_language():
        return persistent.language if hasattr(persistent, 'language') else default_language

# Configuração de fontes para diferentes idiomas
init python:
    if renpy.variant("mobile"):
        # Fontes para mobile
        config.font_replacement_map["DejaVuSans.ttf"] = "DejaVuSans.ttf"
    else:
        # Fontes para desktop
        config.font_replacement_map["DejaVuSans.ttf"] = "DejaVuSans.ttf"

# Função para inicializar o idioma (chamada quando necessário, não durante init)
init python:
    def init_language():
        """Inicializa o idioma salvo. Deve ser chamada apenas quando o jogo está rodando."""
        try:
            if hasattr(persistent, 'language') and persistent.language:
                lang = persistent.language
                if lang == "en":
                    renpy.change_language("english")
                else:
                    renpy.change_language("portuguese")
            else:
                persistent.language = "en"
                renpy.change_language("english")
        except:
            # Se houver erro, apenas define o padrão
            persistent.language = "pt"
    
    # Callback para inicializar o idioma após carregar um save
    def after_load():
        init_language()
    
    # Registrar callback para após carregar
    config.after_load_callbacks.append(after_load)