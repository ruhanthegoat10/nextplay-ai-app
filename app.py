def run_cognitive_inference(user_input):
    inp_lower = user_input.lower()
    inp_title = user_input.title()
    
    # 1. Isolate capitalized words smoothly using regex
    words = re.findall(r'\b[A-Z][a-zA-Z0-9_]+\b', inp_title)
    
    # 2. EXPANDED IGNORE LIST: Add conversational filler verbs, question words, and operators
    ignore_list = [
        "Vs", "And", "What", "The", "Analyze", "Predict", "Score", "In", 
        "Simulation", "Tactics", "Run", "Me", "Game", "Will", "Be", 
        "World", "Cup", "Transfer", "Sign", "Player", "Injury", "Injured",
        "Is", "Are", "Was", "Were", "Does", "Do", "Did", "Can", "Could", 
        "Should", "How", "Who", "Why", "When", "Where", "Playing", "Match"
    ]
    
    # Filter out the noise
    found_entities = [w for w in words if w not in ignore_list]
    
    # 3. FALLBACK SAFETY CHECK: Make sure we actually found real team names
    t1 = found_entities[0] if len(found_entities) > 0 else "The Favorites"
    t2 = found_entities[1] if len(found_entities) > 1 else "The Underdogs"
    
    # If the user only mentioned one team (e.g., "Is France playing?"), 
    # make sure Team 1 and Team 2 aren't accidentally identical or empty strings
    if t1 == t2 or t2 == "The Underdogs":
        if "france" in inp_lower: t2 = "their Group Stage Opponent"
        # Add quick custom fallbacks based on context keywords
