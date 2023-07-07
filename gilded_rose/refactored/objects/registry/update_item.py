from .update_strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras, ConjuredItem


def get_updater_for(item):
    return ItemUpdaterFactory.strategy_for(item).update


def update(item):
    ItemUpdaterFactory.strategy_for(item).update(item)


class ItemUpdaterFactory:
    class_list = []

    @classmethod
    def register(cls, clazz):
        cls.class_list.insert(0, clazz)

    @classmethod
    def strategy_for(cls, item):
        for clazz in cls.class_list:
            if clazz.is_for(item):
                return clazz()


ItemUpdaterFactory.register(NormalItem)
ItemUpdaterFactory.register(AgedBrie)
ItemUpdaterFactory.register(Sulfuras)
ItemUpdaterFactory.register(BackstagePass)
ItemUpdaterFactory.register(ConjuredItem)
