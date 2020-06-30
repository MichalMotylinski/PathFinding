# Represents a single node from grid
import pygame


class Node:
    def __init__(self, obstacle, position_x, position_y):
        self.obstacle = obstacle
        self.visited = False
        self.neighbours = []
        self.parent = None
        # distance from starting node
        self.g_cost = float('inf')
        # distance from end node (heuristic)
        self.h_cost = float('inf')
        # total distance (g + h)
        self.f_cost = 0
        self.parent_dist = 0
        self.position_x = position_x
        self.position_y = position_y

    def draw_node(self, screen, color, thickness, width, height):
        pygame.draw.rect(screen, color, (self.position_x * width, self.position_y * height, width, height), thickness)
