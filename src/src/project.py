import random

board = [[0 for _ in range(10)] for _ in range(10)]
uncovered_board = [[-1 for _ in range(10)] for _ in range(10)]

def count_adjacent_mines(row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < 10 and 0 <= j < 10 and board[i][j] == 1:
                count += 1
    return count


def reveal_cell(row, col):
    uncovered_board[row][col] = count_adjacent_mines(row, col)
    if uncovered_board[row][col] == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < 10 and 0 <= j < 10 and uncovered_board[i][j] == -1:
                    reveal_cell(i, j)


def display_board():
    print("-" * 20)
    for row in range(10):
        for col in range(10):
            if uncovered_board[row][col] == -1:
                print(end="| ")
            else:
                print(uncovered_board[row][col], end=" ")
        print("")
    print("-" * 20)


def check_win():
    for row in range(10):
        for col in range(10):
            if board[row][col] == 0 and uncovered_board[row][col] == -1:
                return False
    return True

def main():
    total_mines = int(input("How many Mines? (Max 25) "))
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

    game_over = False

    while not game_over:
        display_board()

        row = int(input("Guess a row (1-10): ")) - 1
        col = int(input("Guess a col (1-10): ")) - 1

        if board[row][col] == 1:
            print("You hit a Mine!")
            print("GAME OVER")
            game_over = True
        else:
            reveal_cell(row, col)

        if check_win():
            print("Congratulations! You won the game.")
            game_over = True

    if game_over:
        display_board()

if __name__ == "__main__":
  main()