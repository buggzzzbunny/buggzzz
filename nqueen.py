def is_safe(row, col, board):
    irow, icol = row, col
    
    while irow >= 0 and icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        irow -= 1
        icol -= 1
    
    irow, icol = row, col
    while irow < len(board) and icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        irow += 1
        icol -= 1
    
    while icol >= 0:
        if board[row][icol] == 'Q':
            return False
        icol -= 1
    
    return True

def solve_n_queens(n):
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    find_board(n, solutions, board, 0)
    return solutions 

def find_board(n, solutions, board, col):
    if col == n:
        solutions.append([''.join(row) for row in board])
        return
    
    for row in range(n):
        if is_safe(row, col, board):
            board[row][col] = 'Q'
            find_board(n, solutions, board, col + 1)
            board[row][col] = '.'

if __name__ == '__main__':
    n = int(input("Enter the number of rows and columns: "))
    solutions = solve_n_queens(n)
    
    for solution in solutions:
        for row in solution:
            print(row)
        print("------------------------------------------------")
        print()

    print("Total number of outcomes:", len(solutions))
