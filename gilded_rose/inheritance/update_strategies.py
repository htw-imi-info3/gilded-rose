

class Sulfuras:
    def update(self, item):
        item.quality = 80


class AgingItem():
    def update(self, item):
        self._age(item)
        self._cap_quality(item)
        self._update_quality(item)
        self._cap_quality(item)

    def _age(self, item):
        item.sell_in = item.sell_in - 1

    def _update_quality(self, item):
        item.quality += self.__quality_change(item)

    def __quality_change(self, item):
        return 0

    @staticmethod
    def _cap_quality(item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            item.quality = 50


class NormalItem(AgingItem):

    def __quality_change(self, item):

        if item.sell_in < 0:
            return -2
        return -1


class AgedBrie(AgingItem):

    def __quality_change(self, item):
        if item.sell_in < 0:
            return 2
        return 1


class BackstagePass(AgingItem):
     
    def _update_quality(self, item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality += self.__quality_change(item)
            
    def __quality_change(self, item):
        if item.sell_in < 0:
            return 0
        if item.sell_in < 5:
            return 3
        if item.sell_in < 10:
            return 2
        return 1


class ConjuredItem(NormalItem):

    def __quality_change(self, item):
        return 2 * super().__quality_change(item)
