'''
Sudoku Program - Tommy Trinh
Solved using backtracking algorithm
    1. Start with an empty square.
    2. Input possible numbers one at a time until you get one (the first one) 
    that works.
    2. Save the input and repeat step 2 on the next possible square.
    3. Repeat steps 2 and 3 on next empty squares.
    4. If you get to a square where the solution cannot be completed, go to 
    the previous square and check if there is another number that will 
    satisfy the condition. (backtracking)
    5. If there is a number that will satisfy the condition, save it and do 
    steps 2-3. If not, do step 4. (backtrack again)
'''

sudoku_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
    ]
       
#displays the sudoku board
def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
#finds an empty square and return (row, column)
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return ((i, j))
    return None
            
#checks if number is valid
def valid(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #check 3x3 square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
          
#solving board, done with recursion  
def solve(board):
    #board is done
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find
    
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i
            
            if solve(board):
                return True
            
            board[row][column] = 0
    return False

print("--- BEGINNING BOARD ---")
print_board(sudoku_board)
solve(sudoku_board)
print("\n")
print("------- SOLUTION ------")
print_board(sudoku_board)
        
    