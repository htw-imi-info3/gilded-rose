from .update_item import UPDATERS, update_factory, quality_change_normal


def quality_change_conjured(item):
    return quality_change_normal(item) * 2


UPDATERS["Conjured Item"] = update_factory(quality_change_conjured)
