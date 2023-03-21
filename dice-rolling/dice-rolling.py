import random



def roll_dice():
    
    
    dice_drawing = {
        1: (
            "┌─────┐",
            "│     │",
            "│  •  │",
            "│     │",
            "└─────┘",
        ),
        2: (
            "┌─────┐",
            "│ •   │",
            "│     │",
            "│   • │",
            "└─────┘",
        ),
        3: (
            "┌─────┐",
            "│ •   │",
            "│  •  │",
            "│   • │",
            "└─────┘",
        ),
        4: (
            "┌─────┐",
            "│ • • │",
            "│     │",
            "│ • • │",
            "└─────┘",
        ),
        5: (
            "┌─────┐",
            "│ • • │",
            "│  •  │",
            "│ • • │",
            "└─────┘",
        ),
        6: (
            "┌─────┐",
            "│ • • │",
            "│ • • │",
            "│ • • │",
            "└─────┘",
        ),
    }
    roll = input("Would you like to roll a dice (yes/no)?: ")
    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You get {dice1} and {dice2}.")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll_again = input("Would you like to roll the dice again (yes/no)?: ")
roll_dice()


