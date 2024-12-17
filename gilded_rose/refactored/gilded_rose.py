# -*- coding: utf-8 -*-
from gilded_rose.refactored.item import *


def update_one_item(item):
    if item.name.startswith("Sulfuras"):
        item2 = Sulfuras(item.name, item.sell_in, item.quality)
        item2.update()
        return item2

    if item.name.startswith("Aged Brie"):
        item2 = AgedBrie(item.name, item.sell_in, item.quality)
        item2.update()
        return item2

    if item.name.startswith("Backstage"):
        item2 = Backstage(item.name, item.sell_in, item.quality)
        item2.update()
        return item2

    item.update()
    return item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_one_item(item)

