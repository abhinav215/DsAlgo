
def isValid(num,row,column,board,n):
  for i in range(n):
    if board[row][i]==str(num):
      return False
    if board[i][column]==str(num):
      return False
    if board[3*(row//3)+(i//3)][3*(column//3)+(i%3)]==str(num):
      return False
  return True


def answer(n,board):
  for row in range(n):
    for column in range(n):
      if board[row][column]==".":
        for i in range(1,n+1):
          if isValid(i,row,column,board,n):
            board[row][column]=str(i)
            if answer(n,board):
              return True
            board[row][column]="."
        return False
  print(board)
  return True


def solveSudoku(board):
  n = len(board)
  answer(n,board)
  print(board)



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)