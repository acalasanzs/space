"""
Python version: 3.8.10

"""


import pygame as pg
from pygame.locals import *
from win32api import GetSystemMetrics
import os
import math
from OpenGL.GL import *
#import cairo
from OpenGL.GLU import *
def wireCube():
        cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1, 1,-1))
        cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
        glBegin(GL_LINES)
        for cubeEdge in cubeEdges:
            for cubeVertex in cubeEdge:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()
# Variables

x , y = [int(GetSystemMetrics(i)/1.5) for i in range(2)]
clock = pg.time.Clock()
FPS = 60
bg = (53, 59, 72)
white = (220, 221, 225)
windowSize = (x,y)

def main():
    pg.init()
    icon = pg.image.load("icon.png")
    pg.display.set_icon(icon)
    pg.display.set_caption("Derpo draft")
    screen = pg.display.set_mode(windowSize, DOUBLEBUF|OPENGL)

    run = True

    gluPerspective(45,(x/y), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)
    glRotatef(0,0,0,0)
    glViewport(0, 0, x, y)

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        glRotatef(1,3,1,0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        wireCube()
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()