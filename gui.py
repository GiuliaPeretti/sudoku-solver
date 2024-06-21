import pygame
from settings import *
from random import sample
import random 
import copy

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

def draw_button():
    x1,y1,w,h=SCREEN_WIDTH-50-110, 9, 95, 30
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    font = pygame.font.SysFont('arial', 17)
    text=font.render(str("Easy"), True, (0,0,0))
    screen.blit(text, (x1+27, y1+5))

    b_easy=((x1,x1+w),(y1,y1+h))

    y1=y1+h+10
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Medium"), True, (0,0,0))
    screen.blit(text, (x1+20, y1+5))

    b_medium=((x1,x1+w),(y1,y1+h))

    y1=y1+h+10
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Difficult"), True, (0,0,0))
    screen.blit(text, (x1+20, y1+5))

    b_difficult=((x1,x1+w),(y1,y1+h))

    y1=y1+h+10
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Generate new"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_generate=((x1,x1+w),(y1,y1+h))

    return(b_easy,b_medium,b_difficult,b_generate)

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
    grid_solved=generate_grid()
    grid=playble_grid(grid_solved,10)
    grid_bold=generate_bold(grid)
    return(grid, grid_bold, grid_solved)

def generate_bold(grid):
    grid_bold=copy.deepcopy(grid)
    for r in range (9):
        for c in range (9):
            if (grid_bold[r][c]!=0):
                grid_bold[r][c]=1
            else:
                grid_bold[r][c]=0
    return(grid_bold)

def playble_grid(grid_solved, n):
    grid=copy.deepcopy(grid_solved)
    c=0
    while c<n:
        row=random.randint(0,8)
        col=random.randint(0,8)
        if (grid[row][col]!=0):
            grid[row][col]=0
            c+=1
    return grid

def generate_grid():
    base  = 3
    side  = base*base
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return(board)

def pattern(r,c): 
    base  = 3
    side  = base*base
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 

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

            




pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Sudoku♥')
font = pygame.font.SysFont('arial', 25)

grid, grid_black, grid_solved = init_grid()
print("grid")
print_grid(grid)
print("grid_black")
print_grid(grid_black)
print("grid_solved")
print_grid(grid_solved)

print_grid(grid_solved)


run  = True
grid_width=draw_background()
selected_cell=(-1,-1)
b_easy,b_medium,b_difficult,b_generate=draw_button()
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

