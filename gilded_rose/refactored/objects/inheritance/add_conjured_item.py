from .update_strategies import NormalItem
from .update_item import UPDATERS


class ConjuredItem(NormalItem):

    def _quality_change(self, item):
        return 2 * super()._quality_change(item)


UPDATERS["Conjured Item"] = ConjuredItem
