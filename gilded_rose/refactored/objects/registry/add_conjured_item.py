from .update_strategies import NormalItem
from .item_updater_factory import FACTORY


class ConjuredItem(NormalItem):
    @staticmethod
    def is_for(item):
        return item.name == "Conjured Item"

    def _quality_change(self, item):
        return 2 * super()._quality_change(item)


FACTORY.register(ConjuredItem)
