# sistemas_melhorados.rpy - SISTEMAS BASEADOS NOS SUCESSOS DO GÊNERO

# === FUNÇÕES DO SISTEMA DE RELACIONAMENTO ORGÂNICO ===
init python:
    def update_relationship_level(character):
        """Atualiza o nível de relacionamento baseado nos pontos de afinidade"""
        points = globals().get(f"points_{character}", 0)
        
        if points >= 80:
            globals()[f"relationship_{character}"] = "romantic"
        elif points >= 60:
            globals()[f"relationship_{character}"] = "close_friend"
        elif points >= 30:
            globals()[f"relationship_{character}"] = "friend"
        elif points >= 10:
            globals()[f"relationship_{character}"] = "acquaintance"
        else:
            globals()[f"relationship_{character}"] = "stranger"
    
    def add_affinity_points(character, points, reason=""):
        """Adiciona pontos de afinidade com feedback visual e emocional"""
        old_points = globals().get(f"points_{character}", 0)
        globals()[f"points_{character}"] = min(100, old_points + points)
        update_relationship_level(character)
        
        # Aumenta empatia do jogador
        if points > 0:
            globals()["player_empathy_level"] = min(100, globals().get("player_empathy_level", 0) + 1)
        
        # Mensagem de feedback (inspirado em jogos de sucesso)
        if points > 0:
            relationship = globals()[f"relationship_{character}"]
            if relationship == "romantic":
                return f"💕 {character.title()} se sente muito próxima de você"
            elif relationship == "close_friend":
                return f"😊 Sua amizade com {character.title()} se fortaleceu"
            elif relationship == "friend":
                return f"🙂 {character.title()} gosta mais de você"
            else:
                return f"✨ {character.title()} se sente mais confortável com você"
        return ""
    
    def add_shared_memory(memory_key, characters_involved, description):
        """Adiciona uma memória compartilhada significativa"""
        memory = {
            "key": memory_key,
            "characters": characters_involved,
            "description": description,
            "chapter": len(persistent.unlocked_chapters)
        }
        shared_memories.append(memory)
    
    def unlock_emotional_moment(moment_key, description):
        """Desbloqueia um momento emocional especial (sistema nakige)"""
        moment = {
            "key": moment_key,
            "description": description,
            "chapter": len(persistent.unlocked_chapters)
        }
        emotional_moments_unlocked.append(moment)
    
    def trigger_character_growth(character, growth_aspect):
        """Dispara crescimento pessoal de um personagem"""
        current_growth = globals().get(f"character_growth_{character}", 0)
        globals()[f"character_growth_{character}"] = min(100, current_growth + 20)
        
        # Retorna texto de crescimento baseado no aspecto
        growth_texts = {
            "confidence": f"{character.title()} parece mais confiante em si mesma",
            "empathy": f"{character.title()} mostra mais compreensão pelos outros",
            "courage": f"{character.title()} demonstra mais coragem para enfrentar seus medos",
            "wisdom": f"{character.title()} ganha uma perspectiva mais madura sobre a vida",
            "communication": f"{character.title()} se expressa de forma mais clara e honesta"
        }
        return growth_texts.get(growth_aspect, f"{character.title()} cresceu como pessoa")

# === FUNÇÕES PARA ESCOLHAS MAIS SIGNIFICATIVAS ===
label choice_with_consequences(choice_text, character_affected, points_change, growth_aspect=None):
    """Label para escolhas que têm consequências emocionais reais"""
    $ feedback = add_affinity_points(character_affected, points_change)
    
    if growth_aspect and points_change > 0:
        $ growth_feedback = trigger_character_growth(character_affected, growth_aspect)
        narrator "[growth_feedback]"
    
    if feedback:
        narrator "[feedback]"
    
    return

