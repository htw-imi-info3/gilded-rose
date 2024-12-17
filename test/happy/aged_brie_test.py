
#  'every': "- At the end of each day our system lowers both values for every item",


def test_aged_brie_gets_better(update_item):
    item = update_item("Aged Brie", 10, 10)
    assert item.sell_in == 9
    assert item.quality == 11


def test_aged_brie_gets_better_one_before_sell_in(update_item):
    item = update_item("Aged Brie", 1, 30)
    assert item.sell_in == 0
    assert item.quality == 31


def test_aged_brie_gets_better_at_sell_in(update_item):
    item = update_item("Aged Brie", 0, 49)
    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_gets_better_faster_after_sell_in(update_item):
    item = update_item("Aged Brie", -1, 22)
    assert item.sell_in == -2
    assert item.quality == 24


def test_aged_brie_quality_is_never_negative(update_item):
    item = update_item("Aged Brie", 99, 0)
    assert item.sell_in == 98
    assert item.quality == 1


def test_aged_brie_quality_is_never_negative_past_sell_in(update_item):
    item = update_item("Aged Brie", 0, 0)
    assert item.sell_in == -1
    assert item.quality == 2





def test_aged_brie_quality_is_never_over_50_from_49(update_item):
    item = update_item("Aged Brie", 6, 49)
    assert item.sell_in == 5
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50(update_item):
    item = update_item("Aged Brie", 6, 50)
    assert item.sell_in == 5
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_49_at_sell_in(update_item):
    item = update_item("Aged Brie", 0, 49)

    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50_at_sell_in(update_item):
    item = update_item("Aged Brie", 0, 50)

    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_49_past_sell_in(update_item):
    item = update_item("Aged Brie", -1, 49)

    assert item.sell_in == -2
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50_past_sell_in(update_item):
    item = update_item("Aged Brie", -1, 50)

    assert item.sell_in == -2
    assert item.quality == 50

