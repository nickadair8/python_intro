import random
from enum import Enum

#Tuples
names = ("Nick", "Will")
names[0]
names.index("Nick")

pri

# lists
# dogs = ["Malibu", "Marley", "Mae Mo"]
# humans = ["nick", "will"]
# dogs+=humans
# dogs.remove("will")
# dogs[1:1] = ["Test1", "Test2"]
# print(sorted(dogs,key=str.lower))
# dogsCopy = dogs[:]
# print(dogs)
# print(dogsCopy)

#ENUMS
# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

# print(len(State))


# name = "nick is cool"
# last = ""

# full_name = all([name, last])
# print(full_name)



# def get_choices():
#     player_choice = input("Enter a choice for rock-paper-scissors: ")
#     options = ["rock","paper","scissors"]
#     computer_choice = random.choice(options)
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices

# def check_win(player, computer):
#     print(f"you chose:  {player}  computer chose:   {computer}")
#     if(player == computer):
#         return "It's a tie" 
#     elif(player == "rock" ):
#         if(computer == "scissors"):
#             return "you win"
#         else:
#             return "you lose"
#     elif(player == "paper" ):
#         if(computer == "rock"):
#             return "you win"
#         else:
#             return "you lose"
#     elif(player == "scissors" ):
#         if(computer == "paper"):
#             return "you win"
#         else:
#             return "you lose"

    
# choices = get_choices()
# result = check_win(choices["player"], choices["computer"])
# print(result)


# def greeting():
#     return "Hi"

# choices = get_choices()
# print(choices)

# food = ["pizza", "carrot", "eggs"]
# dinner = random.choice(food)