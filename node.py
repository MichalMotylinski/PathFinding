
# Represents a single node from grid
import pygame


class Node:
    def __init__(self, obstacle, position_x, position_y):
        self.obstacle = obstacle
        self.visited = False
        self.neighbours = []
        self.parent = self
        # distance from starting node
        self.g_cost = 0
        # distance from end node (heuristic)
        self.h_cost = 0
        # total distance (g + h)
        self.f_cost = 0
        self.position_x = position_x
        self.position_y = position_y
        self.start_node = 0

    @property
    def obstacle(self):
        return self._obstacle

    @obstacle.setter
    def obstacle(self, value):
        self._obstacle = value

    @property
    def neighbours(self):
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value):
        self._neighbours = value

    @property
    def g_cost(self):
        return self._g_cost

    @g_cost.setter
    def g_cost(self, value):
        self._g_cost = value

    @property
    def h_cost(self):
        return self._h_cost

    @h_cost.setter
    def h_cost(self, value):
        self._h_cost = value

    def __nonzero__(self):
        return bool(self.position_x or self.position_y)

    def draw_node(self, screen, color, thickness, width, height):
        pygame.draw.rect(screen, color, (self.position_x * width, self.position_y * height, width, height),
                         thickness)





        """self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1"""


"""
bool m_bObstacle;
bool m_bVisited;
float m_gCost; // Distance from starting point
float m_hCost; // Distance from endNode
Node* m_parentNode; // Pointer to parent node (previous node)
std::vector<Node*> m_vecNeighbours; // vector storing pointers to all neighbours
sf::Vector2f m_position;
sf::RectangleShape m_rectShape;"""
