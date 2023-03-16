# This code is a simple implementation of the game "Rock, Paper, Scissors" between a human player and the computer.

---

The `get_choices()` function prompts the human player to enter their choice of "rock", "paper", or "scissors", and then generates a random choice for the computer using the `random.choice()` function. The function returns a dictionary containing both the player's and the computer's choices.

The `check_win()` function takes in the player's and the computer's choices as arguments and checks who wins based on the game rules. It then returns a message indicating whether the player won, lost, or tied.

In the main part of the code, choices variable is assigned the dictionary returned by `get_choices()` function, and result variable is assigned the result of calling `check_win()` function with the player's and the computer's choices. Finally, the result is printed to the console.

Overall, this code allows a human player to play a simple game of "Rock, Paper, Scissors" against the computer.
