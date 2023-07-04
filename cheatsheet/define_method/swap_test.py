class Item:
    def __init__(self, field):
        self.field = field

    def set_field(self, new_value):
        self.field = new_value


def set_field_test(self):
    item = Item('a')
    item.set_field('b')
    assert item.field == 'b'


def test_swap_and_use():
    a = Item('a')
    b = Item('b')

    swap_set_field(a, b)

    a.set_field('a to c')
    b.set_field('b to d')

    assert a.field == 'b to d'
    assert b.field == 'a to c'


def swap_set_field(a, b):
    a_set_field = a.set_field
    a.set_field = b.set_field
    b.set_field = a_set_field


def test_swap_and_use_1():
    a = Item('a')
    b = Item('b')

    swap_set_field(a, b)

    a.set_field('c')

    assert a.field == 'a'
    assert b.field == 'c'


def test_swap():
    a = Item('a')
    b = Item('b')
    assert a.field == 'a'
    a_set_field = a.set_field
    a.set_field = b.set_field
    b.set_field = a_set_field
    assert a.field == 'a'
    assert b.field == 'b'
