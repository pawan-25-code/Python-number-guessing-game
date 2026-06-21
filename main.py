import random

print("Let's play a game:- GUESS NUMBER IN BETWEEN 1 TO 100...")
target = random.randint(1, 100)

while True:
    user_choice = input("GUESS THE TARGET OR QUIT(Q):")
    
    if (user_choice.upper() == "Q"):
        break
        
    user_choice = int(user_choice)
    
    if (user_choice == target):
        print("__WELDONE__")
        print("YOU SUCCESSFULLY GUESS THE TARGET!!")
        break
        
    elif (user_choice < target):
        print("YOUR NUMBER IS LOWER THAN TARGET SO, TAKE ANOTHER BIGGER NUMBER!!")
        
    else:
        print("YOUR NUMBER IS BIGGER THAN TARGET SO, TAKE ANOTHER SMALLER NUMBER!!")

print("__GAME OVER__")
