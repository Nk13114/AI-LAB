Condition 1
N = 8  # Board size


def print_board(board):
    """Function to print the chessboard."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check column for any queen
    for i in range(row):
        if board[i][col]:
            return False


    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False


    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False


    return True


def solve_n_queens(board, row):
    """Recursive function to solve N-Queens using backtracking."""
    if row >= N:  # All queens placed
        print_board(board)
        return True  # Return after first valid solution


    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1):  # Recur for next row
                return True
            board[row][col] = 0  # Backtrack


    return False


def solve():
    """Driver function to solve the problem."""
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Solution does not exist")
    else:
        print("One possible solution is shown above.")


# Run the solver
solve()


Condition 2
N = 8  # Size of the chessboard


def print_board(board):
    """Function to print the chessboard."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False


    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False


    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False


    return True


def solve_n_queens(board, row):
    """Recursive function to place one queen at a time using backtracking."""
    if row >= N:  # All queens placed
        return True  


    for col in range(N):
        if is_safe(board, row, col):  # Check if safe
            board[row][col] = 1  # Place queen
            print(f"Placing queen at Row {row}, Column {col}:")
            print_board(board)


            if solve_n_queens(board, row + 1):  # Recur for next row
                return True


            board[row][col] = 0  # Backtrack
            print(f"Backtracking from Row {row}, Column {col}:")
            print_board(board)


    return False


def solve():
    """Driver function to solve the 8 Queens problem."""
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("Solution does not exist")
    else:
        print("Final solution:")


# Run the solver
solve()