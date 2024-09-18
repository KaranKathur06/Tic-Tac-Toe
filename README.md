# Tic Tac Toe
==========================

## Overview
------------

This is a simple implementation of the classic Tic Tac Toe game using Python and the Tkinter library for the graphical user interface. The game allows two players to play against each other, or a single player to play against the computer.

## Features
------------

*   Two game modes: 1 vs 1 with a friend, or against the computer
*   Simple and intuitive graphical user interface
*   Automatic switching between players
*   Winner detection and announcement
*   Reset button to start a new game
*   1 vs 1: Play with a friend on the same computer.
*   Beat the Computer: Play against an AI that randomly picks its moves.
*   Graphical Interface: Uses tkinter to provide a simple, easy-to-use interface.
*   Winning Logic: Detects row, column, and diagonal wins.
*   Reset Option: Allows resetting the game at any point.
*   Turn-Based Play: Alternates between player turns and handles game-end conditions (win, loss, or draw).

## Requirements
------------

*   Python 3.x
*   Tkinter library (comes bundled with Python)

## How to Run
--------------

*   You need Python 3.x installed.
*   tkinter should be installed (usually included with Python).
*   Clone or Download the repository: `git clone <repo_url>`
*   Navigate to the directory where the script is located and run the game: `python tictactoe.py`
*   The game window will appear with the option to select the game mode:
    *   1 vs 1: Play with a friend.
    *   Beat the Computer: Challenge the AI.

## Gameplay
------------

*   Player X always goes first.
*   Click on an empty cell to make your move.
*   If playing against the computer, it will make its move automatically after you.
*   Reset the game:
    *   Click the "Reset" button to start a new game.

## How It Works
----------------

*   The board is a 3x3 grid of buttons that players click to place their mark (X or O).
*   The game checks for a winner after every move by evaluating all rows, columns, and diagonals.
*   If all cells are filled and no winner is found, the game declares a tie.
*   In Beat the Computer mode, after the player's move, the computer will make a random valid move until the game ends.

## Screenshots
--------------

### Game Mode Selection:

![Game Mode Selection](screenshot1.png)

### In-Game:

![In-Game](screenshot2.png)

## Customization
--------------

You can modify the board size, change fonts, or even enhance the AI for smarter moves by editing the code.

## License
----------

This code is released under the MIT License. See the LICENSE file for details.

## Contributing
------------

Contributions are welcome! If you'd like to improve the game or fix a bug, please submit a pull request.
