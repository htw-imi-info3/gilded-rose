import pytest
from .implementation_parameterized_test import impl_a, impl_b


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()
    return name_value


@pytest.fixture(scope='session')
def impl(request):
    impl_value = request.config.option.impl
    if impl_value is None:
        pytest.skip()
 
    IMPLEMENTATIONS = {'impl_a': impl_a, 'impl_b': impl_b}
    return IMPLEMENTATIONS[impl_value]
