"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Caleb Smith]
Date: [10/27/25]

AI Usage: [Document any AI assistance used]
"""

def create_character(name, character_class):


    if character_class == "Warrior":
        strength = 10 + (level * 3)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 12 + (level * 4)
        health = 80 + (level * 6)
    elif character_class == "Rogue":
        strength = 6 + (level * 2)
        magic = 6 + (level * 2)
        health = 70 + (level * 5)
    elif character_class == "Cleric":
        strength = 5 + (level * 2)
        magic = 10 + (level * 3)
        health = 90 + (level * 8)

    # send back all three numbers
    return (strength, magic, health)




    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

def calculate_stats(character_class, level):
    strength, magic, health = calculate_stats(character_class, 1)

    # give each class a little bit of different gold
    if character_class == "Warrior":
        gold = 15
    elif character_class == "Mage":
        gold = 30
    elif character_class == "Rogue":
        gold = 25
    elif character_class == "Cleric":
        gold = 20

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character

    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    

def save_character(character, filename):
    try:
        with open(filename, "w") as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
        return True
    except:
        return False
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
     try:
        with open(filename, "r") as f:
            lines = f.readlines()

        character = {}
        for line in lines:
            line = line.strip()
            if ": " in line:
                key, value = line.split(": ", 1)
                key = key.lower().replace("character name", "name")

                # convert numbers to integers if possible
                if value.isdigit():
                    value = int(value)

                character[key] = value

        return character
    
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
     print("\n=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
     name = input("Enter your character's name: ")

    # show menu and make sure input is valid
    while True:
        choice = input(
            "\nChoose your class:\n1. Warrior\n2. Mage\n3. Rogue\n4. Cleric\nSelection: "
        )

        if choice == "1":
            character_class = "Warrior"
        elif choice == "2":
            character_class = "Mage"
        elif choice == "3":
            character_class = "Rogue"
        elif choice == "4":
            character_class = "Cleric"
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue
        break

    # create and show the character
    player = create_character(name, character_class)
    display_character(player)

    # save to file
    save_character(player, "my_character.txt")
    print("\nCharacter saved to my_character.txt!")

    # load and show it again
    loaded = load_character("my_character.txt")
    if loaded:
        print("\nLoaded character:")
        display_character(loaded)

        print("\nLeveling up...")
        level_up(loaded)
        display_character(loaded)

    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
