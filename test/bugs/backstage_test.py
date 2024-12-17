def test_backstage_pass_quality_is_never_negative_starting_negative(update_item, fixed):
    item = update_item("Backstage passes to a TAFKAL80ETC concert", 10, -5)
    assert item.sell_in == 9
    expected = 2 if fixed('backstage') else -3
    assert item.quality == expected

# this shows a bug in other cases, for Backstage passes its ok
def test_backstage_pass_quality_is_never_over_50_starting_over_50(update_item, fixed):
    item = update_item("Backstage passes to a TAFKAL80ETC concert", 6, 100)
    assert item.sell_in == 5
    expected = 50 if fixed('backstage') else 100
    assert item.quality == expected
