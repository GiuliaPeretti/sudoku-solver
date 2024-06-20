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
        self.solved=([[1,3,7,9,8,6,4,5,2],
                      [9,2,5,3,4,7,1,6,8],
                      [8,6,4,5,2,1,9,7,3],
                      [7,5,3,8,1,4,6,2,9],
                      [6,1,2,7,3,9,8,4,5],
                      [4,8,9,6,5,2,3,1,7],
                      [5,7,1,4,9,3,2,8,6],
                      [2,9,8,1,6,5,7,3,4],
                      [3,4,6,2,7,8,5,9,1]       
                      ])


        self.solved=self.grid.copy()
        self.solved=self.solve(self.solved, 0, 0)[1]
        

    def print_grid(self, g):
        for i in range (0,9):
            if ((i)%3==0 and i!=0):
                print("------+-------+------")
            for j in range (0,9):
                print(g[i][j], end=' ')
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
        
    def generate_bold(self):
        pass

    def get_solved(self):
        return(self.solved)
    
    def solve(self, solved, row, col):
        if row==9:
            return (True, solved)
        elif col==9:
            return self.solve(solved, row+1,0)
        elif solved[row][col] != 0:
            return self.solve(solved, row, col+1)
        else:
            for k in range(1,10):
                if self.is_possible(solved, row, col, k):
                    solved[row][col] = k
                    if self.solve(solved, row, col+1)[0]:
                        return (True, solved)
                    solved[row][col]=0
            return (False, solved)

                

        


        # find = self.find_empty(self.solved)
        # if not find:
        #     return True
        # else:
        #     x, y = find
        
        # for i in range(1,10):
        #     if(self.is_possible(self.solved,x,y,i)):
        #         print(str(i)+" possibile")
        #         self.solved[y][x] = i
        #         if self.solve():
        #             print("finito")
        #             return True
                
        #         self.solved[y][x] = 0
        # print("return false " +str(x)+" "+str(y))
        # return False
    
    def is_possible(self, grid, x, y, n):
        for i in range (0,9):
            if (i!=x and grid[y][i] == n):
                return False
        for i in range (0,9):
            if (i!=y and grid[i][x] == n):
                return False
        x0 = (x//3)*3
        y0= (y//3)*3

        for i in range(0,3):
            for j in range(0,3):
                if (grid[x0+i][y0+j] == n):
                    return False
        return True

    def find_empty(self, grid):
        for x in range(0,9):
            for y in range(0,9):
                if (grid[y][x]==0):
                    return(x,y)
        return None
    
    def prova(self, r, c, n):
        self.solved[r][c]=n

    def get_grid(self):
        return(self.grid)

    # def is_correct(self, row, col, n):
    #     if self.solved[row][col]
        
        
gr=SudokuGrid()
print(gr.get_solved())
print(gr.get_grid())



