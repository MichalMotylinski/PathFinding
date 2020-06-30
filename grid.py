from node import Node


class Grid:
    def __init__(self):
        self.columns = 40
        self.rows = 40
        self.width = 800
        self.height = 800
        self.start_node = (-1, -1)
        self.end_node = (-1, -1)
        self.nodes_list = []

    def create_grid(self):
        # Create grid of nodes
        self.nodes_list = [[Node(False, column, row) for row in range(self.rows)] for column in range(self.columns)]

        # Find neighbours for each node
        for i in range(self.columns):
            for j in range(self.rows):
                # Find northern neighbour
                if j > 0:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i][j - 1])
                # Find  north eastern neighbour
                if 0 < j and i < self.columns - 1:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i + 1][j - 1])
                # Find eastern neighbour
                if i < self.columns - 1:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i + 1][j])
                # Find south eastern neighbour
                if j < self.rows - 1 and i < self.columns - 1:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i + 1][j + 1])
                # Find southern neighbour
                if j < self.rows - 1:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i][j + 1])
                # Find south western neighbour
                if j < self.rows - 1 and i > 0:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i - 1][j + 1])
                # Find western neighbour
                if i > 0:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i - 1][j])
                # Find north western neighbour
                if j > 0 and i > 0:
                    self.nodes_list[i][j].neighbours.append(self.nodes_list[i - 1][j - 1])
        return self.nodes_list
