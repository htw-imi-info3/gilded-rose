from gilded_rose.refactored.functional.template_methods \
    import update_factory, useless_after_sell_in


def get_updater_for(item):
    return UPDATERS.get(item.name, UPDATERS[DEFAULT_KEY])

# the same as in fun_decorators, but without decorators


def quality_change_normal(item):
    return -2 if item.sell_in < 0 else -1


def quality_change_aged_brie(item):
    return 2 if item.sell_in < 0 else 1


def quality_change_backstage_pass(item):
    if item.sell_in < 5:
        return 3
    if item.sell_in < 10:
        return 2
    return 1


def update_sulfuras(item):
    item.quality = 80


DEFAULT_KEY = "----default-----"

# without the decorators, the quality_change methods
# need to be explicitly wrapped
UPDATERS = {
    DEFAULT_KEY: update_factory(quality_change_normal),
    "Aged Brie": update_factory(quality_change_aged_brie),
    "Backstage passes to a TAFKAL80ETC concert":
        useless_after_sell_in(update_factory(
            quality_change_backstage_pass)),
    "Sulfuras, Hand of Ragnaros": update_sulfuras
    }
