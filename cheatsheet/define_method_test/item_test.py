class Item:
    def __init__(self, field):
        self.field = field


def set_field_creator(self):
    def set_field(value):
        self.field = value
    return set_field


def test_item():
    item = Item('initial value')
    assert item.field == 'initial value'


def test_alter_item():
    item = Item('initial value')
    item.update = set_field_creator(item)
    item.update('new value')
    assert item.field == 'new value'
    