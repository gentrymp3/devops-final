from app.roller import roll_dice

def test_modifier_addition():
    rolls, total = roll_dice(1, 2, 3)
    assert total == 5