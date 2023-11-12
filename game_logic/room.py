import logging
from include.ansi_colors import ANSI

logger = logging.getLogger(__name__)

class Room:
    def __init__(self, name, description, exits):
        print(f"Initializing room: {name}, exits: {exits}")
        self.name = name
        self.description = description
        self.monsters = set()
        self.players = set() 
        self.objects = set() 
        self.items = {}
        self.exits = dict(exits) if exits is not None else {}
        print(f"Exits after initialization: {self.exits}")

    def get_exit(self, direction):
        print(f"Getting exit for direction: {direction}, current exits: {self.exits}")
        return self.exits[direction]

    def add_monster(self, monster):
        self.monsters.add(monster)

    def add_player(self, player):
        self.players.add(player)
    
    def get_monsters(self):
        return self.monsters

    def remove_monster(self, monster):
        self.monsters.remove(monster)

    def get_players(self):
        return self.players

    def remove_player(self, player):
        self.players.remove(player)

    def add_item(self, item, desc):
        self.items[item] = desc

    def add_exit(self, direction, room_path):
        self.exits[direction] = room_path

    def remove_item(self, item):
        self.items.discard(item)  # Discard is safe to use if the item might not be present

    def get_item_description(self, item_name):
        return self.items.get(item_name, None)


    def get_object_description(self, target):
        for obj in self.monsters:
            if obj.name.lower() == target.lower():
                return obj.name
        return None 


    def get_description(self, who):
        # Return the room description, including any players and items present
        players_desc = '\n'.join(player.cap_name() for player in self.players if player != who)
        objects_desc = '\n'.join(objects.name for obj in self.objects)
        mons_desc = '\n'.join(f"{ANSI.FG_GREEN}{monster.name}{ANSI.RESET}" for monster in self.monsters)

        
        # Format the exits description
        if self.exits:
            if len(self.exits) == 1:
                exit_desc = f"The only obvious exit is: {list(self.exits.keys())[0]}."
            else:
                # Join all but the last exit with commas, and append the last with 'and'
                all_but_last = ', '.join(list(self.exits)[:-1])
                last = list(self.exits)[-1]
                exit_desc = f"The obvious exits are: {all_but_last} and {last}."
        else:
            exit_desc = "There are no obvious exits."

        # Combine all descriptions into one
        return f"{self.name}\n{ANSI.FG_YELLOW}{self.description}{ANSI.RESET}\n{exit_desc}\n{players_desc}{mons_desc}{objects_desc}"
