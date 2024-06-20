import pygame
import sys
from settings import *

def draw_background():
    screen.fill((255,255,255))
    w=draw_grid()
    return w


def draw_grid():
    w=SCREEN_WIDTH/2
    h=SCREEN_HEIGHT/2
    for i in range (0,10):
        if (i%3==0 or i==0 or i==9):
            width=5
        else:
            width=2
        pygame.draw.line(screen, (0,0,0),(w/9*i+2,0),(w/9*i+2,h+4), width)
        pygame.draw.line(screen, (0,0,0),(0,h/9*i+2),(w+4,h/9*i+2), width)
    return(w)

def colora_cella(xy):
    font = pygame.font.Font('freesansbold.ttf', 32)
    x=xy[0]
    y=xy[1]
    if (x<=w and y<=w):
        x=x//(w/9)
        y=y//(w/9)
        print(str(x)+" "+str(y))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(x*(w/9), y*(w/9), (x+1)*(w/9), (y+1)*(w/9)))
        print(str(x*(w/9))+" " + str(y*(w/9)) + " " + str((x+1)*(w/9)) + " " + str((y+1)*(w/9)))

pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)




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
