class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in seen:
                    print("row")
                    return False
                else:
                    seen[board[i][j]] = 1
        # column
        i = 0
        while i < 9:
            seen = {}
            for row in board:
                if row[i].isdigit() and row[i] in seen:
                    print("col")
                    return False
                else:
                    seen[row[i]] = 1
            i += 1
        # box
        for i in range(3):
            for j in range(3):
                if not check_box(i*3,j*3,board):
                    print("box")
                    return False
                else:
                    continue
        return True

def check_box(starting_i:int, starting_j:int, board: List[List[str]]) -> bool:
    i = 0
    j = 0
    seen = {}
    while i < 3:
        j = 0
        while j < 3:
            if board[starting_i +i][starting_j + j].isdigit() and board[starting_i +i][starting_j + j] in seen:
                print("box")
                return False
            else:
                seen[board[starting_i +i][starting_j + j]] = 1
            j += 1
        i +=1
    return True



