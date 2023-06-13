from tests.settings import *


# create tests for normal items here...
#	- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
#	Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
#	Quality drops to 0 after the concert


def test_backstage_passes_quality_increases_as_sellin_value_approaches():
    item = Item("name item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 11


def test_backstage_passes_quality_increases_by_one_as_sellin_approaches():
    pass


def test_backstage_passes_quality_increases_by_two_ten_days_before_sellin():
    pass


def test_backstage_passes_quality_increases_by_three_five_days_before_sellin():
    pass


def test_backstage_passes_quality_drops_to_zero_after_sellin():
    pass


def test_backstage_passes_quality_never_negative():
    pass
