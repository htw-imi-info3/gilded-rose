class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class AgedBrie(Item):
    def update(self):
        self.sell_in = self.sell_in -1
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality = self.quality + 1
        if self.quality > 50:
            self.quality = 50


class Sulfuras(Item):
    def update(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)