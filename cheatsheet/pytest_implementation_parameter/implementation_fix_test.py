import pytest

# if you have 2 implementations
def impl_a():
    return 'a'

def impl_b():
    return 'b'

# have a fixture return one of them
@pytest.fixture
def impl_local():
    return impl_a


@pytest.mark.xfail(reason="expect a")
def test_for_a(impl_local):
    assert 'a' == impl_local()
    
@pytest.mark.xfail(reason="expect b")
def test_for_b(impl_local):
    assert 'b' == impl_local()
    
