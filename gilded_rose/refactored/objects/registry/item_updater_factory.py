
class ItemUpdaterFactory:
    def __init__(self):
        self.class_list = []

    def register(self, clazz):
        self.class_list.insert(0, clazz)

    def strategy_for(self, item):
        for clazz in self.class_list:
            if clazz.is_for(item):
                return clazz()


FACTORY = ItemUpdaterFactory()
