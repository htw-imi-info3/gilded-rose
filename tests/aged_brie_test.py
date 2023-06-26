import unittest

from tests.settings import *


# from ..gilded_rose.original.gilded_rose import GildedRose, Item
@unittest.skipIf(xfail_aged_brie, reason="not implemented.")
class AgedBrieTest(unittest.TestCase):
    def test_aged_brie_quality_increase(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 11)  # Expected quality after one day

    def test_aged_brie_quality_increase_past_sell_in(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 12)  # Expected quality after one day past sell-in

    def test_aged_brie_quality_max_limit(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 50)  # Quality should remain at max limit (50)