# === SISTEMA DE DIÁLOGOS CONTEXTUAL ===
init python:
    def get_contextual_dialogue(character, context="normal"):
        """Retorna diálogos baseados no nível de relacionamento atual"""
        relationship = globals().get(f"relationship_{character}", "stranger")
        
        # Diálogos mais personalizados baseados no relacionamento
        dialogue_sets = {
            "stranger": {
                "greeting": f"Oi... {character} aqui.",
                "casual": f"Hmm, tudo bem, eu acho.",
                "intimate": f"Desculpa, ainda não nos conhecemos bem..."
            },
            "acquaintance": {
                "greeting": f"Oi! Como você está?",
                "casual": f"Você é bem legal, sabia?",
                "intimate": f"Eu... ainda estou te conhecendo melhor."
            },
            "friend": {
                "greeting": f"Ei! Que bom te ver!",
                "casual": f"Gosto de conversar com você.",
                "intimate": f"Posso te contar algo pessoal?"
            },
            "close_friend": {
                "greeting": f"Oi! Estava esperando você aparecer!",
                "casual": f"Você sempre sabe o que dizer...",
                "intimate": f"Você é realmente especial para mim."
            },
            "romantic": {
                "greeting": f"Oi... fico feliz sempre que te vejo.",
                "casual": f"Cada momento contigo é especial.",
                "intimate": f"Meu coração acelera quando estou perto de você..."
            }
        }
        
        return dialogue_sets.get(relationship, dialogue_sets["stranger"]).get(context, "...")

# === SISTEMA DE MOMENTOS NAKIGE ===
label emotional_moment(moment_type, character=None, description=""):
    """Cria momentos genuinamente emocionantes (técnica nakige)"""
    
    if moment_type == "vulnerability":
        scene bg bedroom with dissolve
        $ unlock_emotional_moment(f"vulnerability_{character}", description)
        narrator "A atmosfera fica mais íntima, e você sente que algo importante está prestes a ser compartilhado..."
        
    elif moment_type == "farewell":
        scene bg sunset with dissolve  
        $ unlock_emotional_moment("farewell", description)
        narrator "O por do sol pinta o céu de dourado, e você sente o peso da despedida se aproximando..."
        
    elif moment_type == "realization":
        $ unlock_emotional_moment("realization", description)
        narrator "De repente, tudo faz sentido. Os sentimentos que estavam confusos agora são claros como cristal..."
    
    # Aumenta empatia do jogador em momentos especiais
    $ player_empathy_level = min(100, player_empathy_level + 5)
    
    return

# === ESCOLHAS MAIS PROFUNDAS E SIGNIFICATIVAS ===
label meaningful_choice(question, option1, option2, character1, character2, points1, points2):
    """Sistema de escolhas que realmente importam para o desenvolvimento"""
    
    menu:
        "[question]"
        
        "[option1]":
            call choice_with_consequences("", character1, points1) from _call_choice_with_consequences_1
            
        "[option2]":
            call choice_with_consequences("", character2, points2) from _call_choice_with_consequences_2
    
    return

# === SISTEMA DE PROGRESSÃO POR PONTOS (ESTILO "5 CORAÇÕES") ===
init python:
    def get_total_affinity_points():
        """Calcula o total de pontos de afinidade de todas as personagens"""
        characters = ["samantha", "katia", "nicole", "larissa", "huey", "camille"]
        total = 0
        for char in characters:
            total += globals().get(f"points_{char}", 0)
        return total
    
    def check_chapter_progression_requirement(chapter_number):
        """Verifica se o jogador tem pontos suficientes para progredir para o próximo capítulo"""
        total_points = get_total_affinity_points()
        required_points = chapter_number * 30  # 30 pontos por capítulo
        
        if total_points >= required_points:
            return True, f"Você tem {total_points} pontos de afinidade total. Requisito para o Capítulo {chapter_number + 1}: {required_points} pontos."
        else:
            missing = required_points - total_points
            return False, f"Você tem {total_points} pontos de afinidade total. Precisa de mais {missing} pontos para progredir para o Capítulo {chapter_number + 1}."
    
    def get_relationship_summary():
        """Retorna um resumo dos relacionamentos atuais"""
        characters = ["samantha", "katia", "nicole", "larissa", "huey", "camille"]
        summary = []
        
        for char in characters:
            points = globals().get(f"points_{char}", 0)
            relationship = globals().get(f"relationship_{char}", "stranger")
            
            # Emojis para cada nível
            if relationship == "romantic":
                emoji = "💕"
            elif relationship == "close_friend":
                emoji = "😊"
            elif relationship == "friend":
                emoji = "🙂"
            elif relationship == "acquaintance":
                emoji = "🤝"
            else:
                emoji = "👋"
            
            summary.append(f"{emoji} {char.title()}: {points} pontos ({relationship.replace('_', ' ')})")
        
        return summary