from gilded_rose.refactored.objects.inheritance.update_strategies \
    import Sulfuras, AgingItem, AgedBrie, BackstagePass, NormalItem

# add is_for predicates to the update strategies
# that return True if the strategy is applicable
# to the item:

Sulfuras.is_for = lambda item: item.name == "Sulfuras, Hand of Ragnaros"

AgingItem.is_for = lambda item: False  # abstract base class

NormalItem.is_for = lambda item: True  # default

AgedBrie.is_for = lambda item: item.name == "Aged Brie"

BackstagePass.is_for = lambda item: item.name == \
    "Backstage passes to a TAFKAL80ETC concert"
