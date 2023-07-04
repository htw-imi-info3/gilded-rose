from tests.settings import pytest, Item, xfail_bug_in_original, xfail_bug_fix

#  'every': "- At the end of each day our system lowers
#  both values for every item",


# however "Sulfuras" is a
# legendary item and as such its Quality is 80 and it never
# alters.

def test_sulfuras_doesnt_change_starting_with_80(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, 80))
    assert item.sell_in == 10
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_doesnt_change(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, 10))
    assert item.sell_in == 10
    assert item.quality == 10


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_doesnt_change_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, 10))
    assert item.sell_in == 10
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_at_sell_in(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 1, 30))
    assert item.sell_in == 1
    assert item.quality == 30


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_at_sell_in_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 1, 30))
    assert item.sell_in == 1
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_after_sell_in(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 49))

    assert item.sell_in == 0
    assert item.quality == 49


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_after_sell_in_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 49))

    assert item.sell_in == 0
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_is_never_negative(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 99, 0))

    assert item.sell_in == 99
    assert item.quality == 0


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 99, 0))

    assert item.sell_in == 99
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_is_never_negative_past_sell_in(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 0))

    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_past_sell_in_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 0))

    assert item.sell_in == 0
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_is_never_negative_starting_negative_fails(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, -5))

    assert item.sell_in == 10
    assert item.quality == -5


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_starting_negative_fails_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, -5))

    assert item.sell_in == 10
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_is_never_negative_starting_negative_value(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, -5))

    assert item.sell_in == 10
    assert item.quality == -5


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_is_never_negative_starting_negative_value_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 10, -5))

    assert item.sell_in == 10
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_can_be_over_50_from_50(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 6, 50))

    assert item.sell_in == 6
    assert item.quality == 50


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_can_be_over_50_from_50_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 6, 50))

    assert item.sell_in == 6
    assert item.quality == 80


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_sulfuras_quality_can_be_over_50_starting_over_50_bug(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 100))

    assert item.sell_in == 0
    assert item.quality == 100


@pytest.mark.xfail(xfail_bug_fix, reason="sulfuras quality is not set to 80")
def test_sulfuras_quality_can_be_over_50_starting_over_50_bug_fixed(update):
    item = update(Item("Sulfuras, Hand of Ragnaros", 0, 100))

    assert item.sell_in == 0
    assert item.quality == 80
