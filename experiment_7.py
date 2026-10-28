def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col):
    # Check this column on upper rows
    for i in range(row):
        if board[i][col] == 'Q':
            return False
            
    # Check upper diagonal on left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
        
    # Check upper diagonal on right side
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
        
    return True

def solve(board, row):
    if row == 8:
        return True
        
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            
            if solve(board, row + 1):
                return True
                
            board[row][col] = '.'
            
    return False

# MAIN PROGRAM
board = [['.' for _ in range(8)] for _ in range(8)]

if solve(board, 0):
    print("solution for 8 queen problem:")
    print_board(board)
else:
    print("NO solution exist")

print("Result:-")
print("the 8 queen problem successfully solved using python back-tracking technique.")
