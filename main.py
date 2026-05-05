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

def roll_die(sides, count):
    rolls = [roll_dice(sides) for _ in range(count)]
    return rolls, sum(rolls)

while True:
    menu()
    choice = input("Pick your poison: ")
    if choice == "Q":
        break
    if choice not in DICE:
        print("Invalid choice")
        continue

    count = int(input("How many dice? "))
    rolls, total = roll_dice(DICE[choice], count)

    print("Rolls:", rolls)
    print("Total:", total)