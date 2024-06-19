import numpy as np

grid=([[1,0,7,0,0,6,4,5,0],
      [0,2,5,3,4,0,0,0,8],
      [0,6,0,0,0,1,0,7,0],
      [0,5,3,0,0,0,0,2,9],
      [6,1,0,0,0,9,8,0,0],
      [0,0,0,6,0,2,0,0,7],
      [0,0,1,0,9,3,2,0,0],
      [0,0,8,0,0,0,0,0,0],
      [0,4,0,0,7,8,5,9,1]])

def is_possible(x, y, n):
    global grid
    print(np.array(grid))
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

def find_empty(grid):
    for x in range(0,9):
        for y in range(0,9):
            if (grid[y][x]==0):
                return(x,y)
    return (-1,-1)

def solve(grid):
    x,y=find_empty(grid)
    if(x==-1):
        return True
    


def print_grid(grid):
    for i in range (0,9):
        if ((i+1)%3==0 and i!=8):
            print("------+-------+------")
        for j in range (0,9):
            print(grid[i][j], end=' ')
            if ((j+1)%3==0 and j!=8):
                print("|", end=' ')
        print()    
        
            

    
print(print_grid(grid))