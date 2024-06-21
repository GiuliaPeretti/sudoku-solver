import numpy as np
import random

grid=([[1,0,7,0,0,6,4,5,0],
      [0,2,5,3,4,0,0,0,8],
      [0,6,0,0,0,1,0,7,0],
      [0,5,3,0,0,0,0,2,9],
      [6,1,0,0,0,9,8,0,0],
      [0,0,0,6,0,2,0,0,7],
      [0,0,1,0,9,3,2,0,0],
      [0,0,8,0,0,0,0,0,0],
      [0,4,0,0,7,8,5,9,1]])

def is_possible(grid, x, y, n):
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
    return None

def solve(grid):
    find = find_empty(grid)
    if not find:
        return (True, grid)
    else:
        x, y = find
    
    for i in range(1,10):
        if(is_possible(grid,x,y,i)):
            grid[y][x] = i
            b,grid=solve(grid)
            if b:
                print("finito")
                return (True, grid)
            
            grid[y][x] = 0
    return (False, grid)

def print_grid(grid):
    for i in range (0,9):
        if ((i)%3==0 and i!=0):
            print("------+-------+------")
        for j in range (0,9):
            print(grid[i][j], end=' ')
            if ((j+1)%3==0 and j!=8):
                print("|", end=' ')
        print()    
    print() 
        
def init_grid():
    
    grid=generate_grid()
    print_grid(grid)
    # grid=[[1,0,7,0,0,6,4,5,0],
    #             [0,2,5,3,4,0,0,0,8],
    #             [0,6,0,0,0,1,0,7,0],
    #             [0,5,3,0,0,0,0,2,9],
    #             [6,1,0,0,0,9,8,0,0],
    #             [0,0,0,6,0,2,0,0,7],
    #             [0,0,1,0,9,3,2,0,0],
    #             [0,0,8,0,0,0,0,0,0],
    #             [0,4,0,0,7,8,5,9,1]]
    
    # grid=[[1,3,7,9,8,6,4,5,2],
    #             [9,0,5,3,0,7,1,0,8],
    #             [8,6,4,5,2,1,9,7,3],
    #             [7,5,3,8,1,4,6,2,9],
    #             [6,0,2,7,0,9,8,0,5],
    #             [4,8,9,6,5,2,3,1,7],
    #             [5,7,1,4,9,3,2,8,6],
    #             [2,0,8,1,0,5,7,0,4],
    #             [3,4,6,2,7,8,5,9,1]       
    #             ]


    grid_base=[ [1,0,1,0,0,1,1,1,0],
                [0,1,1,1,1,0,0,0,1],
                [0,1,0,0,0,1,0,1,0],
                [0,1,1,0,0,0,0,1,1],
                [1,1,0,0,0,1,1,0,0],
                [0,0,0,1,0,1,0,0,1],
                [0,0,1,0,1,1,1,0,0],
                [0,0,1,0,0,0,0,0,0],
                [0,1,0,0,1,1,1,1,1]]
    
    # grid_solved=grid.copy
    # _,grid_solved=solve(grid)
    grid_solved=[   [1,3,7,9,8,6,4,5,2],
                    [9,2,5,3,4,7,1,6,8],
                    [8,6,4,5,2,1,9,7,3],
                    [7,5,3,8,1,4,6,2,9],
                    [6,1,2,7,3,9,8,4,5],
                    [4,8,9,6,5,2,3,1,7],
                    [5,7,1,4,9,3,2,8,6],
                    [2,9,8,1,6,5,7,3,4],
                    [3,4,6,2,7,8,5,9,1]       
                    ]

    return(grid, grid_base, grid_solved)

def generate_grid():
    size=9
    grid=np.zeros([9,9], dtype=int)
    for r in range (size):
        row=[]
        c=0
        numbers=list(range(1,size+1))
        while c!=size:
            number=random.choice(numbers)
            repeat_counter=0
            while (is_possible(grid, r, len(row), number)==False):
                number=random.choice(numbers)
                repeat_counter+=1
                if repeat_counter==size:
                    break
            else:
                grid[r][c]=number
                c+=1
    return(grid)


#   grid[row][col]=0         

grid=[[0]*9]*9    
print_grid(grid)