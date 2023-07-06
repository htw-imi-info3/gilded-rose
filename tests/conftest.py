import pytest
import importlib
from gilded_rose.gilded_rose import GildedRose
from gilded_rose.original.gilded_rose import GildedRose as GildedRose_Original



from gilded_rose.functional.gilded_rose import GildedRose as GildedRose_Functional
from gilded_rose.inheritance.gilded_rose import GildedRose as GildedRose_Inheritance
from gilded_rose.registry.gilded_rose import GildedRose as GildedRose_Registry
from gilded_rose.trick_the_goblin.gilded_rose import GildedRose as GildedRose_Goblin
from gilded_rose.trick_the_goblin.gilded_rose_improved import GildedRose as GildedRoseImproved
from gilded_rose.fun_decorators.gilded_rose import GildedRose as GildedRoseDecorators

impl = importlib.import_module('gilded_rose.registry.gilded_rose')

def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


IMPLEMENTATIONS = {
    'refactored': GildedRose,
    'original': GildedRose_Original,
    'functional': GildedRose_Functional,
    'inheritance': GildedRose_Inheritance,
    'registry': GildedRose_Registry,
    'trick_the_goblin': GildedRose_Goblin,
    'trick_the_goblin_improved': GildedRoseImproved,
    'fun_decorators': GildedRoseDecorators, 
    }

@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    # prepare something ahead of all tests

    pass
    
@pytest.fixture(scope='session')
def update(request):
    impl_value = request.config.option.impl
    if impl_value is None or impl_value not in IMPLEMENTATIONS.keys():
        pytest.skip()
        
    if impl_value in ['original', 'refactored']:
        gilded_rose = IMPLEMENTATIONS[impl_value]
        
        def _update(item):
            gilded_rose([item]).update_quality()
            return item
    elif impl_value in ['functional', 'inheritance', 'registry', 'trick_the_goblin', 'trick_the_goblin_improved', 'fun_decorators']:
        impl = importlib.import_module(f"gilded_rose.{impl_value}.gilded_rose")
        gilded_rose = impl.GildedRose
        gilded_rose = IMPLEMENTATIONS[impl_value]
        
        def _update(item):
            gilded_rose([item]).update_quality()
            return item
    else:
        pass
   
    return _update
