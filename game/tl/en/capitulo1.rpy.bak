# English Translation - Chapter 1
# Tradução em inglês - Capítulo 1

translate english capitulo1:
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === INTRODUCTION WITH PROFESSOR WENDELL'S MONOLOGUE ===
    # Play campus background music
    play music campus_ambient fadein 2.0
    
    scene bg auditorium with fade

    narrator "The Solária College auditorium was filled with anticipation. Dozens of young people, each carrying unique dreams, awaited the beginning of a journey that would change their lives forever."

    narrator "Among them, I sat in the middle rows, trying to absorb every detail of this historic moment. The air was charged with infinite possibilities."

    # Professor Wendell - Monologue about college and life phase
    show professor_wendell neutral at center
    professor_wendell "Welcome to Solária College, bright young minds. You are about to embark on one of the most transformative journeys of your lives."
    professor_wendell "The university is not just a place of academic learning, but a laboratory of personal discoveries, human connections, and inner growth."
    professor_wendell "Each of you brings with you unique dreams, distinct perspectives, and unlimited potential. Here, you will not only study, but discover who you really are."
    professor_wendell "The friendships you will form here, the challenges you will face, the passions you will discover... all of this will shape not only your professional futures, but your souls."
    professor_wendell "Do not be afraid to explore, to question, to connect with people different from you. It is in diversity that we find our true strength."
    professor_wendell "Now, go out and explore this campus. Let life surprise you with the incredible people you are about to meet."
    hide professor_wendell
    
    narrator "Professor Wendell's words echoed in my mind as I walked through the campus. I felt that something special was about to happen."
    narrator "Every corridor, every garden, every building seemed to pulse with infinite possibilities. It was as if the campus itself was waiting to reveal its secrets to me."

    # === CAMPUS EXPLORATION ===
    narrator "As I explored the campus, I realized there were several interesting areas to discover. Where should I begin my journey of discoveries?"
    
    # Initialize control variables
    $ events_completed = []
    
    # === FIRST CHOICE - CAMPUS EXPLORATION ===
    menu:
        "Go to the library and study center":
            $ add_shared_memory("library_exploration", [], "First exploration of the campus library")
            call evento_nicole_camille
            $ events_completed.append("library")
            jump capitulo1_continue_exploration
            
        "Go to the university cinema":
            $ add_shared_memory("cinema_exploration", [], "First exploration of the university cinema")
            call evento_katia_samantha
            $ events_completed.append("cinema")
            jump capitulo1_continue_exploration
            
        "Visit the sports court and recreation areas":
            $ add_shared_memory("sports_exploration", [], "First exploration of the sports areas")
            call evento_larissa_huey
            $ events_completed.append("sports")
            jump capitulo1_continue_exploration

