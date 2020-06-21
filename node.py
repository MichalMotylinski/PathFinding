# Represents a single node from grid
class Node:
    def __init__(self, x, y):
        self.obstacle = False
        self.neighbours = []
        self.global_cost = 0
        self.local_cost = 0

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

    @neighbours.deleter
    def neighbours(self):
        del(self._neighbours)



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
