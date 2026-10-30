
# Unit 27 – Mock Exam III: Morra (Game)

## Overview

In this mock exam, you will develop a Python console game called **Morra**, where one human player competes against a computer.

This assignment will test your understanding of:

- Functions and return values
- Conditional statements
- Loops and repetition
- Input validation
- Exception handling
- Variables and calculations
- Working with predefined functions

You will be provided with a partially completed Python program. Your responsibility is to complete the missing functionality without modifying the predefined code.

---

## Part 1 – Understanding Morra

### What is Morra?

Morra is a traditional hand game dating back thousands of years to ancient Greece and Rome.

In the original game, players simultaneously reveal a number of fingers while guessing the total number of fingers shown by everyone.

For this assignment, we will use a simplified version:

- One human player competes against one computer.
- Each player chooses a hand between **1 and 3 fingers**.
- Each player guesses the combined number of fingers shown by both players.
- The possible combined total is between **2 and 6**.
- A player wins the round by correctly guessing the combined total when the opponent guesses incorrectly.

The computer's hand and guess must remain hidden until the player has made both selections.

### How Does a Round Work?

Each round follows these steps:

1. The player selects a hand between 1 and 3.
2. The player guesses the combined total between 2 and 6.
3. The computer also selects a hand and makes a guess.
4. Both hands and guesses are revealed.
5. The program calculates the combined total.
6. The program determines the winner.
7. If there is a winner, the winner receives experience points (XP).
8. The player decides whether to play another round.

### Example 1 – Player Wins

Suppose the following choices are made:

| Participant | Hand | Guess |
|-------------|------|-------|
| Player | 2 | 5 |
| Computer | 3 | 4 |

The combined total is:

2 + 3 = 5

The player guessed 5, which matches the combined total.

The computer guessed 4, which is incorrect.

**Result: Player wins the round!**

### Example 2 – Computer Wins

| Participant | Hand | Guess |
|-------------|------|-------|
| Player | 1 | 4 |
| Computer | 2 | 3 |

The combined total is:

1 + 2 = 3

The computer correctly guessed 3, while the player incorrectly guessed 4.

**Result: Computer wins the round!**

### Example 3 – Tie

| Participant | Hand | Guess |
|-------------|------|-------|
| Player | 3 | 4 |
| Computer | 1 | 4 |

The combined total is:

3 + 1 = 4

Both participants correctly guessed 4.

**Result: Tie!**

Neither participant receives XP or an additional win.

### Example 4 – No Winner

| Participant | Hand | Guess |
|-------------|------|-------|
| Player | 2 | 3 |
| Computer | 3 | 6 |

The combined total is:

2 + 3 = 5

Neither participant guessed 5.

**Result: No winner.**

Neither participant receives XP or an additional win.

### Summary of Winning Conditions

| Condition | Result |
|-----------|--------|
| Only the player guesses correctly | Player wins |
| Only the computer guesses correctly | Computer wins |
| Both guess correctly | Tie |
| Neither guesses correctly | No winner |

**Important:** The closest guess does not win. A guess must match the combined total exactly.

---

## Part 2 – Experience Points (XP)

Morra uses an experience point system to track each participant's score.

The winner of each round earns randomly generated XP.

The amount of XP depends on the current game round.

**XP Formula:**

XP Earned = Random XP × Current Round

The predefined `generate_xp(game_round)` function generates a random value between 1 and 3 and multiplies it by the current round number.

### XP Examples

| Round | Random XP | XP Earned |
|-------|-----------|-----------|
| 1 | 2 | 2 |
| 2 | 3 | 6 |
| 3 | 1 | 3 |
| 4 | 3 | 12 |

Because XP is randomly generated, the amount earned may differ each time.

### Scoring Rules

- If the player wins, increase the player's total score by the XP earned and increase the player's win count by 1.
- If the computer wins, increase the computer's total score by the XP earned and increase the computer's win count by 1.
- If the round is a tie, do not update either participant's score or win count.
- If there is no winner, do not update either participant's score or win count.

The scores and win counts must be maintained throughout the game.

---

## Part 3 – Getting Started

### Setting Up Your Environment

1. Access the Unit 27 – Mock Exam III assignment through GitHub Classroom.
2. Clone the repository to your computer.
3. Open the repository in Visual Studio Code.
4. Locate and review the provided `morra.py` file.
5. Read and understand the predefined functions before writing your code.

### Important Programming Rules

- Do not modify or delete any predefined code.
- Write your implementation only in the regions marked `STUDENT CODE HERE`.
- Use the provided constants whenever instructed.
- Do not modify the predefined function names or parameters.
- Implement input validation and exception handling where required.
- Re-prompt the user when the instructions require a valid input.
- Test your program frequently as you complete each function.

