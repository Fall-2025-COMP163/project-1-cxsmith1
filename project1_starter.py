"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Caleb Smith
Date: 10/27/25

AI Usage: Not gonna lie, used a lot of AI on this one because I was confused on exactly what was asked for by the autograder.
Used for tuple function, as well as level up function.
"""

def create_character(name, character_class):
    level = 1  # every new character starts at level 1

    stats = {
        "name": name,
        "level": level,
    }

    #base stats for each class
    if character_class == 1:
        stats["class"] = "Warrior"
        stats["strength"] = 10 + (level * 3)
        stats["magic"] = 2 + (level * 1)
        stats["health"] = 100 + (level * 10)
        stats["gold"] = 20
    elif character_class == 2:
        stats["class"] = "Mage"
        stats["strength"] = 3 + (level * 1)
        stats["magic"] = 12 + (level * 4)
        stats["health"] = 80 + (level * 8)
        stats["gold"] = 30
    elif character_class == 3:
        stats["class"] = "Rogue"
        stats["strength"] = 6 + (level * 2)
        stats["magic"] = 5 + (level * 2)
        stats["health"] = 70 + (level * 7)
        stats["gold"] = 25
    elif character_class == 4:
        stats["class"] = "Cleric"
        stats["strength"] = 5 + (level * 2)
        stats["magic"] = 8 + (level * 3)
        stats["health"] = 90 + (level * 9)
        stats["gold"] = 22

    return stats


def calculate_stats(character_class, level):
    """Calculates base stats based on class and level and returns a tuple."""
    if character_class == "Warrior":
        strength = 10 + level * 3
        magic = 2 + level * 1
        health = 100 + level * 10
    elif character_class == "Mage":
        strength = 3 + level * 1
        magic = 12 + level * 4
        health = 80 + level * 8
    elif character_class == "Rogue":
        strength = 6 + level * 2
        magic = 5 + level * 2
        health = 70 + level * 7
    elif character_class == "Cleric":
        strength = 5 + level * 2
        magic = 8 + level * 3
        health = 90 + level * 9
    else:
        raise ValueError("Invalid character class.")

    return strength, magic, health


def save_character(character, filename):
    """Save a character dictionary to a text file."""
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


def load_character(filename):
    """Load a character from a text file and return as a dictionary."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        character = {}
        for line in lines:
            line = line.strip()
            if ": " in line:
                key, value = line.split(": ", 1)
                key = key.lower().replace("character name", "name")
                if value.isdigit():
                    value = int(value)
                character[key] = value

        return character
    except FileNotFoundError:
        print("File not found.")
        return None


def display_character(character):
    """Print a formatted character sheet."""
    print("\n=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")


def level_up(character):
    """Increase character level by 1 and recalculate stats."""
    if "level" not in character:
        character["level"] = 1  # Default if missing

    character["level"] += 1
    # Recalculate stats using calculate_stats
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up to level {character['level']}!")



if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your character's name: ")

    # Keep asking until user picks 1–4
    while True:
        try:
            character_class = int(input(
                "Choose your class:\n1. Warrior\n2. Mage\n3. Rogue\n4. Cleric\nSelection: "
            ))
            if character_class in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Enter 1-4.")
        except ValueError:
            print("Invalid input. Enter a number 1-4.")

    # Create character
    player = create_character(name, character_class)

    # Display the new character
    display_character(player)

    # Save character to file
    save_character(player, "my_character.txt")

    # Load character from file
    loaded = load_character("my_character.txt") 
    if loaded:  # Only proceed if loading succeeded
        print("\nLoaded character from file:")
        display_character(loaded)

        # Level up 
        if "level" not in loaded:
            loaded["level"] = 1  # default if missing
        level_up(loaded)
        display_character(loaded)
    else:
        print("Could not load character from file.")
