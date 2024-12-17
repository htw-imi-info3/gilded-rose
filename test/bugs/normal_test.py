
# The specification says "an item quality is never negative"
# and "an item quality is never more than 50"

# these characterization tests show how the original version
# behaves if the item quality is set to <0 or >50 before
# calling update quality.


def test_normal_quality_is_never_negative_starting_negative(update_item, fixed):
    item = update_item("normal with any name", 10, -5)
    assert item.sell_in == 9
    expected = 0 if fixed('normal') else -5
    assert item.quality == expected


def test_normal_quality_is_never_over_50_from_49_at_sell_in(update_item, fixed):
    item = update_item("normal with any name", 0, 51)
    assert item.sell_in == -1
    expected = 48 if fixed('normal') else 49
    
    assert item.quality == expected

# THESE TWO, however, are clearly bugs as the quality
# is > 50 after update_item is called!


def test_normal_quality_is_never_over_50_starting_over_50(update_item, fixed):
    item = update_item("normal with any name", 0, 100)
    assert item.sell_in == -1

    expected = 48 if fixed('normal') else 98
    assert item.quality == expected

def test_normal_quality_is_never_over_50_from_100(update_item, fixed):
    item = update_item("normal with any name", 5, 100)
    assert item.sell_in == 4

    expected = 49 if fixed('normal') else 99
    assert item.quality == expected