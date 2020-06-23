from tkinter import *
import pygame

from node import Node
from grid import Grid

pygame.init()

# Set up some initial values

# Size of the application window
screen_width = 1200
screen_height = 800

# Colors used in the application
white = (255, 255, 255)
black = (0, 0, 0)
dark_red = (150, 0, 0)
red = (200, 0, 0)
bright_red = (255, 0, 0)
dark_green = (0, 150, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)

# Variables used to reset color in grid cells when not hovered by mouse
old_node_x = -1
old_node_y = -1
mouse_color = white
old_start_node = (-1, -1)
old_end_node = (-1, -1)
put_start_node = False
put_end_node = False

# Classes
grid_class = Grid()

# Show application window and save to variable for further use
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)
screen.fill(grey)

# Get clock for counting fps and set application speed
clock = pygame.time.Clock()

# Set name of the application
pygame.display.set_caption('Path finding test')

# Create grid of nodes
grid = grid_class.create_grid()
node_width = grid_class.width / grid_class.columns
node_height = grid_class.height / grid_class.rows


def text_object(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(text, pos_x, pos_y, width, height, normal_color, hovered_color, clicked_color):
    global mouse_color, put_start_node, put_end_node
    mouse_pos = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    if pos_x + width > mouse_pos[0] > pos_x and pos_y + height > mouse_pos[1] > pos_y:
        pygame.draw.rect(screen, hovered_color, (pos_x, pos_y, width, height))
        if clicked[0] == 1:
            pygame.draw.rect(screen, clicked_color, (pos_x, pos_y, width, height))
            mouse_color = normal_color
            if text == "Start position":
                put_start_node = True
                put_end_node = False
            elif text == "End position":
                put_end_node = True
                put_start_node = False
    else:
        pygame.draw.rect(screen, normal_color, (pos_x, pos_y, width, height))

    text_font = pygame.font.Font("freesansbold.ttf", 20)
    text_surface, text_rect = text_object(text, text_font)
    text_rect.center = (int(pos_x + (width / 2)), int(pos_y + (height / 2)))
    screen.blit(text_surface, text_rect)


# Draw a node
def draw_node(pos_x, pos_y, color):
    grid[pos_x][pos_y].draw_node(screen, color, 0, node_width, node_height)
    grid[pos_x][pos_y].draw_node(screen, black, 1, node_width, node_height)


# Draw representation of the created grid on the screen
for i in range(grid_class.columns):
    for j in range(grid_class.rows):
        draw_node(i, j, white)

app_running = True

# Frame by frame actions
while app_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        app_running = False
        continue
    mouse = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    button("Start position", 825, 50, 150, 50, dark_green, green, bright_green)
    button("End position", 1025, 50, 150, 50, dark_red, red, bright_red)

    if grid_class.width > mouse[0] > 0 and grid_class.height > mouse[1] > 0:
        node_x = int(mouse[0] / node_width)
        node_y = int(mouse[1] / node_height)

        if old_node_x != -1 and old_node_y != -1:
            draw_node(old_node_x, old_node_y, white)

        if (node_width * node_x) + node_width > mouse[0] > node_width * node_x \
                and (node_height * node_y) + node_height > mouse[1] > node_height * node_y:
            draw_node(node_x, node_y, mouse_color)

            if mouse_clicked[0] == 1 and put_start_node:
                grid_class.start_node = (node_x, node_y)
            elif mouse_clicked[0] == 1 and put_end_node:
                grid_class.end_node = (node_x, node_y)

            old_node_x = node_x
            old_node_y = node_y

    else:
        if old_node_x != -1 and old_node_y != -1:
            draw_node(old_node_x, old_node_y, white)

    if grid_class.start_node[0] != -1 and put_start_node:
        draw_node(old_start_node[0], old_start_node[1], white)
        draw_node(grid_class.start_node[0], grid_class.start_node[1], mouse_color)
        old_start_node = grid_class.start_node

    if grid_class.end_node[0] != -1 and put_end_node:
        draw_node(old_end_node[0], old_end_node[1], white)
        draw_node(grid_class.end_node[0], grid_class.end_node[1], mouse_color)
        old_end_node = grid_class.end_node

    """if clicked[0] == 1:
        print("aaa")
        if grid_class.width > mouse[0] > 0 and grid_class.height > mouse[1] > 0:
            node_x = int(mouse[0] / node_width)
            node_y = int(mouse[1] / node_height)

            if (node_width * node_x) + node_width > mouse[0] > node_width * node_x \
                    and (node_height * node_y) + node_height > mouse[1] > node_height * node_y:
                draw_node(node_x, node_y, mouse_color)"""

    pygame.display.update()
    clock.tick(60)
pygame.quit()
