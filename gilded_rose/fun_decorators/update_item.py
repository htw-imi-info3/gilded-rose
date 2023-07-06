
def update(item):
    update = UPDATERS.get(item.name, UPDATERS[DEFAULT_KEY])
    update(item)


def get_updater_for(item):
    return UPDATERS.get(item.name, UPDATERS[DEFAULT_KEY])


def update_factory(quality_change):
    def update(item):
        _cap(item)
        _age(item)
        _update_quality(item)
        _cap(item)

    def _update_quality(item):
        item.quality = item.quality + quality_change(item)

    def _age(item):
        item.sell_in = item.sell_in - 1

    def _cap(item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            item.quality = 50
   
    return update


def useless_after_sell_in(update):
    def useless_after_sell_in(item):
        update(item)
        if item.sell_in < 0:
            item.quality = 0
    return useless_after_sell_in


@update_factory
def quality_change_normal(item):
    return -2 if item.sell_in < 0 else -1


@update_factory
def quality_change_conjured(item):
    return quality_change_normal(item) * 2


@update_factory
def quality_change_aged_brie(item):
    return 2 if item.sell_in < 0 else 1


@useless_after_sell_in
@update_factory
def quality_change_backstage_pass(item):
    if item.sell_in < 5:
        return 3
    if item.sell_in < 10:
        return 2
    return 1


def update_sulfuras(item):
    item.quality = 80


DEFAULT_KEY = "----default-----"

UPDATERS = {
    DEFAULT_KEY: quality_change_normal,
    "Conjured Item": quality_change_conjured,
    "Aged Brie": quality_change_aged_brie,
    "Backstage passes to a TAFKAL80ETC concert":
        quality_change_backstage_pass,
    "Sulfuras, Hand of Ragnaros": update_sulfuras
    }
