from tests.settings import pytest, Item
from tests.settings import XFAILSETTINGS as XFS



def test_something(update):
    item = update(Item("normal with any name", 5, 20))
    assert item.sell_in == 4
    assert item.quality == 19


def test_normal_reduces_both(update):
    item = update(Item("normal with any name", 10, 10))
    assert item.sell_in == 9
    assert item.quality == 9


def test_normal_reduces_both_at_sell_in(update):
    item = update(Item("normal with any name", 1, 30))
    assert item.sell_in == 0
    assert item.quality == 29


def test_normal_degrades_faster_after_sell_in(update):
    item = update(Item("normal with any name", 0, 49))
    assert item.sell_in == -1
    assert item.quality == 47


def test_normal_quality_is_never_negative(update):
    item = update(Item("normal with any name", 99, 0))
    assert item.sell_in == 98
    assert item.quality == 0


def test_normal_quality_is_never_negative_past_sell_in(update):
    item = update(Item("normal with any name", 0, 0))
    assert item.sell_in == -1
    assert item.quality == 0


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_normal_quality_is_never_negative_starting_negative_fails(update):
    item = update(Item("normal with any name", 10, -5))
    assert item.sell_in == 9
    assert item.quality == -5


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_normal_quality_is_never_negative_starting_negative_fixed(update):
    item = update(Item("normal with any name", 10, -5))
    assert item.sell_in == 9
    assert item.quality == 0


def test_normal_quality_is_never_over_50_from_50(update):
    item = update(Item("normal with any name", 6, 50))
    assert item.sell_in == 5
    assert item.quality == 49


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_normal_quality_is_never_over_50_from_49_at_sell_in(update):
    item = update(Item("normal with any name", 0, 51))
    assert item.sell_in == -1
    assert item.quality == 49


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_normal_quality_is_never_over_50_from_49_at_sell_in_fixed(update):
    item = update(Item("normal with any name", 0, 51))
    assert item.sell_in == -1
    assert item.quality == 48


@pytest.mark.xfail(XFS.xfail_bug_in_original, reason="bug in original")
def test_normal_quality_is_never_over_50_starting_over_50_bug(update):
    item = update(Item("normal with any name", 0, 100))
    assert item.sell_in == -1
    assert item.quality == 98


@pytest.mark.xfail(XFS.xfail_bug_fix, reason="fixed value")
def test_normal_quality_is_never_over_50_starting_over_50_fixed(update):
    item = update(Item("normal with any name", 0, 100))
    assert item.sell_in == -1
    assert item.quality == 48

# these are not bugs after all, quality is set back to 0:


def test_failed_characterization_test_2(update):
    item = update(Item("normal with any name", -2, 1))
    assert item.sell_in == -3
    assert item.quality == 0


def test_failed_characterization_test_1(update):
    item = update(Item("normal with any name", -1, 1))
    assert item.sell_in == -2
    assert item.quality == 0


def test_failed_characterization_test_0(update):
    item = update(Item("normal with any name", 0, 1))
    assert item.sell_in == -1
    assert item.quality == 0
