from gilded_rose.original import Item

def test_repr():
    item = Item('just some item', 4, 5)
    assert str(item) == "just some item, 4, 5"
