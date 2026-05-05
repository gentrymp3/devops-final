import random

def roll_die(sides: int) -> int:
    return random.randint(1, sides)

def roll_dice(sides: int, count: int, modifier: int = 0):
    rolls = [roll_die(sides) for _ in range(count)]
    total = sum(rolls) + modifier
    return rolls, total