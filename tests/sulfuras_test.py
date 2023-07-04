from tests.settings import *

#  'every': "- At the end of each day our system lowers both values for every item",



# however "Sulfuras" is a
# legendary item and as such its Quality is 80 and it never alters.

def test_sulfuras_doesnt_change_starting_with_80():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_doesnt_change():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_doesnt_change_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 10, 10)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80



@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_at_sell_in():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 1
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_at_sell_in_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 1, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 1
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_after_sell_in():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_after_sell_in_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 49)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80



@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_is_never_negative():
    item = Item("Sulfuras, Hand of Ragnaros", 99, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 99
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 99, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 99
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_is_never_negative_past_sell_in():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_past_sell_in_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_is_never_negative_starting_negative_fails():
    item = Item("Sulfuras, Hand of Ragnaros", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_starting_negative_fails_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_is_never_negative_starting_negative_value():
    item = Item("Sulfuras, Hand of Ragnaros", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_starting_negative_value_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 10, -5)
    GildedRose([item]).update_quality()
    assert item.sell_in == 10
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_can_be_over_50_from_50():
    item = Item("Sulfuras, Hand of Ragnaros", 6, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 6
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_can_be_over_50_from_50_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 6, 50)
    GildedRose([item]).update_quality()
    assert item.sell_in == 6
    assert item.quality == 80




@pytest.mark.xfail(xfail_bug_in_original, reason = "bug in original")
def test_sulfuras_quality_can_be_over_50_starting_over_50_bug():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

@pytest.mark.xfail(xfail_bug_fix, reason = "sulfuras quality is not set to 80")
def test_sulfuras_quality_can_be_over_50_starting_over_50_bug_fixed():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 100)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80
