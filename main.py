from app.roller import roll_dice

DICE = {
    "1": 4,
    "2": 6,
    "3": 8,
    "4": 10,
    "5": 12,
    "6": 20,
    "7": 100
}

def menu():
    print("\n ~ DICE ROLLER ~")
    print("1. d4")
    print("2. d6")
    print("3. d8")
    print("4. d10")
    print("5. d12")
    print("6. d20")
    print("7. d100")
    print("Enter Q to quit")

while True:
    menu()
    choice = input("Pick your poison: ")

    if choice == "Q":
        print("Closing menu...")
        break

    if choice not in DICE:
        print("Invalid choice")
        continue
    
    try:
        count = int(input("How many dice? "))
    except ValueError:
        print("Invalid number.")
        continue

    mod_input = input("Add Modifier: (3, -2, etc. Enter 0 for none)")
    
    try:
        modifier = int(mod_input) if mod_input else 0
    except ValueError:
        print("Invalid modifier.")
        continue

    rolls, total = roll_dice(DICE[choice], count, modifier)

    sign = "+" if modifier >= 0 else ""

    print("\nRolls:", rolls)
    print("Modifier:", modifier)
    print("Total:", total, "\n")