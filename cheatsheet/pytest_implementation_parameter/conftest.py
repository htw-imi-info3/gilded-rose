import pytest
from .implementation_parameterized_test import impl_a, impl_b


def pytest_addoption(parser):
    parser.addoption("--impl_demo", action="store")


@pytest.fixture(scope='session')
def impl(request):
    impl_value = request.config.option.impl_demo
    if impl_value is None:
        pytest.skip()
 
    IMPLEMENTATIONS = {'impl_a': impl_a, 'impl_b': impl_b}
    return IMPLEMENTATIONS[impl_value]
