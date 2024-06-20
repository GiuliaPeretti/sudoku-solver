import numpy as np
class SudokuGrid:
    def __init__(self):
        # self.grid=np.zeros([9,9], dtype=int)
        self.grid=([[1,0,7,0,0,6,4,5,0],
                    [0,2,5,3,4,0,0,0,8],
                    [0,6,0,0,0,1,0,7,0],
                    [0,5,3,0,0,0,0,2,9],
                    [6,1,0,0,0,9,8,0,0],
                    [0,0,0,6,0,2,0,0,7],
                    [0,0,1,0,9,3,2,0,0],
                    [0,0,8,0,0,0,0,0,0],
                    [0,4,0,0,7,8,5,9,1]])
        self.bold=([[1,0,1,0,0,1,1,1,0],
                    [0,1,1,1,1,0,0,0,1],
                    [0,1,0,0,0,1,0,1,0],
                    [0,1,1,0,0,0,0,1,1],
                    [1,1,0,0,0,1,1,0,0],
                    [0,0,0,1,0,1,0,0,1],
                    [0,0,1,0,1,1,1,0,0],
                    [0,0,1,0,0,0,0,0,0],
                    [0,1,0,0,1,1,1,1,1]])

    def print_grid(self):
        for i in range (0,9):
            if ((i)%3==0 and i!=0):
                print("------+-------+------")
            for j in range (0,9):
                print(self.grid[i][j], end=' ')
                if ((j+1)%3==0 and j!=8):
                    print("|", end=' ')
            print()    
        print() 
    
    def set_number(self, row, col, n):
        self.grid[row][col]=n

    def get_pos(self,row,col):
        return(self.grid[row][col])
    
    def get_bold(self, row, col):
        return(self.bold[row][col])
        
