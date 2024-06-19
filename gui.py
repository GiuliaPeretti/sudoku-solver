import pygame
import sys
from settings import *

def draw_background():
    screen.fill((255,255,255))
    draw_lines()


def draw_lines():
    w=SCREEN_WIDTH-5
    h=SCREEN_HEIGHT-5
    for i in range (0,10):
        if (i%3==0 or i==0 or i==9):
            width=5
        else:
            width=2
        pygame.draw.line(screen, (0,0,0),(w/9*i+2,0),(w/9*i+2,h), width)
        pygame.draw.line(screen, (0,0,0),(0,h/9*i+2),(w,h/9*i+2), width)


pygame.init()

clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)




run  = True
while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
    draw_background()
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
