board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def find_next_empty(bd):
    for row in range(len(bd)):
        for col in range(len(bd[0])):
            if bd[row][col] == 0:
                return row, col
    return False


def is_valid_check(bd, num, coord_x, coord_y):
    trans_mat = list(zip(*bd))
    square_x = (coord_x // 3) * 3
    square_y = (coord_y // 3) * 3

    for i, elem in enumerate(bd[coord_x]):
        if i != coord_y and elem == num:
            return False

    for i, elem in enumerate(trans_mat[coord_y]):
        if i != coord_x and elem == num:
            return False

    for x in range(square_x, square_x + 3):
        for y in range(square_y, square_y + 3):
            if bd[x][y] == num and (x, y) != (coord_x, coord_y):
                return False

    return True


def solve(bd):
    next_empty = find_next_empty(bd)
    if not next_empty:
        return True
    else:
        x, y = next_empty

    for number in range(1, 10):
        if is_valid_check(bd, number, x, y):
            bd[x][y] = number
            if solve(bd):
                return True
            bd[x][y] = 0

    return False


def print_board(bd):
    for row in range(len(bd)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - - -")
        for col in range(len(bd[0])):
            if col != 0:
                print("  ", end="")
            if col % 3 == 0 and col != 0:
                print("|", end="")
                print("  ", end="")
            print(bd[row][col], end="")
        print()


check = solve(board)
if check is False:
    print("No solution")
else:
    print_board(board)
