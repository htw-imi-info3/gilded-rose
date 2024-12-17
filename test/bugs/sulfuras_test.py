
# in the original version,
# sulfuras' quality is never altered.
# this is a contradiction to
# "it is always 80"
# -> room for interpretation, but
# my interpretation is that
# the quality should always be set to 80.

def test_sulfuras_doesnt_change(update_item, fixed):
   item = update_item("Sulfuras, Hand of Ragnaros", 10, 10)
   assert item.sell_in == 10
   expected = 80 if fixed('sulfuras') else 10
   assert item.quality == expected

def test_sulfuras_at_sell_in(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 1, 30)
    assert item.sell_in == 1
    
    expected = 80 if fixed('sulfuras') else 30
    assert item.quality == expected

def test_sulfuras_after_sell_in(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 0, 49)
    assert item.sell_in == 0
    
    expected = 80 if fixed('sulfuras') else 49
    assert item.quality == expected

def test_sulfuras_quality_is_never_negative(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 99, 0)
    assert item.sell_in == 99

    expected = 80 if fixed('sulfuras') else 0
    assert item.quality == expected

def test_sulfuras_quality_is_never_negative_past_sell_in(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 0, 0)
    assert item.sell_in == 0

    expected = 80 if fixed('sulfuras') else 0
    assert item.quality == expected

def test_sulfuras_quality_is_never_negative_starting_negative_fails(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 10, -5)
    assert item.sell_in == 10

    expected = 80 if fixed('sulfuras') else -5
    assert item.quality == expected

def test_sulfuras_quality_is_never_negative_starting_negative_value(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 10, -5)
    assert item.sell_in == 10

    expected = 80 if fixed('sulfuras') else -5
    assert item.quality == expected

def test_sulfuras_quality_can_be_over_50_from_50(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 6, 50)
    assert item.sell_in == 6

    expected = 80 if fixed('sulfuras') else 50
    assert item.quality == expected

def test_sulfuras_quality_can_be_over_50_starting_over_50(update_item, fixed):
    item = update_item("Sulfuras, Hand of Ragnaros", 0, 100)
    assert item.sell_in == 0

    expected = 80 if fixed('sulfuras') else 100
    assert item.quality == expected