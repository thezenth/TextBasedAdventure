from object import Object

class Character(Object):
    def __init__(self, range, items = None, knowledge = None):
        Object.__init__(self)
        self.range = range
        self.items = items # dictionray of items and what they are willing to trade for
        self.knowledge # dictionary of knowledge tidbits according to menu
        """
        Knowledge example:
        1. Recent events --> "recent_events : 'Something bad happened!'"
        2. Monster Tidbits --> "monster_tidbits : 'Creepy beast!'"
        """


# need attack method!
