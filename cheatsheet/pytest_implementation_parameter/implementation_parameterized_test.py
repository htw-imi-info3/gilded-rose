import pytest


def impl_a():
    return 'a'


def impl_b():
    return 'b'


@pytest.mark.xfail(reason="expect a")
def test_for_a_parameterized(impl):
    assert 'a' == impl()


@pytest.mark.xfail(reason="expect b")
def test_for_b_parameterized(impl):
    assert 'b' == impl()
