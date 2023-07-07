import pytest
from .settings import XFAILSETTINGS


def pytest_addoption(parser):
    parser.addoption("--impl", action="store")


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
