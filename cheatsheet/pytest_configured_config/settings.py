import pytest  # noqa
from gilded_rose.original.gilded_rose import Item  # noqa
from dataclasses import dataclass


@dataclass
class XfailConfig:
    xfail_bug_in_original: bool
    xfail_bug_fix: bool
    xfail_new_features: bool


XFAILSETTINGS = XfailConfig(
    xfail_bug_in_original=True,
    xfail_bug_fix=False,
    xfail_new_features=False
)

