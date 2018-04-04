import sys
import colorama

from object import Object
from character import Character
from player import Player
from item import Item
from area import Area
from game_frame import GameFrame
from colors import Colors

colorama.init()

player = Player(0, 5, colorama.Fore.GREEN + colorama.Style.BRIGHT, "Lajja")
npc = Character(5, 5, '@', colorama.Fore.YELLOW, "NPC", 2, 50, items = [ Item("Magical Amulet", 20), Item("Magical Pie", 10000) ])

starting_village = Area("Starting Village", 10, 10)
starting_village.characters.append(player)
starting_village.characters.append(npc)

g = GameFrame(player, starting_village)

while(True):
    g.run_frame()
