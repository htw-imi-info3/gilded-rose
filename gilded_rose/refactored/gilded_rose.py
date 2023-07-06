from gilded_rose.refactored.fun_decorators.update_item import get_updater_for

# this complete GildedRose is tested via the test conf
# pytest $subdir --impl refactored
# the implementation can be changed in the import above.


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        for item in items:
            attach_updater(item)

    def update_quality(self):
        for item in self.items:
            item.update()


def attach_updater(item):
    updater = get_updater_for(item)

    def update():
        updater(item)

    item.update = update
    return item
