import pytest

from gilded_rose import Item, GildedRose
from gilded_rose import FIXED

# this fixture creates a **a method** that
# creates a single item with the given parameters
# (name, sell_in, quality)
# and updates it by initializing GildedRose with an Item list
# consisting of this very item and finally calls update_quality

@pytest.fixture(scope='session')
def update_item():
    def _update_item(name, sell_in, quality):
        item = Item(name, sell_in, quality)
        GildedRose([item]).update_quality()
        return item
    return _update_item

# this fixture returns a method that
# checks if the item_type is in the "FIXED" list above
# this is used by the tests to choose the appropriate expectation
@pytest.fixture(scope='session')
def fixed():
    def _fixed(item_type):
        return item_type in FIXED
    return _fixed

