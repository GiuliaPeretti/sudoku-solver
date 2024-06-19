grid=[[1,0,7,0,0,6,4,5,0],
      [0,2,5,3,4,0,0,0,8],
      [0,6,0,0,0,1,0,7,0],
      [0,5,3,0,0,0,0,2,9],
      [6,1,0,0,0,9,8,0,0],
      [0,0,0,6,0,2,0,0,7],
      [0,0,1,0,9,3,2,0,0],
      [0,0,8,0,0,0,0,0,0],
      [0,4,0,0,7,8,5,9,1]]

def is_possible(x, y, n):
    global grid
    for i in range (0,9):
        if (grid[y][i] == n):
            return False
    for i in range (0,9):
        if (grid[i][x] == n):
            return False
    x0 = (x//3)*3
    y0= (y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if (grid[x0+i][y0+j] == n):
                return False
    return True