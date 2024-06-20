import pygame
import sys
from settings import *

grid=([[1,0,7,0,0,6,4,5,0],
      [0,2,5,3,4,0,0,0,8],
      [0,6,0,0,0,1,0,7,0],
      [0,5,3,0,0,0,0,2,9],
      [6,1,0,0,0,9,8,0,0],
      [0,0,0,6,0,2,0,0,7],
      [0,0,1,0,9,3,2,0,0],
      [0,0,8,0,0,0,0,0,0],
      [0,4,0,0,7,8,5,9,1]])


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
            output=grid[row][col]
            if(output!=0):
                n_text=font.render(str(output), True, (0,0,0))
                screen.blit(n_text, pygame.Vector2(row*(s//9)+25, col*(s//9)+21))

def colora_cella(xy):
    font = pygame.font.Font('freesansbold.ttf', 32)
    prop=w/SCREEN_WIDTH
    x=xy[0]
    y=xy[1]
    if (x<=w and y<=w):
        x=x//(w/9)
        y=y//(w/9)
        print(str(x)+" "+str(y))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(x*(w//9), y*(w//9), (x+1)*(w//9), (y+1)*(w//9)))
        print(str(x*(w//9))+" " + str(y*(w//9)) + " " + str((x+1)*(w//9)) + " " + str((y+1)*(w//9)))

pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.SysFont('arial', 20)
print(pygame.font.get_fonts())



run  = True
w=draw_background()
while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            colora_cella(pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
