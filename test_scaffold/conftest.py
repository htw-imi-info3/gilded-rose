import pytest

from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original
from gilded_rose.refactored.gilded_rose import GildedRose as GildedRose_Refactored

def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'original': GildedRose_Original,
    'refactored': GildedRose_Refactored,
    }
