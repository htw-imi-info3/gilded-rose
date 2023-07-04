from .update_strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras, ConjuredItem


def update(item):
    strategy = UPDATERS.get(item.name, UPDATERS[DEFAULT_KEY])
    strategy().update(item)


DEFAULT_KEY = "----default-----"


UPDATERS = {
    DEFAULT_KEY: NormalItem,
    "Conjured Item": ConjuredItem,
    "Aged Brie": AgedBrie,
    "Backstage passes to a TAFKAL80ETC concert":
        BackstagePass,
    "Sulfuras, Hand of Ragnaros": Sulfuras
    }
