from tests.settings import *

#  'every': "- At the end of each day our system lowers both values for every item",

def test_aged_brie_gets_better():
    item = Item("Aged Brie", 10, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 11

def test_aged_brie_gets_better_one_before_sell_in():
    item = Item("Aged Brie", 1, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 31

def test_aged_brie_gets_better_at_sell_in():
    item = Item("Aged Brie", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 50

def test_aged_brie_gets_better_faster_after_sell_in():
    item = Item("Aged Brie", -1, 22)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 24

def test_aged_brie_quality_is_never_negative():
    item = Item("Aged Brie", 99, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 98
    assert item.quality == 1

def test_aged_brie_quality_is_never_negative_past_sell_in():
    item = Item("Aged Brie", 0, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 2

@pytest.mark.xfail(characterization_mode, reason = "bug in original")
def test_aged_brie_quality_is_never_negative_starting_negative_bug():
    item = Item("Aged Brie", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == -4

@pytest.mark.xfail(bugfix_mode, reason = "fixed value")
def test_aged_brie_quality_is_never_negative_starting_negative_fixed():
    item = Item("Aged Brie", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 1

def test_aged_brie_quality_is_never_over_50_from_49():
    item = Item("Aged Brie", 6, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 50

def test_aged_brie_quality_is_never_over_50_from_50():
    item = Item("Aged Brie", 6, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 50

def test_aged_brie_quality_is_never_over_50_from_49_at_sell_in():
    item = Item("Aged Brie", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 50

def test_aged_brie_quality_is_never_over_50_from_50_at_sell_in():
    item = Item("Aged Brie", 0, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_49_past_sell_in():
    item = Item("Aged Brie", -1, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 50

def test_aged_brie_quality_is_never_over_50_from_50_past_sell_in():
    item = Item("Aged Brie", -1, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 50

@pytest.mark.xfail(characterization_mode, reason = "bug in original")
def test_aged_brie_quality_is_never_over_50_starting_over_50_bug():
    item = Item("Aged Brie", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 100

@pytest.mark.xfail(bugfix_mode, reason = "fixed value")
def test_aged_brie_quality_is_never_over_50_starting_over_50_fixed():
    item = Item("Aged Brie", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 50

@pytest.mark.xfail(characterization_mode, reason = "bug in original")
def test_aged_brie_quality_is_never_over_50_starting_over_50_past_sell_in_bug():
    item = Item("Aged Brie", -1, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 100

@pytest.mark.xfail(bugfix_mode, reason = "fixed value")
def test_aged_brie_quality_is_never_over_50_starting_over_50_past_sell_in_fixed():
    item = Item("Aged Brie", -1, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 50

