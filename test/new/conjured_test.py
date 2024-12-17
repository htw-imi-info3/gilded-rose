import pytest
from test.conftest import FIXED
SKIP_CONJURED = 'conjured' not in FIXED

@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_5_30(update_item):
    item = update_item("Conjured Item", 5, 30)
    assert item.sell_in == 4
    assert item.quality == 28


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_10_2(update_item):
    item = update_item("Conjured Item", 10, 2)
    assert item.sell_in == 9
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_5_1(update_item):
    item = update_item("Conjured Item", 5, 1)
    assert item.sell_in == 4
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_5_3(update_item):
    item = update_item("Conjured Item", 5, 3)
    assert item.sell_in == 4
    assert item.quality == 1


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_1_2(update_item):
    item = update_item("Conjured Item", 1, 2)
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_1_1(update_item):
    item = update_item("Conjured Item", 1, 1)
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_1_0(update_item):
    item = update_item("Conjured Item", 1, 0)
    assert item.sell_in == 0
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_0_6(update_item):
    item = update_item("Conjured Item", 0, 6)
    assert item.sell_in == -1
    assert item.quality == 2


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_0_2(update_item):
    item = update_item("Conjured Item", 0, 2)
    assert item.sell_in == -1
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_0_1(update_item):
    item = update_item("Conjured Item", 0, 1)
    assert item.sell_in == -1
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_5_0(update_item):
    item = update_item("Conjured Item", 5, 0)
    assert item.sell_in == 4
    assert item.quality == 0


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_5_89(update_item):
    item = update_item("Conjured Item", 5, 89)
    assert item.sell_in == 4
    assert item.quality == 48


@pytest.mark.skipif(SKIP_CONJURED, reason="add 'conjured' to FIXED in conftest.py to activate these tests")
def test_conjured_0_89(update_item):
    item = update_item("Conjured Item", 0, 89)
    assert item.sell_in == -1
    assert item.quality == 46
