import os

def execute(command, player):
    # Define the directory where your command modules are located
    commands_dir = os.path.join(os.path.dirname(__file__), '')

    # List all the .py files in the directory
    command_files = [f[:-3] for f in os.listdir(commands_dir) if f.endswith('.py') and not f.startswith('__')]

    # Format the list into a string to display
    commands_list = ', '.join(command_files)

    return f"Available commands: {commands_list}"

