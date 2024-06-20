class SudokuGrid:
    def __init__(self):
        self.grid=[[0]*9]*9

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
        self.grid[col][row]=n
        

d=SudokuGrid()
d.set_number(1,1,4) 
d.print_grid()