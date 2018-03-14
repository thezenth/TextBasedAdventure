import sys

from object import Object
from item import Item
from area import Area
from game_frame import GameFrame
from colors import Colors

player = Player(50, 50, Colors.OKGREEN, "Lajja")
npc = Character(25, 25, '@', Colors.OKBLUE, "NPC", 2, 50, items = [ Item("Magical Amulet", 20), Item("Magical Pie", 10000) ])

starting_village = Area(100, 100)
starting_village.objects.append(player)

g = GameFrame(player, starting_village)

while(True):
    g.run_frame()
