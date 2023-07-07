from .update_item import UPDATERS, update_factory, _quality_change_normal


@update_factory
def quality_change_conjured(item):
    return _quality_change_normal(item) * 2


UPDATERS["Conjured Item"] = quality_change_conjured
