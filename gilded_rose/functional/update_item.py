
def update(item):
    if item.name in UPDATERS.keys():
        UPDATERS[item.name](item)
    else:
        UPDATERS[DEFAULT_KEY](item)


def cap(item):
    if item.quality < 0:
        item.quality = 0
    elif item.quality > 50:
        item.quality = 50


def create_update_function(quality_change):
    def template_function(item):
        cap(item)
        item.sell_in = item.sell_in - 1
        item.quality = item.quality + quality_change(item)
        cap(item)

    return template_function


def quality_change_normal(item):
    return -2 if item.sell_in < 0 else -1


def quality_change_conjured(item):
    return quality_change_normal(item) * 2


def quality_change_aged_brie(item):
    return 2 if item.sell_in < 0 else 1


def quality_change_backstage_pass(item):
    if item.sell_in < 5:
        return 3
    if item.sell_in < 10:
        return 2
    return 1


def cut_after(update_function):
    def cut_past_sell_in(item):
        update_function(item)
        if item.sell_in < 0:
            item.quality = 0
    return cut_past_sell_in


def update_sulfuras(item):
    item.quality = 80


DEFAULT_KEY = "----default-----"

UPDATERS = {
    DEFAULT_KEY: create_update_function(quality_change_normal),
    "Conjured Item": create_update_function(quality_change_conjured),
    "Aged Brie": create_update_function(quality_change_aged_brie),
    "Backstage passes to a TAFKAL80ETC concert":
        cut_after(create_update_function(
            quality_change_backstage_pass)),
    "Sulfuras, Hand of Ragnaros": update_sulfuras
    }
