from lupa import LuaRuntime
from game_logic.room import Room
from game_logic.monster import Monster
import logging

logger = logging.getLogger(__name__)

class GameWorld:
    def __init__(self):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.world_items = []
        self.world_rooms = {}
        self.world_players = {}
        self.world_monsters = {}

    def set_mud_service(self, mud_service):
        self.mud_service = mud_service

    def load_room(self, lua_script_path):
        # is the room already loaded?
        if lua_script_path in self.world_rooms:
            return self.world_rooms[lua_script_path]

        # Load the Lua script that defines the room
        with open(lua_script_path, 'r') as file:
            lua_script = file.read()
 
        # Execute the Lua script and get the room definition
        room_definition = self.lua.execute(lua_script)

        # Use the room definition to create a Room instance
        room = Room(
            name=room_definition['name'],
            description=room_definition['description'],
            exits=room_definition['exits'],
        )

        if 'items' in room_definition:
            python_dict = {}
            items_definition = room_definition['items']
            for index, item in items_definition.items():
                description = item['description']  # Get the description of the item
                names_definition = item['names']
                for index, name in names_definition.items():  # Iterate through each name in the names list
                    room.add_item(name, description)
        
        if 'monsters' in room_definition:
            monsters_definition = room_definition['monsters']
            monsters = []
            for index, monster_def in monsters_definition.items():  # Use .items() here
                monster_def_dict = dict(monster_def)
                mpath = monster_def_dict.get('path')
                params = dict(monster_def_dict.get('params', {}))
                #Expose these params to lua
                self.lua.globals()["params"] = params
                mcount = monster_def_dict.get('count', 1)  # Use default value 1 for count
        
                # Load the Lua script that defines the monster
                with open(mpath, 'r') as file:
                    lua_script = file.read()
                monster_definition = dict(self.lua.execute(lua_script))
                logger.info(monster_definition)

                for _ in range(mcount):  # Use mcount here
                    # mname=params.get('name')
                    monster = Monster(
                        name=monster_definition.get('name'),
                        health=monster_definition.get('health'),
                        attack_power=monster_definition.get('attack_power')
                    )
                    #self.world_monsters.append(monster)
                    monster.move_to_room(room)

        self.add_room_to_world(lua_script_path, room)

        return room

    def add_room_to_world(self, path, room):
        self.world_rooms[path] = room

    def add_item_to_world(self, item):
        self.world_items.append(item)

    def get_all_items(self):
        return self.world_items

    def get_all_rooms(self):
        return self.world_rooms

    def get_all_monsters(self):
        return self.world_monsters
   
    # Players
    def add_player(self, player):
        self.world_players[player.name] = player

    def get_player(self, name):
        return self.world_players.get(name)

    def get_all_players(self):
        return self.world_players

    def tell_player(self, player_name, message):
        player = self.get_player(player_name)
        if player:
            logger.info(f"telling {player_name} {message}")
            self.mud_service.send_message_to_player(player_name, message)
            self.mud_service.message_available[player_name].set()
        else:
            print(f"Player with name {player_name} not found.")

    def tell_room(self, room, message, exclude_players=None):
        exclude_players = exclude_players or []  # Ensure exclude_players is a list
        for player in room.get_players():
            if player not in exclude_players:
                self.tell_player(player.name, message)  # Assuming Player class has this method

game_world = GameWorld()
