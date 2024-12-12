import pytest
from gilded_rose.original.gilded_rose import GildedRose


@pytest.fixture(scope='session')
def update(request):

    def _update(item):
        GildedRose([item]).update_quality()
        return item

    return _update
