
#  'every': "- At the end of each day our system lowers
#  both values for every item",


# however "Sulfuras" is a
# legendary item and as such its Quality is 80 and it never
# alters.

def test_sulfuras_doesnt_change_starting_with_80(update_item):
    item = update_item("Sulfuras, Hand of Ragnaros", 10, 80)
    assert item.sell_in == 10
    assert item.quality == 80
