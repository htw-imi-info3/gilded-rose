class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update(self):
        self.sell_in = self.sell_in -1
        self.quality = self.quality - 1
        if self.sell_in < 0:
            self.quality = self.quality - 1
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

class AgedBrie(Item):
    def update(self):
        self.sell_in = self.sell_in -1
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality = self.quality + 1
        if self.quality > 50:
            self.quality = 50

class Backstage(Item):
    def update(self):
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

        self.quality = self.quality + 1
        item = self
        if item.sell_in < 11:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1
        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            self.quality = 0

        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

class Sulfuras(Item):
    def update(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)