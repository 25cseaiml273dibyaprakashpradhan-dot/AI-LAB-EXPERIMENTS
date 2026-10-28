def print_board(board):
    for row in board:
        print(" ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
        
    return False

# Initialize board and player
board = [[" " for _ in range(3)] for _ in range(3)]
player = "x"

while True:
    print("\nCurrent Board")
    print_board(board)
    
    print(f"Player {player}'s turn")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    
    if board[row][col] == " ":
        board[row][col] = player
        
        if check_winner(board):
            print("\nFinal Board:")
            print_board(board)
            print(f"Player {player} wins!")
            break
            
        # Check for draw (if board is full)
        if all(cell != " " for row_cells in board for cell in row_cells):
            print("\nFinal Board:")
            print_board(board)
            print("Game Over!")
            break
            
        player = "o" if player == "x" else "x"
    else:
        print("Cell already OCCUPIED. Try again.")
