# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a classic Hangman game in Python. You will practice working with strings, loops, conditionals, lists, and user input while creating a complete playable program.

## 📝 Tasks

### 🛠️	Build the Core Game Loop

#### Description
Create the main game flow for Hangman. The program should select a hidden word, let the player guess one letter at a time, and repeatedly update the game state until the game ends.

#### Requirements
Completed program should:

- Randomly select a word from a predefined Python list.
- Accept single-letter guesses from the user.
- Show the current progress of the word using underscores for unknown letters (for example: `_ _ t h _ n`).
- Track and display remaining incorrect attempts.
- End the game when the full word is guessed or when attempts run out.

### 🛠️	Handle Input and Endgame Messages

#### Description
Improve the user experience by validating guesses and showing clear feedback. The game should handle invalid or repeated input gracefully and provide a final result message.

#### Requirements
Completed program should:

- Reject invalid input (empty input, multiple characters, non-letter characters) with a helpful message.
- Detect repeated guesses and notify the player without changing attempts.
- Display a clear win message when the player guesses the word.
- Display a clear lose message when attempts reach zero, including the correct word.
- Keep prompts and messages student-friendly and easy to follow.
