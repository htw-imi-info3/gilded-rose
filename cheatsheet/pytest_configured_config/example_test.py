from .settings import XFAILSETTINGS
import pytest

# xfail_bug_in_original = True
# xfail_bug_fix = False
# xfail_new_features = False


@pytest.mark.xfail(XFAILSETTINGS.xfail_bug_fix, reason=".")
def test_bug_fix():
    assert False is XFAILSETTINGS.xfail_bug_fix


@pytest.mark.xfail(XFAILSETTINGS.xfail_bug_in_original, reason=".")
def test_bug_original():
    assert False is XFAILSETTINGS.xfail_bug_in_original


@pytest.mark.xfail(XFAILSETTINGS.xfail_new_features, reason=".")
def test_new_features():
    assert False is XFAILSETTINGS.xfail_new_features
