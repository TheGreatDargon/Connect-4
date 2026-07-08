import numpy as np
import random

cols = 7
rows = 6
connect = 4

theBoard = np.array([[" 0 " for i in range(cols)] for j in range(rows)])

def printBoard():
    for i in range(0,6):
        print(theBoard[i])

def is_Empty(row, col):
    if theBoard[row][col] == " 0 ":
        return True
    else:
        return False

def is_Winner(piece):

    # Check Rows
    for r in range(rows):
        for c in range (cols - connect + 1):
            if (theBoard[r][c] == piece and
                theBoard[r][c+1] == piece and
                theBoard[r][c+2] == piece and
                theBoard[r][c+3] == piece):
                return True
        
    # Check Columns
    for c in range(cols):
        for r in range (rows - connect + 1):
            if (theBoard[r][c] == piece and
                theBoard[r+1][c] == piece and
                theBoard[r+2][c] == piece and
                theBoard[r+3][c] == piece):
                return True
            
    # Check Diagonals 
    # up right
    for r in range(rows - connect + 1):
        for c in range(rows - connect + 1):
            if (theBoard[r][c] == piece and
                theBoard[r+1][c+1] == piece and
                theBoard[r+2][c+2] == piece and
                theBoard[r+3][c+3] == piece):
                return True
    # down right
    for r in range(rows - connect + 1):
        for c in range(connect-1,cols):
            if (theBoard[r][c] == piece and
                theBoard[r+1][c-1] == piece and
                theBoard[r+2][c-2] == piece and
                theBoard[r+3][c-3] == piece):
                return True
            
    return False    
def makeMove(player, move):
    if move < 0 or move > 6:
        print("You didn't put the piece in a column, Try again.")
        return False
    for i in range(rows-1, -1, -1):
        if is_Empty(i, move) == True:
            theBoard[i][move] = player
            return True
            break

def onePlayer():
    player1 = " R "
    comp = " Y "

def twoPlayer():
    player1 = " R "
    player2 = " Y "

    moved = False

    while is_Winner(player1) is False or is_Winner(player2) is False:
        move = input(f"Player 1 choose a column to place a piece (1-{cols}): ")
        while makeMove(player1, int(move)-1) != True:
            move = input(f"Player 1 choose a column to place a piece (1-{cols}): ")
            print(f"{player1}, That column is full, please choose another column.")
            printBoard()
            continue
        printBoard()
        if is_Winner(player1) is True:
            print(f"{player1} wins!")
            return 0
        move = input(f"Player 2 choose a column to place a piece (1-{cols}): ")
        while makeMove(player2, int(move)-1) != True:
            move = input(f"Player 2 choose a column to place a piece (1-{cols}): ")
            print(f"{player2}, That column is full, please choose another column.")
            printBoard()
            continue
        printBoard()
        if is_Winner(player2) is True:
            print(f"{player2} wins!")
            return 0
        



def main():
    choice = 0
    while choice == 0:
        choice = int(input("Welcome to Connect-4, Please choose a game mode:\n1. One Player\n2. Two Player\n3. Quit\n"))
        if choice == 1:
            onePlayer()
        elif choice == 2:
            twoPlayer()
        else:
            return 0



main()