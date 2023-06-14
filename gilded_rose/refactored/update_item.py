class ItemUpdaterFactory:
    class_list = []
    @classmethod
    def register(cls, clazz):
        cls.class_list.insert(0,clazz)
    @classmethod
    def strategy_for(cls,item):
        for clazz in cls.class_list:
            if clazz.is_for(item):
                return clazz()

def cap_quality(item):
    if item.quality < 0:
        item.quality = 0
    elif item.quality > 50:
        item.quality = 50
class Sulfuras:
    @classmethod
    def is_for(cls, item):
        return item.name == "Sulfuras, Hand of Ragnaros"
    
    def update(self,item):
        cap_quality(item)
class AgingItem():
    def update(self,item):
        item.sell_in = item.sell_in -1
        cap_quality(item)
        self._update_quality(item)
        cap_quality(item)

    def _quality_change(self, item):
        return 0

    def _update_quality(self, item):
        item.quality += self._quality_change(item)
        self._update_hook(item)

    def _update_hook(self, item):
        pass

class NormalItem(AgingItem):
    @classmethod
    def is_for(cls, item):
        return True
    def _quality_change(self,item):
        if item.sell_in < 0:
            return -2
        return -1

class AgedBrie(AgingItem):
    @classmethod
    def is_for(cls, item):
        return item.name == "Aged Brie"

    def _quality_change(self,item):
        if item.sell_in < 0:
            return 2
        return 1

class BackstagePass(AgingItem):
    @classmethod
    def is_for(cls, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"
  
    def _update_hook(self, item):
        if item.sell_in < 0:
            item.quality = 0
    def _quality_change(self, item):
        if item.sell_in < 0:
            return 0
        if item.sell_in < 5:
            return 3
        if item.sell_in < 10:
            return 2
        return 1
  

ItemUpdaterFactory.register(NormalItem)
ItemUpdaterFactory.register(AgedBrie)
ItemUpdaterFactory.register(Sulfuras)
ItemUpdaterFactory.register(BackstagePass)