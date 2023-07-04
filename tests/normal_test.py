from tests.settings import *

# create tests for normal items here...

def test_something():
    item = Item("normal with any name", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19



def test_normal_reduces_both():
    item = Item("normal with any name", 10, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 9

def test_normal_reduces_both_at_sell_in():
    item = Item("normal with any name", 1, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 29

def test_normal_degrades_faster_after_sell_in():
    item = Item("normal with any name", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 47

def test_normal_quality_is_never_negative():
    item = Item("normal with any name", 99, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 98
    assert item.quality == 0

def test_normal_quality_is_never_negative_past_sell_in():
    item = Item("normal with any name", 0, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_normal_quality_is_never_negative_starting_negative_fails():
    item = Item("normal with any name", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == -5

@pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
def test_normal_quality_is_never_negative_starting_negative_fixed():
    item = Item("normal with any name", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 0

def test_normal_quality_is_never_over_50_from_50():
    item = Item("normal with any name", 6, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 49

@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_normal_quality_is_never_over_50_from_49_at_sell_in():
    item = Item("normal with any name", 0, 51)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 49
    
@pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
def test_normal_quality_is_never_over_50_from_49_at_sell_in():
    item = Item("normal with any name", 0, 51)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 48

@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_normal_quality_is_never_over_50_starting_over_50_bug():
    item = Item("normal with any name", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 98

@pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
def test_normal_quality_is_never_over_50_starting_over_50_fixed():
    item = Item("normal with any name", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 48

# these are not bugs after all, quality is set back to 0:
def test_failed_characterization_test_2():
    item = Item("normal with any name", -2, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == -3
    assert item.quality == 0

def test_failed_characterization_test_1():
    item = Item("normal with any name", -1, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 0

def test_failed_characterization_test_0():
    item = Item("normal with any name", 0, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

