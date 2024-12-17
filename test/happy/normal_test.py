# tests for normal items

def test_something(update_item):
    item = update_item("normal with any name", 5, 20)
    assert item.sell_in == 4
    assert item.quality == 19


def test_normal_reduces_both(update_item):
    item = update_item("normal with any name", 10, 10)
    assert item.sell_in == 9
    assert item.quality == 9


def test_normal_reduces_both_at_sell_in(update_item):
    item = update_item("normal with any name", 1, 30)
    assert item.sell_in == 0
    assert item.quality == 29


def test_normal_degrades_faster_after_sell_in(update_item):
    item = update_item("normal with any name", 0, 49)
    assert item.sell_in == -1
    assert item.quality == 47


def test_normal_quality_is_never_negative(update_item):
    item = update_item("normal with any name", 99, 0)
    assert item.sell_in == 98
    assert item.quality == 0


def test_normal_quality_is_never_negative_past_sell_in(update_item):
    item = update_item("normal with any name", 0, 0)
    assert item.sell_in == -1
    assert item.quality == 0


def test_normal_quality_is_never_over_50_from_50(update_item):
    item = update_item("normal with any name", 6, 50)
    assert item.sell_in == 5
    assert item.quality == 49


def test_failed_characterization_test_2(update_item):
    item = update_item("normal with any name", -2, 1)
    assert item.sell_in == -3
    assert item.quality == 0


def test_failed_characterization_test_1(update_item):
    item = update_item("normal with any name", -1, 1)
    assert item.sell_in == -2
    assert item.quality == 0


def test_failed_characterization_test_0(update_item):
    item = update_item("normal with any name", 0, 1)
    assert item.sell_in == -1
    assert item.quality == 0
