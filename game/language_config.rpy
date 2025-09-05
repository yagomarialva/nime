# Sistema de Idiomas Simples - NIME
# Configuração básica para português e inglês

# Definir variável persistente
default persistent.language = "pt"

init python:
    # Configuração de idiomas disponíveis
    available_languages = {
        "pt": "Português",
        "en": "English"
    }
    
    # Idioma padrão
    default_language = "pt"
    
    # Função para trocar idioma
    def change_language(lang):
        if lang in available_languages:
            if lang == "en":
                renpy.change_language("english")
            else:
                renpy.change_language("portuguese")
            persistent.language = lang
            renpy.restart_interaction()
    
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