class Item:
    def __init__(self, field):
        self.field = field


def create_set_field(self):
    def set_field(value):
        self.field = value
    return set_field


def test_item():
    item = Item('initial value')
    assert item.field == 'initial value'


def test_alter_item():
    item = Item('initial value')
    item.update = create_set_field(item)
    item.update('new value')
    assert item.field == 'new value'
    