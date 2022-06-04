import random
import time
import re
import tools

player_X = 0
player_Y = 0

run = True
run2 = True
run3 = True
admin = False
haveBeenAdmin = False

# persons
player = tools.Person("steve", 12, "school", 100, ["steve", "Alex"], [], "unknown", "doing nothing")
Steve = tools.Person("steve", 12, "home", 100, ["Alex", player.name], [], "unknown", "doing nothing")
Alex = tools.Person("steve", 12, "school", 100, ["Steve", player.name], [],
                    "unknown", "doing nothing")

# locations
school = tools.Location(True, True)

# indicators
indicator = "/"

health_indicator_bar = (tools.convert_to_string(
    ([indicator] * (int(player.health / 10)))))

# main loops
while run:

    while run2:
        print("Welcome to Texter!")
        print("It´s time to make your character.")
        player.name = input("Character Name: ")
        current_scene = 0
        while run3:
            choice = (random.randint(0, 100))
            current_scene = current_scene + 1
            current_conversation = False
            player.action = "doing nothing"
            hurt = 0
            heal = 0
            health_indicator_bar = (tools.convert_to_string(
                ([indicator] * (int(player.health / 10)))))

            print(
                f"health:{health_indicator_bar} friends:{len(player.friends)}")

            command = input("Write here: ")

            if command == "__admin__":
                subCommand = input("print OK after the semicolon to confirm, if not, just click enter;")
                if subCommand == "OK":
                    admin = True
                    haveBeenAdmin = True
                    print("you are now __admin__")
                else:
                    print("Ok. You are not __admin__")
            if command == "__deAdmin__":
                if admin:
                    subCommand = input("print OK after the semicolon to confirm, if not, just click enter;")
                    if subCommand == "OK":
                        admin = False
                        print("You are no longer __admin__")
                else:
                    print("Nothing changed. You are not __admin__")
            if command == "haveBeenAdmin?":
                if haveBeenAdmin:
                    print("Yes")
                else:
                    print("No")
            

                
            
            if choice:
                Steve.location = player.location
            if command.startswith("walk to"):
                player.location = (command.split()[2])
                player.action = f"walking to {player.location}"
                print(f"You began walking to {player.location}")

            if Steve.location == player.location:
                current_conversation = tools.Conversation([Steve])


            if command == "health":
                print(f"Your health is {player.health}.")
            if command == "location":
                print(f"Location: {player.location}")
            if command == "friends":
                print(player.friends)
            if command == "items":
                print(player.items)
            if command == "admin?":
                if admin:
                    print("yes")
                else:
                    print("no")

            tools.scene(current_scene, player.action, player.name, player.location)


            if admin:
                if command.startswith("hurt"):
                    hurt = re.findall("\d", command)
                    hurt = tools.convert_to_string(hurt)
                    print(hurt)
                if command.startswith("heal") and command != "health":
                    heal = re.findall("\d", command)
                    heal = tools.convert_to_string(heal)
                    print(heal)

            player.health = player.health - int(hurt)
            player.health = player.health + int(heal)
            if player.location == "School":
                school.Player_Presence = True
                print("you are now at school")




