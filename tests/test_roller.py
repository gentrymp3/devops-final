from app.roller import roll_dice

def test_roll_die_range():
    rolls, total = roll_dice(6, 1)

    assert len(rolls) == 1
    assert 1 <= rolls[0] <= 6
    assert total >= 1
        