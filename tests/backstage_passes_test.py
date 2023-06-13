from tests.settings import *

'''
- All items have a SellIn value which denotes the number of days we have to sell the item
- All items have a Quality value which denotes how valuable the item is

- The Quality of an item is never negative
- "Aged Brie" actually increases in Quality the older it gets
- The Quality of an item is never more than 50
- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert
'''


def test_backstage_passes_sellin_decreases_by_one_as_day_updates():
    """All items have a SellIn value which denotes the number of days we have to sell the item"""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4


def test_backstage_passes_quality_increases_by_one_as_sellin_approaches():
    """"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;"""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 21


def test_backstage_passes_quality_increases_by_two_ten_days_before_sellin():
    """Quality increases by 2 when there are 10 days or less..."""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 22


def test_backstage_passes_quality_increases_by_three_five_days_before_sellin():
    """...and by 3 when there are 5 days or less but..."""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 23


def test_backstage_passes_quality_drops_to_zero_after_sellin():
    """...Quality drops to 0 after the concert"""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0


def test_backstage_passes_quality_never_negative():
    """The Quality of an item is never negative"""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.quality >= 0

def test_backstage_passes_quality_never_greater_than_fifty():
    """The Quality of an item is never more than 50"""
    item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.quality <= 50