
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
