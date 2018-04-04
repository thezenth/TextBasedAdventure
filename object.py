import math

class Object:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanceTo(self, fromObj):
        return math.sqrt( ((self.x - fromObj.x) ** 2) + ((self.y - fromObj.y) ** 2) )
