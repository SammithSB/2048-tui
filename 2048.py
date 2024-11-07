import random
import os

SIZE = 4

def new_game():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-' * (SIZE * 7 + 1))
    for row in board:
        print('|', end='')
        for num in row:
            if num == 0:
                print('      |', end='')
            else:
                print(f'{num:^6}|', end='')
        print()
        print('-' * (SIZE * 7 + 1))

def transpose(board):
    return [list(row) for row in zip(*board)]

def reverse(board):
    return [row[::-1] for row in board]

def merge(row):
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False
    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])
    merged_row += [0] * (SIZE - len(merged_row))
    return merged_row

def move_left(board):
    new_board = []
    for row in board:
        new_row = merge(row)
        new_board.append(new_row)
    return new_board

def move_right(board):
    new_board = []
    for row in board:
        new_row = merge(row[::-1])
        new_board.append(new_row[::-1])
    return new_board

def move_up(board):
    transposed = transpose(board)
    moved = move_left(transposed)
    return transpose(moved)

def move_down(board):
    transposed = transpose(board)
    moved = move_right(transposed)
    return transpose(moved)

def is_game_over(board):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return False
            if i < SIZE - 1 and board[i][j] == board[i + 1][j]:
                return False
            if j < SIZE - 1 and board[i][j] == board[i][j + 1]:
                return False
    return True

def main():
    board = new_game()
    while True:
        print_board(board)
        move = input("Enter move (w/a/s/d or q to quit): ").lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print("Invalid input! Please use 'w', 'a', 's', 'd' to move or 'q' to quit.")
            continue
        if move == 'q':
            print("Game terminated.")
            break
        if move == 'a':
            new_board = move_left(board)
        elif move == 'd':
            new_board = move_right(board)
        elif move == 'w':
            new_board = move_up(board)
        elif move == 's':
            new_board = move_down(board)
        if new_board != board:
            board = new_board
            add_new_tile(board)
            if is_game_over(board):
                print_board(board)
                print("Game Over!")
                break
        else:
            print("No tiles moved. Try a different direction.")

if __name__ == "__main__":
    main()
 