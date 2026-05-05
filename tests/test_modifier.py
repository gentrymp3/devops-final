from app.roller import roll_dice

def test_modifier_addition():
    rolls = [1,1]
    modifier = 3
    total = sum(rolls) + modifier
    assert total == 5