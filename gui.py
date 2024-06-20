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
    x=xy[0]
    y=xy[1]
    if (x<=w and y<=w):
        print(x+" "+y)
        x=x//(w/9)
        y=y//(w/9)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(x, y, x+(w/9), y+(w/9)))

pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)




run  = True
while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            colora_cella(pygame.mouse.get_pos())
    w=draw_background()
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
