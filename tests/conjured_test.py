from tests.settings import GildedRose, Item, pytest, xfail_new_features


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_5_30():
    item = Item("Conjured Item", 5, 30)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 28


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_10_2():
    item = Item("Conjured Item", 10, 2)
    GildedRose([item]).update_quality()
    assert item.sell_in == 9
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_5_1():
    item = Item("Conjured Item", 5, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_5_3():
    item = Item("Conjured Item", 5, 3)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 1


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_1_2():
    item = Item("Conjured Item", 1, 2)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_1_1():
    item = Item("Conjured Item", 1, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_1_0():
    item = Item("Conjured Item", 1, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_0_6():
    item = Item("Conjured Item", 0, 6)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 2


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_0_2():
    item = Item("Conjured Item", 0, 2)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_0_1():
    item = Item("Conjured Item", 0, 1)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_5_0():
    item = Item("Conjured Item", 5, 0)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 0


@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_5_89():
    item = Item("Conjured Item", 5, 89)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 48



@pytest.mark.xfail(xfail_new_features, reason="add conjured item")
def test_conjured_0_89():
    item = Item("Conjured Item", 0, 89)
    GildedRose([item]).update_quality()
    assert item.sell_in == -1
    assert item.quality == 46
