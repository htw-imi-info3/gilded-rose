from tests.settings import *

#"Sulfuras", being a legendary item, never has to be sold or decreases in Quality
#Just for clarification, an item can never have its Quality increase above 50,
#however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.

def test_sulfuras_quality_never_decreases():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.quality == 80

def test_sulfuras_sellin_never_decreases():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.sell_in == 5

def test_sulfuras_quality_never_increases():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.quality == 80

def test_sulfuras_quality_never_changes():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.quality == 80

def test_sulfuras_sellin_never_changes():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.sell_in == 0

def test_sulfuras_quality_never_changes_negative_sellin():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.quality == 80