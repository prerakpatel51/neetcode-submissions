class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for i in range(9):
            dic={}
            dic2={}
            for j in range(9):
                
                if board[i][j].isnumeric() :
                    if board[i][j]in dic:
                        return False
                    dic[board[i][j]] = 1
     
                   
                if board[j][i].isnumeric():
                    if board[j][i]in dic2:
                        return False
                    dic2[board[j][i]] = 1
        

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                print("Block starting at:", box_row, box_col)
                dic3={}
                for i in range(3):
                    
                    for j in range(3):
                       
                       
                        if board[box_row + i][box_col+j].isnumeric() :
                            if board[box_row + i][box_col+j]in dic3:
                                return False
                            dic3[board[box_row + i][box_col+j]] = 1
           
                        
        return True
      