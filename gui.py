import pygame
import numpy as np
import sys
from settings import *
from SudokuGrid import *

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
            output=grid.get_pos(row,col)
            if(output!=0):
                color=(0,0,0) if (grid.get_bold(row,col)==1) else (0,0,255)
                n_text=font_bold.render(str(output), True, color)
                screen.blit(n_text, pygame.Vector2(row*(grid_width//9)+24, col*(grid_width//9)+18))

def draw_number(row, col, n):
    # current_font=font_bold if (grid.get_bold(row,col)==1) else font
    color=(0,0,0) if (grid.get_bold(row,col)==1) else (0,0,255)
    if(n!=0):
        n_text=font_bold.render(str(n), True, color)
        screen.blit(n_text, pygame.Vector2(row*(grid_width//9)+25, col*(grid_width//9)+21))


def set_cella(xy, prev_xy):
    _=draw_background()
    x=xy[0]
    y=xy[1]
    x= int(x//(grid_width/9))
    y = int(y//(grid_width/9))
    # if (x<=w and y<=w):
    #     x=x//(w/9)
    #     y=y//(w/9)
    #     print(str(x)+" "+str(y))
    #     pygame.draw.rect(screen, (255,0,0), pygame.Rect(x*(w//9), y*(w//9), (x+1)*(w//9), (y+1)*(w//9)))
    #     print(str(x*(w//9))+" " + str(y*(w//9)) + " " + str((x+1)*(w//9)) + " " + str((y+1)*(w//9)))
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

        if((x+1)%3==0):
            offset3+=0
        if((y+1)%3==0):
            offset4+=0
        
        # print("offset1 "+str(offset1))
        # print("offset2 "+str(offset2))
        # print("offset3 "+str(offset3))
        # print("offset4 "+str(offset4))



        pygame.draw.rect(screen, (100,200,100), pygame.Rect((grid_width/9)*x+offset1, (grid_width/9)*y+offset2, (grid_width/9)+(x+1)-offset3, (grid_width/9)+(y+1)-offset4 ))
        draw_number(x,y, grid.get_pos(x,y))
        # print(grid_width)
        # print((grid_width/9)*x+12)
        # print((grid_width/9)*y+12)
        # print((grid_width/9)+(x+1))
        # print((grid_width/9)+(y+1))
        return( (x, y) )
    else:
        return((-1,-1))


pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.font.init()
font_bold = pygame.font.SysFont('arial', 25)
font = pygame.font.SysFont('arial', 20)

grid = SudokuGrid()


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
                print("inizio for")
                if (event.key==INPUTS[i]):
                    print("trovato: "+str(i+1))
                    print(selected_cell[0]!=-1)
                    print(grid.get_pos(selected_cell[1],selected_cell[0])==0)
                    if(selected_cell[0]!=-1 and grid.get_pos(selected_cell[0],selected_cell[1])==0):
                        draw_number(selected_cell[0],selected_cell[1], i+1)
                        grid.set_number(selected_cell[0],selected_cell[1],i+1)
                print('fine for')







    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()

#TODO: quando selezioni celle consecutivamente non scrive