
from gilded_rose.refactored.item import Item, item_factory, all_subclasses, item_classes

def test_item_subclasses():
    assert len(item_classes(Item)) == 3