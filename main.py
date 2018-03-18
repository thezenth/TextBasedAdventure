import sys

from object import Object
from character import Character
from player import Player
from item import Item
from area import Area
from game_frame import GameFrame
from colors import Colors

player = Player(50, 50, Colors.OKGREEN, "Lajja")
npc = Character(25, 25, '@', Colors.OKBLUE, "NPC", 2, 50, items = [ Item("Magical Amulet", 20), Item("Magical Pie", 10000) ])

starting_village = Area("Starting Village", 100, 100)
starting_village.characters.append(player)
starting_village.characters.append(npc)

g = GameFrame(player, starting_village)

while(True):
    g.run_frame()
