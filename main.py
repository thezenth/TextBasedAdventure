import sys

from object import Object
from area import Area
from game_frame import GameFrame
from colors import Colors

player = Object(50, 50, '@', Colors.OKGREEN)

starting_village = Area(100, 100)
starting_village.objects.append(player)

g = GameFrame(player, starting_village)

while(True):
    g.run_frame()
