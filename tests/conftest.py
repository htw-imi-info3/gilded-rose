import pytest
import importlib
from gilded_rose.refactored.gilded_rose import GildedRose
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


# implementations that cannot be imported from update_item.get_updater_for
IMPLEMENTATIONS = {
    'refactored': GildedRose,
    'original': GildedRose_Original,
    }


@pytest.fixture(scope='session')
def update(request):
    impl_value = request.config.option.impl
    if impl_value is None or False:
        pytest.skip()
     
    if _impl_includes_gilded_rose(impl_value):
        module_name = f"gilded_rose.{impl_value}.gilded_rose"
        impl = importlib.import_module(module_name)
        gilded_rose = impl.GildedRose
        
        def _update(item):
            gilded_rose([item]).update_quality()
            return item
    else:
        module_name = f"gilded_rose.{impl_value}.update_item"
        impl = importlib.import_module(module_name)

        def _update(item):
            updater = impl.get_updater_for(item)
            updater(item)
            return item

    return _update


def _impl_includes_gilded_rose(impl_value):
    return impl_value in ['original', 'refactored']
