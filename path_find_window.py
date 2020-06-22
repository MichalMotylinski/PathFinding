from tkinter import *
import pygame

from node import Node
from grid import Grid

pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)

clock = pygame.time.Clock()

pygame.display.set_caption('Path finding test')

grid_class = Grid()
grid = grid_class.create_grid()
for i in range(grid_class.columns):
    for j in range(grid_class.rows):
        grid[i][j].draw_node(screen, (255, 255, 255), 1, grid_class.width / grid_class.columns,
                             grid_class.height / grid_class.rows)

"""for i in range(grid.columns):
    for j in range(grid.rows):
        def draw_node(self, screen, color, thickness, width, height):
            pygame.draw.rect(screen, color, (self.position_x * width, self.position_y * height, width, height),
                             thickness)"""

"""draw_grid(grid, screen, (255, 255, 255), x, y)"""

app_running = True

while app_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        app_running = False
        continue

    pygame.display.update()

    clock.tick(60)
    #print(clock.get_fps())

pygame.quit()
