
def create_update_function(special_updater):
    def cap(item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            item.quality = 50

    def template_function(item):
        cap(item)
        item.sell_in = item.sell_in - 1
        special_updater(item)
        cap(item)

    return template_function


def update_normal(item):
    change = -2 if item.sell_in < 0 else -1
    item.quality = item.quality + change


def update_conjured(item):
    change = -4 if item.sell_in < 0 else -2
    item.quality = item.quality + change


def update_aged_brie(item):
    change = 2 if item.sell_in < 0 else 1
    item.quality = item.quality + change


def update_backstage_pass(item):
    if item.sell_in < 0:
        item.quality = 0
        return

    def backstage_change():
        if item.sell_in < 5:
            return 3
        if item.sell_in < 10:
            return 2
        return 1
    item.quality = item.quality + backstage_change()


def update_sulfuras(item):
    item.quality = 80


DEFAULT_KEY = "----default-----"

UPDATERS = {DEFAULT_KEY: create_update_function(update_normal),
            "Conjured Item": create_update_function(update_conjured),
            "Aged Brie": create_update_function(update_aged_brie),
            "Backstage passes to a TAFKAL80ETC concert":
                create_update_function(update_backstage_pass),
            "Sulfuras, Hand of Ragnaros": update_sulfuras
            }


def update(item):
    if item.name in UPDATERS.keys():
        UPDATERS[item.name](item)
    else:
        UPDATERS[DEFAULT_KEY](item)
