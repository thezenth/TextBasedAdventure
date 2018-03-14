import math

from object import Object
from area import Area

class GameFrame:
    # ===== Constructor =====
    def __init__(self, player, area):
        self.player = player
        self.area = area

    # ===== Pre-Frame Checks =====
    # checks which happen at the beginning of the frame!
    def character_check(self):
        # check if any enemies are in range
        for c in self.area.characters:
            if c.hostile: # if hostile, check if it is in range
                dist = math.sqrt( ((self.player.x - c.x) ** 2) + ((self.player.y - c.y) ** 2) )
                if dist <= c.range: # if in range, then attack!
                    c.attack(self.player)

    # runs all pre-checks
    def pre_frame_check(self):
        self.character_check()

    # ===== Frame Actions =====
    # player movement prompt
    def move_prompt(self):
        direction = raw_input("Which direction? ").lower()

        allDirections = ["north", "south", "east", "west", "cancel"]

        while(direction not in allDirections):
            direction = raw_input("Invalid direction! Which direction? ").lower()

        if direction == "north":
            self.player.move(0, 1)
        elif direction == "south":
            self.player.move(0, -1)
        elif direction == "east":
            self.player.move(-1, 0)
        elif direction == "west":
            self.player.move(1, 0)

    # check attack... possibly prompt for different attacks later
    def attack_prompt(self, target):
        dist = math.sqrt( ((self.player.x - target.x) ** 2) + ((self.player.y - target.y) ** 2) )
        if dist <= self.player.range:
            self.player.attack(target)

    # talk prompt --> will provide menu of options
    def talk_prompt(self, target):
        dist = math.sqrt( ((self.player.x - target.x) ** 2) + ((self.player.y - target.y) ** 2) )
        if dist <= 2:
            self.player.talk_to(target)

    # trade prompt --> will provide menu of options based on target's items and what they are willing to trade for each
    def trade_prompt(self, target):
        dist = math.sqrt( ((self.player.x - target.x) ** 2) + ((self.player.y - target.y) ** 2) )
        if dist <= 2:
            self.player.trade_with(target)

    # interact movement prompt
    def interact_prompt(self):
        interaction = raw_input("Attack, talk, or trade? ").lower()

        allInteractions = ["attack", "talk", "trade", "cancel"]

        while(interaction not in allInteractions):
            interaction = raw_input("Invalid interaction! Which interaction? ").lower()

        target_name = raw_input("Who is the target? ").lower()
        target = self.area.find_character_by_name(target_name)

        if interaction == "attack":
            attack_prompt(target)
        elif interaction == "talk":
            talk_prompt(target)
        elif interaction == "trade":
            trade_prompt(target)

    # quit the game
    def quit_action(self):
        print("Bye! See you next time, adventurer...")
        sys.exit()

    # runs all frame actions with appropriate if/elif
    def frame_action_prompt(self):
        # ask the user for their input
        player_action = raw_input("What do you want to do? ").lower()

        if player_action == "move":
            self.move_prompt()
        elif player_action == "interact":
            self.interact_prompt()
        elif player_action == "look":
            self.look()
        elif player_action == "quit" or player_action == "exit":
            self.quit_action()

    def run_frame(self):
        self.pre_frame_check()
        self.frame_action_prompt()
