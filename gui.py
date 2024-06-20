import pygame
import numpy as np
import sys
from settings import *
from sudoku_solver import *

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

def draw_buttons():
    text_surface = font.render('Some Text', False, (0, 0, 0), (255,255,255))
    screen.blit(text_surface, (420,20))

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
                n_text=font_bold.render(str(output), True, color)
                screen.blit(n_text, pygame.Vector2(row*(grid_width//9)+24, col*(grid_width//9)+18))

def draw_number(row, col, n):
    if (grid_black[row][col]==1):
        color=(0,0,0)
    elif (grid_solved[row][col]!=n):
        print(grid_solved[row][col])
        print(n)
        color=(255,0,0)
    else:
        color=(0,0,255)
    if(n!=0):
        n_text=font_bold.render(str(n), True, color)
        screen.blit(n_text, pygame.Vector2(row*(grid_width//9)+25, col*(grid_width//9)+21))

def set_cella(xy, prev_xy):
    _=draw_background()
    x=xy[0]
    y=xy[1]
    x= int(x//(grid_width/9))
    y = int(y//(grid_width/9))

    if(prev_xy[0]==x and prev_xy[1]==y):
        _=draw_background()
        return((-1,-1))
    
    if (x<=grid_width and y<=grid_width):
        offset1=10
        offset2=10
        offset3=x+5-(x%3)
        offset4=y+5-(y%3)
        if(x%3==0):
            offset1+=1
            offset3-=2
        if(y%3==0):
            offset2+=1
            offset4-=2
        if((x-1)%3==0):
            offset3-=3
        if((y-1)%3==0):
            offset4-=3
        pygame.draw.rect(screen, (100,200,100), pygame.Rect((grid_width/9)*x+offset1, (grid_width/9)*y+offset2, (grid_width/9)+(x+1)-offset3, (grid_width/9)+(y+1)-offset4 ))
        draw_number(x,y, grid[x][y])
        return((x, y))
    else:
        return((-1,-1))

def init_grid():
        # self.grid=np.zeros([9,9], dtype=int)
    grid=([[1,0,7,0,0,6,4,5,0],
                [0,2,5,3,4,0,0,0,8],
                [0,6,0,0,0,1,0,7,0],
                [0,5,3,0,0,0,0,2,9],
                [6,1,0,0,0,9,8,0,0],
                [0,0,0,6,0,2,0,0,7],
                [0,0,1,0,9,3,2,0,0],
                [0,0,8,0,0,0,0,0,0],
                [0,4,0,0,7,8,5,9,1]])
    grid_base=([[1,0,1,0,0,1,1,1,0],
                [0,1,1,1,1,0,0,0,1],
                [0,1,0,0,0,1,0,1,0],
                [0,1,1,0,0,0,0,1,1],
                [1,1,0,0,0,1,1,0,0],
                [0,0,0,1,0,1,0,0,1],
                [0,0,1,0,1,1,1,0,0],
                [0,0,1,0,0,0,0,0,0],
                [0,1,0,0,1,1,1,1,1]])
    
    # grid_solved=grid.copy
    # solve(grid_solved)
    grid_solved=([[1,3,7,9,8,6,4,5,2],
                    [9,2,5,3,4,7,1,6,8],
                    [8,6,4,5,2,1,9,7,3],
                    [7,5,3,8,1,4,6,2,9],
                    [6,1,2,7,3,9,8,4,5],
                    [4,8,9,6,5,2,3,1,7],
                    [5,7,1,4,9,3,2,8,6],
                    [2,9,8,1,6,5,7,3,4],
                    [3,4,6,2,7,8,5,9,1]       
                    ])

    return(grid, grid_base, grid_solved)



pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.font.init()
font_bold = pygame.font.SysFont('arial', 25)
font = pygame.font.SysFont('arial', 20)

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
        if (event.type == pygame.KEYDOWN):
            for i in range(len(INPUTS)):
                if (event.key==INPUTS[i]):
                    if(selected_cell[0]!=-1 and grid[selected_cell[0]][selected_cell[1]])==0:
                        draw_number(selected_cell[0],selected_cell[1], i+1)
                        grid[selected_cell[0]][selected_cell[1]]=i+1







    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()

