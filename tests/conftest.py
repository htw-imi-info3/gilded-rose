import pytest
from gilded_rose.original.gilded_rose import Item
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original
from gilded_rose.refactored.gilded_rose import GildedRose as GildedRose_Refactored


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'original': GildedRose_Original,
    'refactored': GildedRose_Refactored}


@pytest.fixture(scope='session')
def update(request):
    impl_value = request.config.option.impl
    if impl_value is None or impl_value not in IMPLEMENTATIONS.keys():
        pytest.skip()

    gilded_rose = IMPLEMENTATIONS[impl_value]

    def _update(item):
        gilded_rose([item]).update_quality()
        return item

    return _update
