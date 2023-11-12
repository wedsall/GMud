class Monster:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.is_alive = True
        self.current_room = None

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def attack(self, target):
        if self.is_alive:
            print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
            target.take_damage(self.attack_power)
        else:
            print(f"{self.name} is defeated and can't attack.")

    def get_current_room(self):
        return self.current_room

    def move_to_room(self, room):
        if self.current_room:
            self.current_room.remove_monster(self)
        room.add_monster(self)
        self.current_room = room

# Example of creating and using a monster
# dragon = Monster("Dragon", 100, 20)
# hero = Player("Hero", 50, 10)  # Assuming you have a Player class
# dragon.attack(hero)

