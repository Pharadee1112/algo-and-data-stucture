board = []
for _ in range(8):
    board.append(list(map(int, input().split())))

start = None
for row in range(8):
    for col in range(8):
        if board[row][col] == 2:
            start = (row, col)

diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def dfs(black_row, black_col):
    max_captured = 0

    for row_step, col_step in diagonal_directions:
        white_row = black_row + row_step
        white_col = black_col + col_step
        land_row = black_row + 2 * row_step
        land_col = black_col + 2 * col_step

        if not (0 <= white_row < 8 and 0 <= white_col < 8):
            continue
        if not (0 <= land_row < 8 and 0 <= land_col < 8):
            continue

        if board[white_row][white_col] == 1 and board[land_row][land_col] == 0:

            board[white_row][white_col] = 0
            board[black_row][black_col] = 0
            board[land_row][land_col] = 2

            max_captured = max(max_captured, 1 + dfs(land_row, land_col))

            board[white_row][white_col] = 1
            board[black_row][black_col] = 2
            board[land_row][land_col] = 0

    return max_captured


print(dfs(start[0], start[1]))
