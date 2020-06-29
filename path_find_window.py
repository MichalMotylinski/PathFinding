from tkinter import *
import pygame

from node import Node
from grid import Grid
import a_star

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
dark_yellow = (150, 150, 0)
yellow = (200, 200, 0)
bright_yellow = (255, 255, 0)
blue = (0, 0, 255)
dark_grey = (128, 128, 128)
grey = (169, 169, 169)
bright_grey = (192, 192, 192)
gainsboro = (220, 220, 220)
dark_magenta = (150, 0, 150)
magenta = (200, 0, 200)
bright_magenta = (250, 0, 250)

# Variables used to reset color in grid cells when not hovered by mouse
old_node_x = -1
old_node_y = -1
mouse_color = white
old_start_node = (-1, -1)
old_end_node = (-1, -1)
put_start_node = False
put_end_node = False
put_obstacle = False
start_node_created = False
end_node_created = False

visited_list = []
old_visited_list = []
path_list = []
path_dist = 0
total_time = 0
start_end_dist = 0
solved = False
a_star_alg = False

# Classes
grid = Grid()

# Show application window and save to variable for further use
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)
screen.fill(gainsboro)

# Get clock for counting fps and set application speed
clock = pygame.time.Clock()

# Set name of the application
pygame.display.set_caption('Path finding')

# Create grid of nodes
nodes_list = grid.create_grid()
node_width = grid.width / grid.columns
node_height = grid.height / grid.rows


# Create surface with text rendered on it
def text_object(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# Create legend/manual
def legend(pos_x, pos_y, width, height, background_color):
    pygame.draw.rect(screen, background_color, (pos_x, pos_y, width, height))
    text_font = pygame.font.Font("freesansbold.ttf", 14)

    separator = "--------------------------------------------------------------------"
    head = "Legend:"
    text_surface, text_rect = text_object(head, text_font, white)
    text_rect.center = (int(pos_x + (width / 2)), int(pos_y + (height / 2)))
    screen.blit(text_surface, text_rect)
    pos_y = pos_y + 30
    texts = ("Choose action by pressing one of the buttons", "Left mouse button to create objects in the grid",
             "Right mouse button to remove objects from grid", separator, "Algorithm time: " + str(total_time) + " s",
             "Start-End distance: " + str(start_end_dist), "Path distance: " + str(path_dist))

    for line in texts:
        pygame.draw.rect(screen, background_color, (pos_x, pos_y, width, height))
        text_surface, text_rect = text_object(line, text_font, white)
        text_rect = (int(pos_x + 5), int(pos_y + (height / 4)))
        pos_y = pos_y + 30
        screen.blit(text_surface, text_rect)


# Create button functionality
def button(text, pos_x, pos_y, width, height, normal_color, hovered_color, clicked_color, mouse_event):
    global mouse_color, put_start_node, put_end_node, put_obstacle, visited_list, old_visited_list, path_dist,\
        total_time, a_star_alg
    mouse_pos = pygame.mouse.get_pos()

    if pos_x + width > mouse_pos[0] > pos_x and pos_y + height > mouse_pos[1] > pos_y:
        pygame.draw.rect(screen, hovered_color, (pos_x, pos_y, width, height))
        if mouse_event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, clicked_color, (pos_x, pos_y, width, height))

            # Choose action depending on the button that user clicked on
            if text == "Start position":
                put_start_node = True
                put_end_node = False
                put_obstacle = False
                mouse_color = normal_color
            elif text == "End position":
                put_end_node = True
                put_start_node = False
                put_obstacle = False
                mouse_color = normal_color
            elif text == "Obstacle":
                put_obstacle = True
                put_start_node = False
                put_end_node = False
                mouse_color = normal_color
            elif text == "Reset grid":
                put_start_node = False
                put_end_node = False
                put_obstacle = False
                mouse_color = white
                reset_grid()
            elif text == "Solve A*" and grid.start_node != (-1, -1) and grid.end_node != (-1, -1):
                a_star_alg = True
    else:
        pygame.draw.rect(screen, normal_color, (pos_x, pos_y, width, height))

    text_font = pygame.font.Font("freesansbold.ttf", 20)
    text_surface, text_rect = text_object(text, text_font, black)
    text_rect.center = (int(pos_x + (width / 2)), int(pos_y + (height / 2)))
    screen.blit(text_surface, text_rect)


