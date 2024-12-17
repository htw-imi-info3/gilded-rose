# -*- coding: utf-8 -*-
from argparse import ArgumentError

from gilded_rose.refactored.item import *


# as item is already instantiated this is not elegant.
def update_one_item(item):
    item2 = item_factory(item.name, item.sell_in, item.quality)
    item2.update()
    return item2


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_one_item(item)

