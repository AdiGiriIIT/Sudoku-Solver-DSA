def is_valid(board, row, col, number):
    for n in range(9):
        if board[row][n] == number or board[n][col] == number:
            return False
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[square_row + i][square_col + j] == number:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if is_valid(board, row, col, number):
                        board[row][col] = number
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def validate_input(user_grid, solution_grid):
    """Compares user input to solved board and returns a grid of status flags."""
    status = []
    for i in range(9):
        row = []
        for j in range(9):
            if user_grid[i][j] == 0:
                row.append("empty")
            elif user_grid[i][j] == solution_grid[i][j]:
                row.append("correct")
            else:
                row.append("wrong")
        status.append(row)
    return status
