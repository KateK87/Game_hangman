import random

characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
hidden_character = []

# Generování náhodného slova
random_character = characters[random.randint(0, len(characters)-1)]

# Generování podtržítek
for one_letter in random_character:
    hidden_character.append("_")
    
guess = input("Zadejte hádané písmeno")