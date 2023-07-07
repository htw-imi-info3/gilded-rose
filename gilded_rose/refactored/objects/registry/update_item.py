from .update_strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras
from .item_updater_factory import FACTORY


def get_updater_for(item):
    return FACTORY.strategy_for(item).update


FACTORY.register(NormalItem)
FACTORY.register(AgedBrie)
FACTORY.register(Sulfuras)
FACTORY.register(BackstagePass)
