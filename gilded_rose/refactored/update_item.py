from gilded_rose.refactored.update_strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras


def get_updater_for(item):
    return UPDATERS.get(item.name, UPDATERS[DEFAULT])().update


DEFAULT = "----default-----"

UPDATERS = {
    DEFAULT: NormalItem,
    "Aged Brie": AgedBrie,
    "Backstage passes to a TAFKAL80ETC concert":
        BackstagePass,
    "Sulfuras, Hand of Ragnaros": Sulfuras
    }
