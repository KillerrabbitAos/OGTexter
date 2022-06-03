def convert_to_string(text):
    bar = ""
    return bar.join(text)


def write(text):
    return f"test: {text}"


class Location:
    def __init__(self, Player_Presence, Possible_Destination):
        self.Player_Presence = Player_Presence
        self.Possible_Destination = Possible_Destination



class Person:
    def __init__(self, name, age, location, health, friends, items, home, action):
        self.name = name
        self.age = age
        self.location = location
        self.health = health
        self.friends = friends
        self.items = items
        self.home = home
        self.action = action


class Conversation:
    def __init__(self, members):
        self.members = members


def scene(number, action, player_name, player_location):
    if number == 1:
        print(f"Whilst {action} you stumble upon Mr.Z")
        current_conversation = True
        while current_conversation:
            subcommand = input("What will you say?: ")
            print(f"{subcommand} to you too {player_name}")
            if subcommand == "hello" or subcommand == "Hello":
                current_conversation = False

