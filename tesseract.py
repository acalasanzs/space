import pygame
from win32api import GetSystemMetrics
import os
import math
def matrix_m(a,b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len (b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_a:
        for x in range(rows_a):
            for y in range(columns_b):
                sum= 0
                for j in range(columns_a):
                    sum += range(columns_a)
                result_matrix[x][y] = sum

        return result_matrix
    else:
        print("Err")
        return None

os.environ["SDL_VIDEO_CENTERED"]= '1'

black, white = (20,20,20),(230,230,230)

x , y = [int(GetSystemMetrics(i)/2) for i in range(2)]

pygame.init()
pygame.display.set_caption("Tesseract")
screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
FPS = 60

angle = 0
cube_position = [x//2,y//2]
scale = 2500
speed = 0.01
points = [n for n in range(16)]

points[0] = [[-1],[-1],[1],[1]]
points[1] = [[1],[-1],[1],[1]]
points[2] = [[1],[1],[1],[1]]
points[3] = [[-1],[1],[1],[1]]
points[4] = [[-1],[-1],[-1],[1]]
points[5] = [[1],[-1],[-1],[1]]
points[6] = [[1],[1],[-1],[1]]
points[7] = [[-1],[-1],[1],[1]]
points[8] = [[-1],[-1],[1],[-1]]
points[9] = [[1],[-1],[1],[-1]]
points[10] = [[1],[1],[1],[-1]]
points[11] = [[-1],[1],[1],[-1]]
points[12] = [[-1],[-1],[-1],[-1]]
points[13] = [[1],[-1],[-1],[-1]]
points[14] = [[1],[1],[-1],[-1]]
points[15] = [[-1],[1],[-1],[-1]]

def connect_point(i,j,k,offset):
    a = k[i+offset]
    b = k[j+ offset]
    pygame.draw.line(screen,black,(a[0],a[1]),(b[0],b[1]),2)
run = True
while run:
    clock.tick(FPS)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    index = 0
    projected_point = [j]