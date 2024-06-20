import pygame
from settings import *
from sudoku_solver import *
from random import sample
import random 

def draw_background():
    screen.fill((200,200,200))
    grid_width=draw_grid()
    draw_numbers(grid_width)
    return grid_width

def draw_grid():
    s=SCREEN_HEIGHT-20
    for i in range (0,10):
        if (i%3==0 or i==0 or i==9):
            width=3
        else:
            width=1
        pygame.draw.line(screen, (0 ,0,0),(s/9*i+9,9),(s/9*i+9,s+9), width)
        pygame.draw.line(screen, (0,0,0),(9,s/9*i+9),(s+9,s/9*i+9), width)
    return(s)

def draw_numbers(grid_width):
    for row in range (0,9):
        for col in range(0,9):
            output=grid[row][col]
            if(output!=0):
                if (grid_black[row][col]==1):
                    color=(0,0,0)
                elif (grid_solved[row][col]!=grid[row][col]):
                    color=(255,0,0)
                else:
                    color=(0,0,255)
                n_text=font.render(str(output), True, color)

                screen.blit(n_text, (col*(grid_width//9)+24, row*(grid_width//9)+18))

def draw_number(row, col, n):
    if (grid_black[row][col]==1):
        color=(0,0,0)
    elif (grid_solved[row][col]!=n):
        color=(255,0,0)
    else:
        color=(0,0,255)
    if(n!=0):
        n_text=font.render(str(n), True, color)
        screen.blit(n_text, (col*(grid_width//9)+24, row*(grid_width//9)+18))

def set_cella(xy, prev_xy):
    _=draw_background()
    col=xy[0]
    row=xy[1]

    if(col>grid_width or row>grid_width):
        return((-1,-1))

    col= int(col//(grid_width/9))
    row = int(row//(grid_width/9))

    if(prev_xy[0]==col and prev_xy[1]==row):
        _=draw_background()
        return((-1,-1))
    
    if (col<=grid_width and row<=grid_width):
        offset1=10
        offset2=10
        offset3=col+5-(col%3)
        offset4=row+5-(row%3)
        if(col%3==0):
            offset1+=1
            offset3-=2
        if(row%3==0):
            offset2+=1
            offset4-=2
        if((col-1)%3==0):
            offset3-=3
        if((row-1)%3==0):
            offset4-=3
        pygame.draw.rect(screen, (100,200,100), pygame.Rect((grid_width/9)*col+offset1, (grid_width/9)*row+offset2, (grid_width/9)+(col+1)-offset3, (grid_width/9)+(row+1)-offset4 ))
        draw_number(row, col, grid[row][col])
        return((row, col))
    else:
        return((-1,-1))

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


    grid_base=[[1,0,1,0,0,1,1,1,0],
                [0,1,1,1,1,0,0,0,1],
                [0,1,0,0,0,1,0,1,0],
                [0,1,1,0,0,0,0,1,1],
                [1,1,0,0,0,1,1,0,0],
                [0,0,0,1,0,1,0,0,1],
                [0,0,1,0,1,1,1,0,0],
                [0,0,1,0,0,0,0,0,0],
                [0,1,0,0,1,1,1,1,1]]
    
    # grid_solved=grid.copy
    _,grid_solved=solve(grid)
    grid_solved=[[1,3,7,9,8,6,4,5,2],
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



            




pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Sudoku♥')
font = pygame.font.SysFont('arial', 25)

grid, grid_black, grid_solved = init_grid()

print_grid(grid_solved)


run  = True
grid_width=draw_background()
selected_cell=(-1,-1)

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            selected_cell=set_cella(pygame.mouse.get_pos(),selected_cell)
            print("Cella selezionate:")
            print(selected_cell)
        if (event.type == pygame.KEYDOWN):
            for i in range(len(INPUTS)):
                if (event.key==INPUTS[i]):
                    if(selected_cell[0]!=-1 and grid[selected_cell[0]][selected_cell[1]])==0:
                        draw_number(selected_cell[0],selected_cell[1], i+1)
                        grid[selected_cell[0]][selected_cell[1]]=i+1

    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()

