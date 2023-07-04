# -*- coding: utf-8 -*-
from .update_item import attach_updater


class GildedRose(object):

    def __init__(self, items):
        self.items = [attach_updater(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()
