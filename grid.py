import pygame

from node import Node


class Grid:
    def __init__(self):
        self.columns = 50
        self.rows = 50
        self.width = 800
        self.height = 800
        self.start_node = (-1, -1)
        self.end_node = (-1, -1)
        self.closed = False
        self.nodes_list = []

    def create_grid(self):
        # Create grid of nodes
        grid = [[Node(False, column, row) for row in range(self.rows)] for column in range(self.columns)]

        # Find neighbours for each node
        for i in range(self.columns):
            for j in range(self.rows):
                #print("Node " + str(grid[i][j].position_x) + " " + str(grid[i][j].position_y))
                # Find northern neighbour
                if j > 0:
                    grid[i][j].neighbours.append(grid[i][j - 1])
                    #print("N " + str(grid[i][j - 1].position_x) + " " + str(grid[i][j - 1].position_y))
                # Find  north eastern neighbour
                if 0 < j and i < self.columns - 1:
                    grid[i][j].neighbours.append(grid[i + 1][j - 1])
                    #print("NE " + str(grid[i + 1][j - 1].position_x) + " " + str(grid[i + 1][j - 1].position_y))
                # Find eastern neighbour
                if i < self.columns - 1:
                    grid[i][j].neighbours.append(grid[i + 1][j])
                    #print("E " + str(grid[i + 1][j].position_x) + " " + str(grid[i + 1][j].position_y))
                # Find south eastern neighbour
                if j < self.rows - 1 and i < self.columns - 1:
                    grid[i][j].neighbours.append(grid[i + 1][j + 1])
                    #print("SE " + str(grid[i + 1][j + 1].position_x) + " " + str(grid[i + 1][j + 1].position_y))
                # Find southern neighbour
                if j < self.rows - 1:
                    grid[i][j].neighbours.append(grid[i][j + 1])
                    #print("S " + str(grid[i][j + 1].position_x) + " " + str(grid[i][j + 1].position_y))
                # Find south western neighbour
                if j < self.rows - 1 and i > 0:
                    grid[i][j].neighbours.append(grid[i - 1][j + 1])
                    #print("SW " + str(grid[i - 1][j + 1].position_x) + " " + str(grid[i - 1][j + 1].position_y))
                # Find western neighbour
                if i > 0:
                    grid[i][j].neighbours.append(grid[i - 1][j])
                    #print("W " + str(grid[i - 1][j].position_x) + " " + str(grid[i - 1][j].position_y))
                # Find north western neighbour
                if j > 0 and i > 0:
                    grid[i][j].neighbours.append(grid[i - 1][j - 1])
                    #print("NW " + str(grid[i - 1][j - 1].position_x) + " " + str(grid[i - 1][j - 1].position_y))

        # Testing lines
        #print(str(grid[i][j].position_x) + " " + str(grid[i][j].position_y))
        #print(str(grid[i][j+ 1].position_x) + " " + str(grid[i][j+ 1].position_y))
        return grid


