import pytest
import importlib
from gilded_rose.refactored.gilded_rose import GildedRose
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original
from .settings import XFAILSETTINGS


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'refactored': GildedRose,
    'original': GildedRose_Original,
}


def pytest_configure(config):
    impl_value = config.option.impl
    if impl_value == 'original':
        XFAILSETTINGS.xfail_bug_in_original = False
        XFAILSETTINGS.xfail_bug_fix = True
        XFAILSETTINGS.xfail_new_features = True
    elif impl_value == 'refactored':
        XFAILSETTINGS.xfail_bug_in_original = True
        XFAILSETTINGS.xfail_bug_fix = False
        XFAILSETTINGS.xfail_new_features = False


def _impl_includes_gilded_rose(impl_value):
    return impl_value in ['original', 'refactored']


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
        module_name = f"gilded_rose.refactored.{impl_value}"
        impl = importlib.import_module(module_name)

        def _update(item):
            updater = impl.get_updater_for(item)
            updater(item)
            return item

    return _update
