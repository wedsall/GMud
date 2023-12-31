class Player:
    def __init__(self, name, starting_room, lua_file):
        self.current_room = starting_room
        starting_room.add_player(self)
        self.name = name
    def move_to_room(self, room):
        if self.current_room:
            self.current_room.remove_player(self)
        room.add_player(self)
        self.current_room = room

    def get_current_room(self):
        return self.current_room
 
    def get_name(self):
        return self.name

    def cap_name(self):
        return self.name.capitalize()
 
    def query_context(self):
        return self.context
