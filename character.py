from object import Object

class Character(Object):
    def __init__(self, x, y, char, color, name, range, money, hostile = False, items = [], knowledge = []):
        Object.__init__(self, x, y, char, color)
        self.name = name
        self.range = range
        self.money = money
        self.hostile = hostile
        self.items = items # dictionray of items and what they are willing to trade for
        self.knowledge = knowledge # dictionary of knowledge tidbits according to menu
        """
        Knowledge example:
        1. Recent events --> "recent_events : 'Something bad happened!'"
        2. Monster Tidbits --> "monster_tidbits : 'Creepy beast!'"
        """

    def trade(self, tradeItem, buyingFrom = None):
        if tradeItem.value > self.money:
            print("Not enough money to buy this item!")
        else:
            self.money -= tradeItem.value
            self.items.append(tradeItem)
            if buyingFrom is not None:
                buyingFrom.items.remove(tradeItem)


# need attack method!