**Note:** This is a mock practical exam. You are expected to independently design and implement the required functionality.

---

## Part 4 – Predefined Functions

The starter file contains several functions that are already implemented.

You must use these functions as needed, but you must not modify their code.

### 1. `get_game_header()`

Returns the game's header containing:

- Game name
- Game version
- Current date and time

### 2. `generate_xp(game_round)`

Generates XP based on the current round.

**Parameter:**
- `game_round` – Current round number

**Returns:**
- Random XP multiplied by the round number

### 3. `get_computer_hand()`

Randomly selects the computer's hand.

**Returns:**
- An integer between 1 and 3

### 4. `get_computer_guess()`

Randomly generates the computer's guess.

**Returns:**
- An integer between 2 and 6

### Provided Constants

The following constants are available:

| Constant | Value | Purpose |
|----------|-------|---------|
| `HAND_MIN` | 1 | Minimum number of fingers |
| `HAND_MAX` | 3 | Maximum number of fingers |

Use these constants instead of hardcoding the minimum and maximum hand values.

---

## Part 5 – Functions You Must Implement

Declare and implement the following five functions in the designated `STUDENT CODE HERE` region.

You may initially use `pass` when declaring each function to prevent errors while developing the remaining functions.

### Function 1 – `get_player_hand()`

**Purpose:** Prompt the player to select a hand.

Requirements:

1. Prompt the player to enter a number between `HAND_MIN` and `HAND_MAX`, inclusive.
2. Validate that the number is within the allowed range.
3. Handle invalid inputs and exceptions, including nonnumeric or blank input.
4. Continue prompting until a valid hand is entered.
5. Return the validated hand as an integer.

Example:

```text
Play a hand between 1 and 3: 5
Invalid Hand

Play a hand between 1 and 3: abc
Invalid Input

Play a hand between 1 and 3: 2
```

The function should return `2`.

### Function 2 – `get_player_guess()`

**Purpose:** Prompt the player to guess the combined total of both hands.

Requirements:

1. Prompt the player to enter a number between `HAND_MIN * 2` and `HAND_MAX * 2`, inclusive.
2. Validate that the guess is within the allowed range.
3. Handle invalid inputs and exceptions, including nonnumeric or blank input.
4. Continue prompting until a valid guess is entered.
5. Return the validated guess as an integer.

Example:

```text
Guess the sum of both hands between 2 and 6: 7
Invalid Guess

Guess the sum of both hands between 2 and 6: hello
Invalid Input

Guess the sum of both hands between 2 and 6: 4
```

The function should return `4`.

### Function 3 – `determine_winner(player_hand, player_guess, computer_hand, computer_guess)`

**Purpose:** Determine the winner of the current round.

Parameters:

- `player_hand` – Number of fingers selected by the player
- `player_guess` – Player's guess of the combined total
- `computer_hand` – Number of fingers selected by the computer
- `computer_guess` – Computer's guess of the combined total

Requirements:

1. Calculate the combined total of both hands.
2. Compare the player's guess against the combined total.
3. Compare the computer's guess against the combined total.
4. Determine the outcome using the Morra winning conditions.
5. Return one of the following strings:

| Return Value | Meaning |
|--------------|---------|
| `"player"` | Only the player guessed correctly |
| `"computer"` | Only the computer guessed correctly |
| `"tie"` | Both participants guessed correctly |
| `"no winner"` | Neither participant guessed correctly |

This function must return the result rather than print it.

### Function 4 – `get_stats(player_score, player_wins, computer_score, computer_wins)`

**Purpose:** Return the current game statistics in a formatted string.

Parameters:

- `player_score` – Player's accumulated XP
- `player_wins` – Number of rounds won by the player
- `computer_score` – Computer's accumulated XP
- `computer_wins` – Number of rounds won by the computer

Requirements:

1. Include all four statistics.
2. Format the statistics in a readable manner.
3. Return the formatted string.

Example output:

```text
==============================
  Player Score: 6
   Player Wins: 2
Computer Score: 3
 Computer Wins: 1
```

**Important:** This function must return the formatted statistics rather than print them directly.

### Function 5 – `get_play_again_prompt()`

**Purpose:** Ask the player whether to continue playing Morra.

Requirements:

1. Prompt the player to enter `yes` or `quit`.
2. Accept only these two responses.
3. Handle uppercase and lowercase responses.
4. If the response is invalid, display an error message and prompt again.
5. Return the validated response in lowercase.

Example:

```text
Do you want to play again (yes or quit): maybe
Invalid Response

Do you want to play again (yes or quit): YES
```

The function should return `"yes"`.

---

