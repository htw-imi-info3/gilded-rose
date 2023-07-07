from .update_strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras


def get_updater_for(item):
    return UPDATERS.get(item.name, UPDATERS[DEFAULT_KEY])().update


DEFAULT_KEY = "----default-----"


UPDATERS = {
    DEFAULT_KEY: NormalItem,
    "Aged Brie": AgedBrie,
    "Backstage passes to a TAFKAL80ETC concert":
        BackstagePass,
    "Sulfuras, Hand of Ragnaros": Sulfuras
    }
