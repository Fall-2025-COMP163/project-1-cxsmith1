"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Caleb Smith
Date: 10/27/25

AI Usage: ChatGPT used for debugging and structure clarification.
"""

# -----------------------------------
# Function: calculate_stats
# -----------------------------------
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 10 + (level * 3)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 12 + (level * 4)
        health = 80 + (level * 8)
    elif character_class == "Rogue":
        strength = 6 + (level * 2)
        magic = 5 + (level * 2)
        health = 70 + (level * 7)
    elif character_class == "Cleric":
        strength = 5 + (level * 2)
        magic = 8 + (level * 3)
        health = 90 + (level * 9)
    else:
        strength, magic, health = 0, 0, 0

    return (strength, magic, health)


# -----------------------------------
# Function: create_character
# -----------------------------------
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys:
    name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    # assign gold based on class
    if character_class == "Warrior":
        gold = 20
    elif character_class == "Mage":
        gold = 30
    elif character_class == "Rogue":
        gold = 25
    elif character_class == "Cleric":
        gold = 22
    else:
        gold = 10

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


# -----------------------------------
# Function: save_character
# -----------------------------------
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
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


# -----------------------------------
# Function: load_character
# -----------------------------------
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        character = {}
        for line in lines:
            if ": " in line:
                key, value = line.strip().split(": ", 1)
                key = key.lower().replace("character name", "name")
                if value.isdigit():
                    value = int(value)
                character[key] = value
        return character
    except FileNotFoundError:
        return None


# -----------------------------------
# Function: display_character
# -----------------------------------
def display_character(character):
    """
    Prints formatted character sheet
    """
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# -----------------------------------
# Function: level_up
# -----------------------------------
def level_up(character):
    """
    Increases character level and recalculates stats
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health


# -----------------------------------
# MAIN PROGRAM (manual test)
# -----------------------------------
if __name__ == "__main__":
    name = input("Enter character name: ")
    cls = input("Enter class (Warrior/Mage/Rogue/Cleric): ")

    char = create_character(name, cls)
    display_character(char)

    save_character(char, "my_character.txt")

    loaded = load_character("my_character.txt")
    if loaded:
        print("\nLoaded character:")
        display_character(loaded)
        level_up(loaded)
        print("\nAfter leveling up:")
        display_character(loaded)
    else:
        print("File not found.")


