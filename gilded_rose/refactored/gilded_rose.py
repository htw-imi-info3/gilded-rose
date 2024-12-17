# -*- coding: utf-8 -*-
from argparse import ArgumentError

from gilded_rose.refactored import item
from gilded_rose.refactored.item import *


# as item is already instantiated this is not elegant.
def update_one_item(item):
    item_classes = [AgedBrie, Backstage, Sulfuras, Item]

    implementation = [c for c in item_classes if c.is_for(item.name)]
    if len(implementation) > 0:
        item2 = implementation[0](item.name, item.sell_in, item.quality)
    else:
        raise NotImplementedError(f"no implementation for '{item.name}'")

    item2.update()
    return item2


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_one_item(item)