# Draw a node
def draw_node(pos_x, pos_y, color):
    nodes_list[pos_x][pos_y].draw_node(screen, color, 0, node_width, node_height)
    nodes_list[pos_x][pos_y].draw_node(screen, black, 1, node_width, node_height)


# Clear all cells of the grid and set default values for variables/parameters used
def reset_grid():
    global start_node_created, end_node_created, visited_list, a_star_alg, path_dist, total_time, start_end_dist
    start_node_created = False
    end_node_created = False
    a_star_alg = False
    grid.start_node = (-1, -1)
    grid.end_node = (-1, -1)
    path_dist = 0
    start_end_dist = 0
    total_time = 0
    path_list.clear()
    for x in range(grid.columns):
        for y in range(grid.rows):
            nodes_list[x][y].g_cost = float('inf')
            nodes_list[x][y].h_cost = float('inf')
            nodes_list[x][y].visited = False
            nodes_list[x][y].parent = None
            nodes_list[x][y].obstacle = False
            draw_node(x, y, white)


# Draw representation of the created grid on the screen
for i in range(grid.columns):
    for j in range(grid.rows):
        draw_node(i, j, white)

app_running = True

# Frame by frame actions
while app_running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        app_running = False
        continue
    mouse = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    # Get coordinates of a node hovered by mouse
    node_x = int(mouse[0] / node_width)
    node_y = int(mouse[1] / node_height)

    # Render UI
    legend(825, 25, 350, 30, black)
    button("Start position", 825, 280, 150, 50, dark_green, green, bright_green, event)
    button("End position", 1025, 280, 150, 50, dark_red, red, bright_red, event)
    button("Obstacle", 825, 340, 150, 50, dark_grey, grey, bright_grey, event)
    button("Reset grid", 1025, 340, 150, 50, dark_magenta, magenta, bright_magenta, event)
    button("Solve A*", 925, 400, 150, 50, dark_yellow, yellow, bright_yellow, event)

    # Rendering path and visited nodes between start and end node
    if start_node_created and end_node_created:
        for node in visited_list:
            if (node.position_x, node.position_y) != grid.start_node and (node.position_x,
                                                                          node.position_y) != grid.end_node:
                if node.visited:
                    draw_node(node.position_x, node.position_y, yellow)
                if node.obstacle:
                    draw_node(node.position_x, node.position_y, dark_grey)

        for node in old_visited_list:
            if node not in visited_list and not node.obstacle:
                draw_node(node.position_x, node.position_y, white)

        if not solved:
            if a_star_alg:
                visited_list, old_visited_list, start_end_dist, total_time = a_star.solve_a_star(nodes_list,
                                                                                                 grid.start_node,
                                                                                                 grid.end_node,
                                                                                                 visited_list)
                solved = True
        if solved:
            start_node = nodes_list[grid.start_node[0]][grid.start_node[1]]
            end_node = nodes_list[grid.end_node[0]][grid.end_node[1]]
            path = end_node
            path_dist = 0
            path_list.clear()
            while path.parent is not None:
                if path.parent.position_x == start_node.position_x and path.parent.position_y == start_node.position_y:
                    if path_dist == 0:
                        path_dist = path.parent.f_cost
                    break
                path_list.append(path.parent)
                if path.parent.f_cost > path_dist:
                    path_dist = path.parent.f_cost
                path = path.parent

    # Draw path
    for node in path_list:
        if not node.obstacle:
            draw_node(node.position_x, node.position_y, blue)

    # Rendering cells colors when hoovering over with mouse
    if grid.width > mouse[0] >= 0 and grid.height > mouse[1] >= 0:

        if old_node_x != -1 and old_node_y != -1 and not nodes_list[old_node_x][old_node_y].visited \
                and not nodes_list[old_node_x][old_node_y].obstacle:
            draw_node(old_node_x, old_node_y, white)
        elif old_node_x != -1 and old_node_y != -1 and nodes_list[old_node_x][old_node_y].visited:
            draw_node(old_node_x, old_node_y, yellow)
            if nodes_list[old_node_x][old_node_y].obstacle:
                draw_node(old_node_x, old_node_y, dark_grey)
            elif nodes_list[old_node_x][old_node_y] in path_list and not nodes_list[old_node_x][old_node_y].obstacle:
                draw_node(old_node_x, old_node_y, blue)

        if (node_width * node_x) + node_width >= mouse[0] >= node_width * node_x \
                and (node_height * node_y) + node_height >= mouse[1] >= node_height * node_y \
                and not nodes_list[node_x][node_y].obstacle:
            draw_node(node_x, node_y, mouse_color)

            if mouse_clicked[0] == 1 and put_start_node and (node_x, node_y) != grid.end_node \
                    and not nodes_list[node_x][node_y].obstacle:
                grid.start_node = (node_x, node_y)
                start_node_created = True
                if nodes_list[node_x][node_y].obstacle:
                    nodes_list[node_x][node_y].obstacle = False
                solved = False
            elif mouse_clicked[0] == 1 and put_end_node and (node_x, node_y) != grid.start_node \
                    and not nodes_list[node_x][node_y].obstacle:
                grid.end_node = (node_x, node_y)
                end_node_created = True
                if nodes_list[node_x][node_y].obstacle:
                    nodes_list[node_x][node_y].obstacle = False
                solved = False
            elif mouse_clicked[0] == 1 and put_obstacle and (node_x, node_y) != grid.start_node \
                    and (node_x, node_y) != grid.end_node:
                nodes_list[node_x][node_y].obstacle = True
                solved = False

            old_node_x = node_x
            old_node_y = node_y

    else:
        if old_node_x != -1 and old_node_y != -1 and not nodes_list[old_node_x][old_node_y].visited \
                and not nodes_list[old_node_x][old_node_y].obstacle:
            draw_node(old_node_x, old_node_y, white)
        elif old_node_x != -1 and old_node_y != -1 and nodes_list[old_node_x][old_node_y].visited:
            draw_node(old_node_x, old_node_y, yellow)
            if nodes_list[old_node_x][old_node_y].obstacle:
                draw_node(old_node_x, old_node_y, dark_grey)
            elif nodes_list[old_node_x][old_node_y] in path_list and not nodes_list[old_node_x][old_node_y].obstacle:
                draw_node(old_node_x, old_node_y, blue)

    # Remove obstacle action
    if mouse_clicked[2] == 1:
        if (node_width * node_x) + node_width > mouse[0] > node_width * node_x \
                and (node_height * node_y) + node_height > mouse[1] > node_height * node_y:
            if nodes_list[node_x][node_y].obstacle:
                nodes_list[node_x][node_y].obstacle = False
                draw_node(node_x, node_y, white)
                solved = False

    # Drawing start node
    if not ((node_width * grid.start_node[0]) + node_width > mouse[0] > node_width * grid.start_node[0]
            and (node_height * grid.start_node[1]) + node_height > mouse[1] > node_height * grid.start_node[1]) \
            and grid.start_node != (-1, -1) and start_node_created:
        if nodes_list[old_start_node[0]][old_start_node[1]].obstacle:
            draw_node(old_start_node[0], old_start_node[1], dark_grey)
        else:
            draw_node(old_start_node[0], old_start_node[1], white)
        draw_node(grid.start_node[0], grid.start_node[1], dark_green)
        old_start_node = grid.start_node

    # Drawing end node
    if grid.end_node != (-1, -1) and end_node_created \
            and not ((node_width * grid.end_node[0]) + node_width > mouse[0] > node_width * grid.end_node[0]
                     and (node_height * grid.end_node[1]) + node_height > mouse[1] > node_height * grid.end_node[1]):
        draw_node(old_end_node[0], old_end_node[1], white)
        draw_node(grid.end_node[0], grid.end_node[1], dark_red)
        old_end_node = grid.end_node

    pygame.display.update()
    clock.tick(60)
pygame.quit()
