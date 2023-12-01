import random


board = [[0 for _ in range(10)] for _ in range(10)]
uncovered_board = [[-1 for _ in range(10)] for _ in range(10)]
total_mines = int(input("How many Mines?"))
if total_mines > 25:
    print("Impossible. Setting to 5 as default.")
    total_mines = 5

placed_mines = 0
while placed_mines < total_mines:
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    if board[row][col] == 0:
        board[row][col] = 1
        placed_mines += 1


def count_adjacent_mines(row, col):
    """
    Counts the number of mines surrounding a cell.
    """
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < 10 and 0 <= j < 10 and board[i][j] == 1:
                count += 1
    return count


def reveal_cell(row, col):
    """
    Reveals a cell and its surrounding cells if it's empty.
    """
    uncovered_board[row][col] = count_adjacent_mines(row, col)
    if uncovered_board[row][col] == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < 10 and 0 <= j < 10 and uncovered_board[i][j] == -1:
                    reveal_cell(i, j)


def display_board():
    """
    Prints the current state of the board.
    """
    print("-" * 40)
    for row in range(10):
        print("|", end="")
        for col in range(10):
            if uncovered_board[row][col] == -1:
                print(" ", end=" | ")
            else:
                print(uncovered_board[row][col], end=" ")
        print("")
    print("-" * 40)


def check_win():
    """
    Checks if the player has won the game.
    """
    for row in range(10):
        for col in range(10):
            if board[row][col] == 0 and uncovered_board[row][col] == -1:
                return False
    return True


guesses_left = 25 - total_mines

display_board()
while guesses_left > 0 and not check_win():
    row = int(input("Guess a row (1-10):")) - 1
    col = int(input("Guess a col (1-10):")) - 1
    if board[row][col] == 1:
        print("You hit a Mine.")
        print("GAME OVER")
        display_board()
        break
    else:
        reveal_cell(row, col)
        display_board()
        guesses_left -= 1

if check_win():
    print("Congratulations! You won the game.")
else:
    print("You ran out of guesses. Better luck next time!")