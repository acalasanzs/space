"""
Python version: 3.8.10

"""


import pygame as pg
from pygame.locals import *
from win32api import GetSystemMetrics
import os
import math
from OpenGL.GL import *
from OpenGL.GLU import *
pg.init()
# Variables

x , y = [int(GetSystemMetrics(i)/2) for i in range(2)]


windowSize = (x,y)
pg.display.set_mode(windowSize, DOUBLEBUF|OPENGL)