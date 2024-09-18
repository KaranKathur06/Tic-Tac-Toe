import tkinter as tk
from tkinter import messagebox
import random 

# FUNCTION TO CHECK FOR WINNER
def check_winner():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != '':
            return board[i][0]['text']
        if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != '':
            return board[0][i]['text']
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return board[0][0]['text']
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return board[0][2]['text']
    return None

# FUNCTION TO CHECK IF BOARD IS FULL OR NOT
def board_full():
    for row in board:
        for cell in row:
            if cell['text'] == '':
                return False
    return True

# FUNCTION TO HANDLE CLICK CALLS 
def cell_click(row, col):
    if board[row][col]['text'] == '' and not winner.get():
        # User's move
        board[row][col]['text'] = player.get()
        win = check_winner()
        if win:
            winner.set(win)
            if game_mode.get() == 'Computer':
                if win == 'X':
                    messagebox.showinfo("GAME OVER", "CONGRATS, YOU BEAT THE COMPUTER :)")
                else:
                    messagebox.showinfo("GAME OVER", "COMPUTER BEAT YOU :(")
            else:
                messagebox.showinfo("GAME OVER", f"Player {win} wins!")
        elif board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            # If it's the computer's turn, let the computer move
            if game_mode.get() == 'Computer' and player.get() == 'X':
                player.set('O')
                computer_move()  # Let computer make its move after the user
                win = check_winner()
                if win:
                    winner.set(win)
                    messagebox.showinfo("GAME OVER", "COMPUTER BEAT YOU :(")
                elif board_full():
                    messagebox.showinfo("Game Over", "It's a tie!")
                else:
                    player.set('X')  # Switch turn back to the player
            else:
                # If 1 vs 1 mode, just alternate players
                player.set('O' if player.get() == 'X' else 'X')

# FUNCTION FOR THE MOVE OF COMPUTER
def computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c]['text'] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col]['text'] = 'O'  # Computer places 'O' directly without triggering user click event

# FOR THE RESET OF THE GAME 
def reset_game():
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ''
    player.set('X')
    winner.set('')

# TO SET THE GAME MODE AND START THE GAME
def start_game(mode):
    game_mode.set(mode)
    game_setup_frame.pack_forget()
    game_frame.grid(row=0, column=0)
    reset_game()

# CREATING MAIN WINDOW
root = tk.Tk()
root.title("TIC TAC TOE")

# VARIABLES
player = tk.StringVar(value='X')
winner = tk.StringVar(value='')
game_mode = tk.StringVar(value='')

# GAME SETUP FRAME
game_setup_frame = tk.Frame(root)
game_setup_frame.grid(row=0, column=0, padx=20, pady=20)

tk.Label(game_setup_frame, text="PLEASE SELECT THE GAME MODE", font=('Helvetica', 14)).grid(row=0, column=0, columnspan=2, pady=10)
tk.Button(game_setup_frame, text="1 VS 1 WITH YOUR FRIEND", command=lambda: start_game('Friend')).grid(row=1, column=0, padx=10, pady=5)
tk.Button(game_setup_frame, text="BEAT THE COMPUTER", command=lambda: start_game('Computer')).grid(row=1, column=1, padx=10, pady=5)

# GAME FRAME
game_frame = tk.Frame(root)

# Create the board
board = [[None, None, None], [None, None, None], [None, None, None]]
for row in range(3):
    for col in range(3):
        button = tk.Button(game_frame, text='', font=('Helvetica', 20), width=15, height=3, 
                           command=lambda r=row, c=col: cell_click(r, c))
        button.grid(row=row, column=col)
        board[row][col] = button

# LABEL TO SHOW CURRENT PLAYER
player_label = tk.Label(game_frame, textvariable=player, font=('Helvetica', 14))
player_label.grid(row=3, column=0, columnspan=3)

# RESET BUTTON
reset_button = tk.Button(game_frame, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

# MAIN LOOP
root.mainloop()
