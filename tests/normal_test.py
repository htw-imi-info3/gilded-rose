from tests.settings import *


# create tests for normal items here...

def test_something():
    item = Item("Normal Item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19


def test_normal_items_zero_quality():
    normal_item = Item("Normal Item", 5, 0)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == 4
    assert normal_item.quality == 0


def test_normal_items_after_sell():
    normal_item = Item("Normal Item", -1, 10)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == -2
    assert normal_item.quality == 8


def test_normal_items_after_sell_zero_quality():
    normal_item = Item("Normal Item", -1, 0)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == -2
    assert normal_item.quality == 0
