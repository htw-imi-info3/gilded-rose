import pytest
import importlib
from gilded_rose.gilded_rose import GildedRose
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'refactored': GildedRose,
    'original': GildedRose_Original,
    }


@pytest.fixture(scope='session')
def update(request):
    impl_value = request.config.option.impl
    if impl_value is None or impl_value not in IMPLEMENTATIONS.keys():
        pytest.skip()
        
    if _impl_includes_gilded_rose(impl_value):
        gilded_rose = IMPLEMENTATIONS[impl_value]
        
        def _update(item):
            gilded_rose([item]).update_quality()
            return item
    elif impl_value in IMPLEMENTATIONS.keys():
   # ['functional', 'inheritance', 'registry', 'trick_the_goblin', 'trick_the_goblin_improved']:
        impl = importlib.import_module(f"gilded_rose.{impl_value}.gilded_rose")
        gilded_rose = impl.GildedRose
        gilded_rose = IMPLEMENTATIONS[impl_value]
        
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
