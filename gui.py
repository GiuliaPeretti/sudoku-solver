import pygame
import numpy as np
import sys
from settings import *
from SudokuGrid import *

def draw_background():
    screen.fill((200,200,200))
    w=draw_grid()
    draw_number(w)
    # draw_buttons()
    return w

def draw_grid():
    s=SCREEN_HEIGHT-20
    for i in range (0,10):
        if (i==0 or i==9):
            width=5
        elif(i%3==0):
            width=4
        else:
            width=2
        pygame.draw.line(screen, (0 ,0,0),(s/9*i+9,9),(s/9*i+9,s+11), width)
        pygame.draw.line(screen, (0,0,0),(9,s/9*i+9),(s+11,s/9*i+9), width)
    return(s)

def draw_buttons():
    text_surface = font.render('Some Text', False, (0, 0, 0), (255,255,255))
    screen.blit(text_surface, (420,20))

def draw_number(s):
    for row in range (0,9):
        for col in range(0,9):
            output=grid.get_pos(row,col)
            if(output!=0):
                n_text=font.render(str(output), True, (0,0,0))
                screen.blit(n_text, pygame.Vector2(row*(s//9)+25, col*(s//9)+21))

def set_cella(xy):
    x=xy[0]
    y=xy[1]
    # if (x<=w and y<=w):
    #     x=x//(w/9)
    #     y=y//(w/9)
    #     print(str(x)+" "+str(y))
    #     pygame.draw.rect(screen, (255,0,0), pygame.Rect(x*(w//9), y*(w//9), (x+1)*(w//9), (y+1)*(w//9)))
    #     print(str(x*(w//9))+" " + str(y*(w//9)) + " " + str((x+1)*(w//9)) + " " + str((y+1)*(w//9)))
    if (x<=grid_width and y<=grid_width):
        x= int(x//(grid_width/9))
        y = int(y//(grid_width/9))
        offses1=0
        offses2=0
        if(x==0 or x==3 or x==6):
            offses1=12
            print("offset1")
            print(offses1)

        if(y==0 or y==3 or y==6):
            offses2=12
            print("offset2")
            print(offses2)


        pygame.draw.rect(screen, (100,100,200), pygame.Rect((grid_width/9)*x+offses1, (grid_width/9)*y+offses2, (grid_width/9)+(x+1), (grid_width/9)+(y+1) ))
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
font = pygame.font.SysFont('arial', 20)

grid = SudokuGrid()


run  = True
grid_width=draw_background()
while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(set_cella(pygame.mouse.get_pos()))

    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
