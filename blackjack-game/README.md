# This is a Python code that simulates a simplified version of the card game Blackjack.

The code defines four classes: `Card`, `Deck`, `Hand`, and a `Game` class.

- `Card` class: represents a single card with a `suit` and a `rank`. The `__init__()` method initializes the suit and rank values for a card. The `__str__()` method returns a string representation of the card object.

- `Deck` class: represents a deck of cards, which is a collection of 52 cards. The `__init__()` method initializes the deck by creating 52 `Card` objects and adding them to the `cards` list. The `shuffle()` method shuffles the deck using the `random.shuffle()` method. The `deal()` method returns a specified number of cards from the deck.

- `Hand` class: represents a hand of cards held by either the player or the dealer. The `__init__()` method initializes the `cards` list and sets the `value` of the hand to 0. The `add_card()` method adds cards to the hand. The `calculate_value()` method calculates the value of the hand by summing up the values of the cards in the hand. The `get_value()` method returns the current value of the hand. The `is_blackjack()` method checks if the hand is a blackjack (a hand with a value of 21) and returns a boolean value. The `display()` method displays the cards in the hand.

- `Game` class: represents the game itself. The `play()` method runs the game. It starts by asking the user how many games they want to play, then creates a `Deck` object, a `Hand` object for the player, and a `Hand` object for the dealer. It deals two cards to each player and displays the cards. It then prompts the player to choose whether to hit or stand, and adds cards to the player's hand as necessary. After the player has finished their turn, the dealer takes their turn by adding cards to their hand until the value of their hand is at least 17. The `check_winner()` method checks who won the game and returns a boolean value indicating whether the game is over. The `play()` method continues to the next game until the specified number of games has been played.