## Part 6 – Completing the `main()` Function

The `main()` function is partially implemented in the starter file.

The following variables are already initialized:

- `player_score`
- `player_wins`
- `computer_score`
- `computer_wins`
- `game_round`

You must complete the game workflow in the designated `STUDENT CODE HERE` region.

### Game Initialization

1. Display the game header and current date using the appropriate predefined function.
2. Begin the game at round 1.

### Game Loop

The program must repeatedly execute the following steps until the player chooses to quit.

**Step 1 – Display Statistics**

- Display the current game statistics only after round 1.
- Use the appropriate function to retrieve the formatted statistics.

**Step 2 – Display Round**

- Display the current round number.

**Step 3 – Obtain Hands and Guesses**

- Obtain the player's hand and guess using the appropriate functions.
- Obtain the computer's hand and guess using the predefined functions.
- Store all four values for use later.
- Keep the computer's selections hidden until the player has completed both inputs.

**Step 4 – Reveal Results**

Display:

- Computer's hand
- Computer's guess
- Combined total of both hands

**Step 5 – Determine the Winner**

- Call `determine_winner()` with the appropriate arguments.
- Display the result of the round.

**Step 6 – Update Statistics**

- If the player wins, generate XP and update the player's score and wins.
- If the computer wins, generate XP and update the computer's score and wins.
- If there is a tie or no winner, do not update the statistics.

**Step 7 – Ask to Play Again**

- Call `get_play_again_prompt()`.
- If the player enters `yes`, increase the round number by 1 and start another round.
- If the player enters `quit`, exit the game loop.

### Game Termination

When the player quits, the program must display:

```text
Thank you for playing Morra!
```

The program should terminate gracefully without crashing.

---

## Part 7 – Expected Console Output

The following example demonstrates two rounds of gameplay.

The computer's choices and XP values are randomly generated, so your output may differ.

```text
==============================
Morra
    Game Version 1.0
==============================
Date and Time: 28/10/2026 09:00:00

Round 1
Play a hand between 1 and 3: 2
Guess the sum of both hands between 2 and 6: 5

Computer's Hand 3
Computer's Guess 4

The sum of both hands is 5
Player won the round!
Do you want to play again (yes or quit): yes

==============================
  Player Score: 2
   Player Wins: 1
Computer Score: 0
 Computer Wins: 0

Round 2
Play a hand between 1 and 3: 1
Guess the sum of both hands between 2 and 6: 3

Computer's Hand 2
Computer's Guess 3

The sum of both hands is 3
It's a tie!
Do you want to play again (yes or quit): quit
Thank you for playing Morra!
```

Notice that:

- The game header appears at the beginning.
- Statistics are not displayed before round 1.
- Statistics appear at the beginning of subsequent rounds.
- The computer's choices are revealed after the player enters both selections.
- The player earns XP only when winning a round.
- A tie does not increase either participant's score or wins.
- The game continues until the player enters `quit`.

---

## Part 8 – Testing Your Program

Before submitting your work, verify that your program handles the following situations.

### Gameplay Testing

- [ ] Player wins when only the player's guess is correct.
- [ ] Computer wins when only the computer's guess is correct.
- [ ] A tie occurs when both guesses are correct.
- [ ] No winner occurs when neither guess is correct.
- [ ] XP is awarded only to the winner.
- [ ] XP is multiplied by the current round number.
- [ ] Scores and win counts are updated correctly.
- [ ] Statistics are displayed after round 1.
- [ ] The round number increases when the player continues.

### Input Validation Testing

- [ ] Player's hand accepts integers from 1 to 3.
- [ ] Player's hand rejects values outside the range.
- [ ] Player's hand handles nonnumeric and blank inputs.
- [ ] Player's guess accepts integers from 2 to 6.
- [ ] Player's guess rejects values outside the range.
- [ ] Player's guess handles nonnumeric and blank inputs.
- [ ] Play-again prompt accepts `yes` and `quit`.
- [ ] Play-again prompt rejects invalid responses.
- [ ] Invalid inputs do not crash the program.

### Program Structure Testing

- [ ] All five required functions are implemented.
- [ ] Functions accept the required parameters.
- [ ] Functions return the expected values.
- [ ] Predefined code remains unchanged.
- [ ] The `main()` function manages the game workflow.
- [ ] The program exits gracefully when the player quits.

---

## Submission Instructions

1. Complete the provided `morra.py` starter file.
2. Test your program to ensure all required functionality works.
3. Save your changes.
4. Commit and push your completed work to your GitHub Classroom repository.

**Reminder:** This mock exam is designed to prepare you for Practical Exam III. Focus on understanding the logic, using functions appropriately, and testing your program as you develop it.
