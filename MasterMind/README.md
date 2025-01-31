# MasterMind Game

## Overview
This is a simple Python implementation of the classic **MasterMind** game. The computer generates a **random 4-digit number**, and the player has a limited number of chances to guess the correct number. The game provides hints after each incorrect guess, revealing whether digits are correct and their presence in the number.

## Features
- Generates a **random 4-digit number** for the player to guess.
- Allows the player **5 chances** to guess the number.
- Displays hints after each incorrect guess:
  - Reveals correct digits in the correct position.
  - Notifies if a digit exists in the number but is in the wrong position.
- Ends the game when:
  - The player correctly guesses the number.
  - The player runs out of attempts.

## Requirements
This script only uses Python's built-in libraries, so **no external installations** are required.

## Imports
The script uses the following import:
```python
import random  # Used to generate a random 4-digit number
```

## How to Run
1. Make sure you have **Python installed** (Python 3.x recommended).
2. Copy and paste the `MasterMind` function into a new Python script.
3. Run the script.
4. Enter your **4-digit guess** when prompted.
5. Follow the hints and try to guess the correct number before your chances run out!

## Code Explanation
```python
comp_guess = str(random.randrange(1000, 10000))  # Generate a random 4-digit number
```
- Generates a random number between **1000 and 9999**.
- Converts it into a string for easy comparison.

```python
if user == comp_guess:
    print("You are MasterMind!")
    break
```
- If the player's guess matches the generated number, the game ends.

```python
correct_guess = ['X'] * 4  # Placeholder for correct digits
```
- Keeps track of correctly guessed digits at their respective positions.

```python
elif user[i] in comp_guess:
    print(f"{user[i]} is present in the guess")
```
- Checks if a digit is **present anywhere** in the number but in the wrong position.

## Example Gameplay
```
Enter the guess: 1234
4 is present in guess
['X', 'X', 'X', '4']
4 chances left.

Enter the guess: 5678
5 is present in guess
['5', 'X', 'X', '4']
3 chances left.

Enter the guess: 5943
You are MasterMind!
```

## License
This project is free to use under the **MIT License**.

## Thank you
[Author](https://github.com/abhinandan2540)

