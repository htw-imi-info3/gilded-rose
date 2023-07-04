from tests.settings import *

# - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
# 	Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
# 	Quality drops to 0 after the concert

def test_backstage_pass_gets_better_11():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 11

def test_backstage_pass_gets_better_by_2_at_10():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 12

def test_backstage_pass_gets_better_by_2_at_6():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 12

def test_backstage_pass_gets_better_by_3_at_5():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 13

def test_backstage_pass_gets_better_by_3_at_4():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 3
    assert item.quality == 13

def test_backstage_pass_gets_better_one_before_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 33

def test_backstage_pass_is_useless_at_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

def test_backstage_pass_is_useless_after_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 22)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 0

@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_backstage_pass_quality_is_never_negative_starting_negative_fails():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == -3

@pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
def test_backstage_pass_quality_is_never_negative_starting_negative_fixed():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 2

def test_backstage_pass_quality_is_never_over_50_from_49():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_50():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_49_at_3():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 2
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_50_at_3():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 2
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_49_at_12():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 11
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_50_at_12():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 11
    assert item.quality == 50


def test_backstage_pass_quality_is_never_over_50_from_49_at_7():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 6
    assert item.quality == 50

def test_backstage_pass_quality_is_never_over_50_from_50_at_7():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 6
    assert item.quality == 50


@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_backstage_pass_quality_is_never_over_50_starting_over_50_bug():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 100

@pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
def test_backstage_pass_quality_is_never_over_50_starting_over_50_fixed():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == 5
    assert item.quality == 50

# this shows a bug in other cases, for Backstage passes its ok
def test_backstage_pass_quality_is_never_over_50_starting_over_50_past_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == -2
    assert item.quality == 0



