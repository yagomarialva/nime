define sombra = Character("Narrator", color="#A9A9A9")  # Mysterious and shadowed character

label prologo:

    scene bg city with fade  # Replace with your real image

    sombra "This game is recommended for ages 18 and up."
    sombra "Do you confirm that you are 18 years old or older?"

    menu:
        "Yes, I am 18 years old or older.":
            jump nome_jogador

        "No, I am underage.":
            sombra "Unfortunately, you will not be able to play this game. Thank you for your understanding!"
            return

label nome_jogador:
    scene bg city with fade

    $ nome = renpy.input("Enter your name:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Player"

    sombra "Hello, [nome]. Welcome!"

    jump aviso_jogo

label aviso_jogo:
    scene bg city with fade
    with dissolve

    sombra "All characters in this game are 18 years old or older."
    sombra "Although it addresses mature relationships and themes, this is NOT a pornographic game."
    sombra "Our focus is on narrative construction, romance, and choices with consequences."
    sombra "We hope you enjoy your journey with responsibility and respect."

    jump tutorial_mecanicas

label tutorial_mecanicas:
    scene bg city with dissolve
    
    sombra "Before you begin your journey, [nome], let me explain how this world works..."
    sombra "NIME is not just a story - it's an experience where your choices shape real relationships."
    
    menu:
        "I want to learn about the game mechanics":
            jump explicar_mecanicas
        "I prefer to discover by playing":
            sombra "I understand! Sometimes discovery is part of the fun."
            sombra "But remember: in the top left corner you can always see how your relationships are evolving."
            jump iniciar_aventura

label explicar_mecanicas:
    scene bg city with dissolve
    
    # === RELATIONSHIP SYSTEM EXPLANATION ===
    sombra "🏠 Welcome to NIME's relationship system!"
    sombra "You will meet 6 unique characters, each with their own personality, dreams, and vulnerabilities."
    
    sombra "💕 In the top left corner, you'll see RELATIONSHIP LEVELS:"
    sombra "🤝 Stranger → 🙂 Friend → 😊 Close Friend → 💖 Romantic"
    
    sombra "Each positive interaction strengthens your bonds. Each special moment creates lasting memories."
    
    # === CHOICE EXPLANATION ===
    sombra "🎯 Your CHOICES have real consequences:"
    sombra "• Some increase affinity with specific characters"
    sombra "• Others affect multiple relationships"
    sombra "• Special moments unlock when you show genuine empathy"
    
    sombra "🌱 Your EMPATHY LEVEL also matters - the more you care about others, the more special opportunities arise."
    
    # === SPECIAL MOMENTS EXPLANATION ===
    sombra "✨ SPECIAL MOMENTS happen when true connections form:"
    sombra "• Deep conversations that reveal vulnerabilities"
    sombra "• Shared experiences that become precious memories"
    sombra "• Realizations about love, friendship, and personal growth"
    
    sombra "📚 Your SHARED MEMORIES are recorded - each one represents a unique moment you created."
    
    # === GROWTH EXPLANATION ===
    sombra "🌟 But here's the most important thing:"
    sombra "This is not a game about 'conquering' someone. It's about mutual growth."
    sombra "Each character has their own journey of self-discovery."
    sombra "Your actions not only affect how they feel about you - but how they grow as people."
    
    # === ENDINGS EXPLANATION ===
    sombra "🎭 There are multiple paths for your story:"
    sombra "• Deep friendships that last a lifetime"
    sombra "• Romantic relationships based on genuine connection"
    sombra "• Personal growth that transforms you as a person"
    sombra "• Memories that will stay with you forever"
    
    sombra "The choice is yours, [nome]. What kind of story will you create?"
    
    jump iniciar_aventura

label iniciar_aventura:
    scene bg city with dissolve
    
    sombra "🌟 Your journey at Solária College is about to begin, [nome]."
    sombra "You will meet:"
    sombra "💼 Nicole - The strategist who dreams of helping artists"
    sombra "🎬 Katia - The filmmaker who sees art in shadows"  
    sombra "🏐 Larissa - The athlete who finds peace in movement"
    sombra "🎨 Huey - The artist who sees magic in everything"
    sombra "🎮 Samantha - The gamer who lives in fantasy worlds"
    sombra "🧘 Camille - The spiritualist who feels the energies of the universe"
    
    sombra "Each one has their dreams, fears, and a unique story to tell."
    sombra "But most importantly: each one can change, grow, and flourish..."
    sombra "...depending on how you choose to connect with them."
    
    sombra "💫 What kind of story will you create together?"
    sombra "That, my dear [nome], depends entirely on you."
    
    sombra "🏠 Welcome to Aurora Street, 57."
    sombra "Your new home. Your new family. Your new life."
    
    # Epic transition to the first chapter
    scene black with fade
    centered "{color=#FFD700}🌟 Your journey of human connections begins now... 🌟{/color}"
    pause 2.0

    jump capitulo1
