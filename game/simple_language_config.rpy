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