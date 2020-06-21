from tkinter import *
import pygame

from node import Node
pygame.init()

screen = pygame.display.set_mode((1000, 800))

columns = 50
rows = 50
grid = [[Node] * rows for i in range(columns)]

app_running = True

while app_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        app_running = False
        continue
    pygame.display.update()

pygame.quit()
