import pygame

from node import Node


class Grid:
    def __init__(self):
        self.columns = 50
        self.rows = 50
        self.width = 800
        self.height = 800
        self.start_node = Node
        self.end_node = Node
        self.closed = False
        self.nodes_list = []

    def create_grid(self):
        # Create grid of nodes
        grid = [[Node(False, column, row) for row in range(self.rows)] for column in range(self.columns)]

        # Find neighbours for each node
        """for i in range(self.columns):
            for j in range(self.rows):

                # Find adjacent nodes
                if j > 0:
                    grid[i][j].neighbours.append(grid[i][j + 1])"""

        #print(grid[0][1].neighbours)

        return grid


