
def test_aged_brie_quality_is_never_negative_starting_negative(update_item, fixed):
    item = update_item("Aged Brie", 10, -5)
    assert item.sell_in == 9

    expected = 1 if fixed('aged_brie') else -4
    assert item.quality == expected


def test_aged_brie_quality_is_never_over_50_starting_over_50(update_item, fixed):
    item = update_item("Aged Brie", 0, 100)
    assert item.sell_in == -1
    
    expected = 50 if fixed('aged_brie') else 100
    assert item.quality == expected


def test_aged_brie_quality_is_never_over_50_starting_over_50_past_sell_in(update_item, fixed):
    item = update_item("Aged Brie", -1, 100)
    assert item.sell_in == -2
    
    expected = 50 if fixed('aged_brie') else 100
    assert item.quality == expected