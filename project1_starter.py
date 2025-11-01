"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Caleb Smith
Date: 10/27/25
AI Usage: ChatGPT used for code structure, debugging, and documentation.
"""

# -----------------------------------
# Function: calculate_stats
# -----------------------------------
def calculate_stats(character_class, level):
    """Return tuple of (strength, magic, health) based on class and level"""
    if character_class == "Warrior":
        return (10 + level * 3, 2 + level * 1, 100 + level * 10)
    elif character_class == "Mage":
        return (3 + level * 1, 12 + level * 4, 80 + level * 8)
    elif character_class == "Rogue":
        return (6 + level * 2, 5 + level * 2, 70 + level * 7)
    elif character_class == "Cleric":
        return (5 + level * 2, 8 + level * 3, 90 + level * 9)
    else:
        return (0, 0, 0)  # fallback


# -----------------------------------
# Function: create_character
# -----------------------------------
def create_character(name, character_class_num):
    """Create a new character dictionary"""
    level = 1

    class_map = {1: "Warrior", 2: "Mage", 3: "Rogue", 4: "Cleric"}
    character_class = class_map.get(character_class_num, "Unknown")

    strength, magic, health = calculate_stats(character_class, level)

    # gold values differ by class
    gold_values = {"Warrior": 20, "Mage": 30, "Rogue": 25, "Cleric": 22}
    gold = gold_values.get(character_class, 10)

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


# -----------------------------------
# Function: save_character
# -----------------------------------
def save_character(character, filename):
    """Save character data to a text file"""
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
    except Exception as e:
        print("Error saving character:", e)
        return False


# -----------------------------------
# Function: load_character
# -----------------------------------
def load_character(filename):
    """Load a character from a text file and return as a dictionary."""
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
        print("File not found.")
        return None


# -----------------------------------
# Function: display_character
# -----------------------------------
def display_character(character):
    """Print character info"""
    print("\n=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")


# -----------------------------------
# Function: level_up
# -----------------------------------
def level_up(character):
    """Increase level and update stats"""
    if "level" not in character:
        character["level"] = 1

    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print("\nYou leveled up!")


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your character's name: ")

    while True:
        try:
            cls = int(input("Choose your class:\n1. Warrior\n2. Mage\n3. Rogue\n4. Cleric\nSelection: "))
            if cls in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Enter 1–4.")
        except ValueError:
            print("Invalid input. Enter a number 1–4.")

    player = create_character(name, cls)
    display_character(player)

    save_character(player, "my_character.txt")
    print("\nCharacter saved to file.")

    loaded = load_character("my_character.txt")
    if loaded:
        print("\nLoaded character from file:")
        display_character(loaded)
        level_up(loaded)
        display_character(loaded)
    else:
        print("Error: Could not load character.")

