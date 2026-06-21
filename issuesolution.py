import random

def play_game():
    print("--- WELCOME TO THE NUMBER GUESSING GAME ---")
    
    # 1. Difficulty Level Setup
    print("Choose difficulty: 1 (Easy: 1-10), 2 (Medium: 1-50), 3 (Hard: 1-100)")
    level = input("Enter choice (1/2/3): ")
    
    if level == '1':
        target = random.randint(1, 10)
    elif level == '2':
        target = random.randint(1, 50)
    else:
        target = random.randint(1, 100)
        
    attempts = 0
    
    while True:
        user_input = input("GUESS THE TARGET OR QUIT(Q): ")
        
        if user_input.upper() == "Q":
            print("Game exited.")
            break
            
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Please enter a valid number or 'Q'.")
            continue
            
        attempts += 1
        
        if user_choice == target:
            # 2. Score Tracking
            # Score formula: 100 - (attempts * 5), minimum 0
            score = max(0, 100 - (attempts * 5))
            print(f"__WELDONE__")
            print(f"YOU SUCCESSFULLY GUESS THE TARGET!!")
            print(f"Attempts: {attempts}, Your Score: {score}")
            break
        elif user_choice < target:
            print("YOUR NUMBER IS LOWER, TAKE A BIGGER NUMBER!!")
        else:
            print("YOUR NUMBER IS BIGGER, TAKE A SMALLER NUMBER!!")

    print("__GAME OVER__")

play_game()
