from tests.settings import pytest, Item
from tests.settings import XFAILSETTINGS as XFS

#  'every': "- At the end of each day our system lowers both values for every item",


def test_aged_brie_gets_better(update):
    item = update(Item("Aged Brie", 10, 10))
    assert item.sell_in == 9
    assert item.quality == 11


def test_aged_brie_gets_better_one_before_sell_in(update):
    item = update(Item("Aged Brie", 1, 30))
    assert item.sell_in == 0
    assert item.quality == 31


def test_aged_brie_gets_better_at_sell_in(update):
    item = update(Item("Aged Brie", 0, 49))
    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_gets_better_faster_after_sell_in(update):
    item = update(Item("Aged Brie", -1, 22))
    assert item.sell_in == -2
    assert item.quality == 24


def test_aged_brie_quality_is_never_negative(update):
    item = update(Item("Aged Brie", 99, 0))
    assert item.sell_in == 98
    assert item.quality == 1


def test_aged_brie_quality_is_never_negative_past_sell_in(update):
    item = update(Item("Aged Brie", 0, 0))
    assert item.sell_in == -1
    assert item.quality == 2


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_aged_brie_quality_is_never_negative_starting_negative_bug(update):
    item = update(Item("Aged Brie", 10, -5))
    assert item.sell_in == 9
    assert item.quality == -4


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_aged_brie_quality_is_never_negative_starting_negative_fixed(update):
    item = update(Item("Aged Brie", 10, -5))
    assert item.sell_in == 9
    assert item.quality == 1


def test_aged_brie_quality_is_never_over_50_from_49(update):
    item = update(Item("Aged Brie", 6, 49))
    assert item.sell_in == 5
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50(update):
    item = update(Item("Aged Brie", 6, 50))
    assert item.sell_in == 5
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_49_at_sell_in(update):
    item = update(Item("Aged Brie", 0, 49))

    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50_at_sell_in(update):
    item = update(Item("Aged Brie", 0, 50))

    assert item.sell_in == -1
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_49_past_sell_in(update):
    item = update(Item("Aged Brie", -1, 49))

    assert item.sell_in == -2
    assert item.quality == 50


def test_aged_brie_quality_is_never_over_50_from_50_past_sell_in(update):
    item = update(Item("Aged Brie", -1, 50))

    assert item.sell_in == -2
    assert item.quality == 50


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_aged_brie_quality_is_never_over_50_starting_over_50_bug(update):
    item = update(Item("Aged Brie", 0, 100))

    assert item.sell_in == -1
    assert item.quality == 100


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_aged_brie_quality_is_never_over_50_starting_over_50_fixed(update):
    item = update(Item("Aged Brie", 0, 100))

    assert item.sell_in == -1
    assert item.quality == 50


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_aged_brie_quality_is_never_over_50_starting_over_50_past_sell_in_bug(update):
    item = update(Item("Aged Brie", -1, 100))

    assert item.sell_in == -2
    assert item.quality == 100


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_aged_brie_quality_is_never_over_50_starting_over_50_past_sell_in_fixed(update):
    item = update(Item("Aged Brie", -1, 100))

    assert item.sell_in == -2
    assert item.quality == 50
