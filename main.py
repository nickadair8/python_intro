import random

def get_choices():
    player_choice = input("Enter a choice for rock-paper-scissors: ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose:  {player}  computer chose:   {computer}")
    if(player == computer):
        return "It's a tie" 
    elif(player == "rock" ):
        if(computer == "scissors"):
            return "you win"
        else:
            return "you lose"
    elif(player == "paper" ):
        if(computer == "rock"):
            return "you win"
        else:
            return "you lose"
    elif(player == "scissors" ):
        if(computer == "paper"):
            return "you win"
        else:
            return "you lose"

    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


# def greeting():
#     return "Hi"

# choices = get_choices()
# print(choices)

# food = ["pizza", "carrot", "eggs"]
# dinner = random.choice(food)