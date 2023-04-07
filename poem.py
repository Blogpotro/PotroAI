import random

# Lists of adjectives, nouns, verbs, and adverbs
adjectives = ["mysterious", "majestic", "tranquil", "serene", "elegant", "magnificent", "enchanting", "romantic", "picturesque", "delightful"]
nouns = ["moon", "stars", "ocean", "forest", "mountain", "meadow", "sun", "sky", "river", "breeze"]
verbs = ["dance", "sing", "whisper", "embrace", "wander", "gaze", "sparkle", "glimmer", "illuminate", "dazzle"]
adverbs = ["gracefully", "silently", "peacefully", "tenderly", "sensually", "softly", "delicately", "magically", "beautifully", "harmoniously"]

# Lists of phrases from famous poems
phrases = ["Do not go gentle into that good night", "I wandered lonely as a cloud", "The woods are lovely, dark and deep", "Hope is the thing with feathers", "Because I could not stop for Death", "She walks in beauty, like the night", "Shall I compare thee to a summer's day?", "To be or not to be, that is the question", "All the world's a stage", "Water, water, everywhere, And all the boards did shrink"]

def generate_poem():
    # Randomly select 3 adjectives, 3 nouns, 2 verbs, and 2 adverbs
    selected_adjectives = random.sample(adjectives, 3)
    selected_nouns = random.sample(nouns, 3)
    selected_verbs = random.sample(verbs, 2)
    selected_adverbs = random.sample(adverbs, 2)
    
    # Randomly select a phrase from the list of phrases
    selected_phrase = random.choice(phrases)
    
    # Combine the parts of speech and phrase to create a poem
    poem = f"{selected_adjectives[0].title()} {selected_nouns[0]} {selected_verbs[0]} {selected_adverbs[0]},\n{selected_adjectives[1].title()} {selected_nouns[1]} {selected_verbs[1]} {selected_adverbs[1]},\n{selected_adjectives[2].title()} {selected_nouns[2]} {selected_phrase}."
    
    return poem

