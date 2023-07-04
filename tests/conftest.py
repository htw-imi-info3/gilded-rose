import pytest
from gilded_rose.original.gilded_rose import Item
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original
from gilded_rose.functional.gilded_rose import GildedRose as GildedRose_Functional
from gilded_rose.inheritance.gilded_rose import GildedRose as GildedRose_Inheritance
from gilded_rose.registry.gilded_rose import GildedRose as GildedRose_Registry


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'original': GildedRose_Original,
    'functional': GildedRose_Functional,
    'inheritance': GildedRose_Inheritance,
    'registry': GildedRose_Registry}


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
