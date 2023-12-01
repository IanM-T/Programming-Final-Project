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


                
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col(pos)
                    if self.board[row][col] == None:
                        self.reveal_cell(screen, row, col)
                        self.check_game_over()
                    elif self.board[row][col] == 'M':
                        self.reveal_mines(screen)
                        self.running = False

            pygame.display.flip()

        pygame.quit()

    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                cell = self.board[row][col]
                if cell == None:
                    pygame.draw.rect(screen, (128, 128, 128), (col * 32, row * 32, 32, 32))
                elif cell == 'M':
                    pygame.draw.rect(screen, (255, 0, 0), (col * 32, row * 32, 32, 32))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (col * 32, row * 32, 32, 32))
                    if cell != 0:
                        font = pygame.font.Font(None, 32)
                        text = font.render(str(cell), True, (0, 0, 0))
                        text_pos = text.get_rect(center=(col * 32 + 16, row * 32 + 16))
                        screen.blit(text, text_pos)

    def get_row_col(self, pos):
        row = pos[1] // 32
        col = pos[0] // 32
        return row, col

    def reveal_cell(self, screen, row, col):
        if self.board[row][col] == None:
            if self.count_adjacent_mines(row, col) == 0:
                self.reveal_adjacent_cells(screen, row, col)
            else:
                self.board[row][col] = self.count_adjacent_mines(row, col)
                self.draw(screen)

    def reveal_mines(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 'M':
                    self.board[row][col] = 'X'
        self.draw(screen)

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i >= 0 and i < len(self.board) and
                    j >= 0 and j < len(self.board[0]) and
                    (i, j) != (row, col) and
                    self.board[i][j] == 'M'):
                    count += 1
        return count

    def reveal_adjacent_cells(self, screen, row, col):
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i >= 0 and i < len(self.board) and
                    j >= 0 and j < len(self.board[0]) and
                    self.board[i][j] == None):
                    self.reveal_cell(screen, i, j)

def check_game_over(self):
    cells_revealed = 0
    for row in range(len(self.board)):
        for col in range(len(self.board[0])):
            if self.board[row][col] == None or self.board[row][col] == 'M':
                cells_revealed += 1

    if cells_revealed == 0:
        print("You win!")
        self.running = False

    for row in range(len(self.board)):
        for col in range(len(self.board[0])):
            if self.board[row][col] == 'X':
                print("Game Over!")
                self.reveal_mines(screen)
                self.running = False