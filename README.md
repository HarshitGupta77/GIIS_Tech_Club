# Hand Cricket Game

## Overview
This is a simple console-based Hand Cricket game implemented in Python. Players can compete against a computer by choosing to bat or bowl after winning a toss. The game simulates a basic version of cricket where players take turns attempting to score runs, and the game ends when a player or the computer gets out.

## Features
- **Toss**: Players can choose either "odd" or "even" to win the toss.
- **Batting and Bowling Choices**: Players can choose to bat or bowl after winning the toss. If the player loses the toss, the computer randomly chooses.
- **Randomized Outcomes**: The computer randomly generates runs when batting, and the player must guess the number to score runs.
- **Out Mechanism**: Players and the computer can get out by matching their guessed number with the opponent's batting score.
- **Innings**: The game consists of two innings where the player and the computer take turns batting and bowling.
- **Victory Conditions**: The game announces the winner based on the scores at the end of both innings.

## How to Play
1. **Start the Game**: Run the script in a Python environment.
2. **Toss**: Choose "odd" or "even". Input your toss number between 1 to 6.
3. **Bat or Bowl**: If you win the toss, choose to bat or bowl. If you lose, the computer will make a choice.
4. **Gameplay**:
   - If you bowl, input a number between 1 to 6 to try to get the computer out. If your number matches the computer's score, you're out.
   - If you bat, input your score to accumulate runs. If your score matches the computer's, you're out.
5. **Winning**: The game announces the winner after both innings based on the runs scored.

## Requirements
- Python 3.x
- The `colorama` library for colored terminal output (install via pip if not already installed):
  ```bash
  pip install colorama
  ```

## Code Structure
- The game logic is structured into several sections for clarity, including:
  - Toss mechanics
  - Batting and bowling decisions
  - Scorekeeping and out conditions

## Conclusion
This Hand Cricket game serves as an introduction to basic game development concepts in Python and can be extended with additional features such as scoring history, multiple players, and more complex rules to enhance the gameplay experience. Enjoy playing!
