from lupa import LuaRuntime

class DynamicObject:
    def __init__(self, lua_file):
        self._definitions = self.load_lua_definitions(lua_file)
        self._attributes = {}
        for var_name, data_type in self._definitions.items():
            self.set_attribute(var_name, self.default_value(data_type))

    @staticmethod
    def load_lua_definitions(lua_file):
        lua = LuaRuntime(unpack_returned_tuples=True)
        with open(lua_file, 'r') as file:
            lua_script = file.read()
        return lua.execute(lua_script)

    @staticmethod
    def default_value(data_type):
        type_defaults = {
            "string": "",
            "int": 0,
            "float": 0.0,
            "dict": {},
            "bool": False,
            "set": set(),
            "object": None
        }
        return type_defaults.get(data_type, None)

    def set_attribute(self, attr_name, value):
        if attr_name in self._definitions:
            expected_type_str = self._definitions[attr_name]
            value_type = type(value).__name__
            if not self.is_type(value, expected_type_str):
                raise TypeError(f"Attribute '{attr_name}' must be of type '{expected_type_str}' but was '{value_type}'")
            self._attributes[attr_name] = value
        else:
            raise AttributeError(f"'{attr_name}' is not a valid attribute")

    def get_attribute(self, attr_name):
        return self._attributes.get(attr_name, None)

    @staticmethod
    def is_type(value, expected_type_str):
        python_types = {
            "string": str,
            "int": int,
            "float": float, 
            "dict": dict,
            "bool": bool,
            "set": set
        }
        expected_type = python_types.get(expected_type_str, object)
        return isinstance(value, expected_type)

# Example usage
#player = DynamicObject("player_variables.lua")

# Set and get attributes
#player.set_attribute("name", "Hero")
#player.set_attribute("health", 100)

#print(player.get_attribute("name"))  # Outputs: Hero
#print(player.get_attribute("health"))  # Outputs: 100

# Attempting to set an incorrect type will raise an error
#try:
#    player.set_attribute("health", "not a number")
#except TypeError as e:
#    print(e)  # Outputs error message

