class Item:
    def __init__(self, field):
        self.field = field

    def set_field(self, new_value):
        self.field = new_value

    def get_field(self):
        return self.field


def wrap_getter(old_getter):
    def new_wrapped_method():
        return f"<<<altered_get: {old_getter()}>>>"
    return new_wrapped_method


def wrap_setter(old_setter):
    def new_wrapped_method(new_value):
        old_setter(f"<<<altered_set: {new_value}>>>")

    return new_wrapped_method


def test_setter_getter():
    item = Item('item_field')
    item.set_field('b')
    assert item.get_field() == 'b'


def test_wrap_getter():
    item = Item('item_field')
    item.get_field = wrap_getter(item.get_field)

    assert item.get_field() == '<<<altered_get: item_field>>>'
    assert item.field == 'item_field'


def test_wrap_setter():
    item = Item('item_field')
    item.set_field = wrap_setter(item.set_field)

    assert item.get_field() == 'item_field'
    assert item.field == 'item_field'

    item.set_field('new value')

    assert item.get_field() == '<<<altered_set: new value>>>'
    assert item.field == '<<<altered_set: new value>>>'


def test_wrap_both():
    item = Item('item_field')
    item.set_field = wrap_setter(item.set_field)
    item.get_field = wrap_getter(item.get_field)

    assert item.get_field() == '<<<altered_get: item_field>>>'
    assert item.field == 'item_field'

    item.set_field('new value')

    assert item.get_field() == '<<<altered_get: <<<altered_set: new value>>>>>>'
    assert item.field == '<<<altered_set: new value>>>'
