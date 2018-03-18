from character import Character

class Player(Character):
    def __init__(self, x, y, color, name):
        Character.__init__(self, x, y, '@', color, name, 2, 100)
