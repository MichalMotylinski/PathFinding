import math
from queue import PriorityQueue


def calculate_node_distance(node_a, node_b):
    return math.sqrt((node_b.position_x - node_a.position_x)**2 + (node_b.position_y - node_a.position_y)**2)


def solve_a_star(grid, start_node_coords, end_node_coords):

    for i in range(50):
        for j in range(50):
            if not grid[i][j].obstacle:
                grid[i][j].g_cost = float('inf')
                grid[i][j].h_cost = float('inf')
                grid[i][j].visited = False
                grid[i][j].parent = None

    open_list = PriorityQueue()
    closed_list = []

    start_node = grid[start_node_coords[0]][start_node_coords[1]]
    end_node = grid[end_node_coords[0]][end_node_coords[1]]

    current_node = grid[start_node_coords[0]][start_node_coords[1]]
    current_node.g_cost = float(0)
    current_node.h_cost = calculate_node_distance(start_node, end_node)

    h_cost = current_node.h_cost
    open_list.put((h_cost, (current_node.position_x, current_node.position_y)))

    while not open_list.empty():

        # Get node from the list
        element = open_list.get()
        current_node = grid[element[1][0]][element[1][1]]

        if current_node == end_node:
            break
        # Find node with smallest cost
        """current_index = 0
        for index, node in enumerate(open_list):
            if node.f_cost < current_node.f_cost:
                current_node = node
                current_index = index"""

        # Move current node to a closed list
        closed_list.append(current_node)
        current_node.visited = True
        parent_node = current_node

        for neighbour in parent_node.neighbours:
            if neighbour.visited is True or neighbour.obstacle is True:
                continue
            lower_goal = parent_node.g_cost + calculate_node_distance(parent_node, neighbour)
            if lower_goal < neighbour.g_cost:
                neighbour.g_cost = lower_goal
                neighbour.h_cost = neighbour.g_cost + calculate_node_distance(neighbour, end_node)
                neighbour.f_cost = neighbour.g_cost + neighbour.h_cost
                neighbour.parent = parent_node

                h_cost = neighbour.h_cost
                open_list.put((h_cost, (neighbour.position_x, neighbour.position_y)))
                neighbour.visited = True
                current_node = neighbour


    total_cost = calculate_node_distance(start_node, end_node)

    """print("Start: " + str(start_node.position_x) + ", " + str(start_node.position_y))
    print("End: " + str(end_node.position_x) + ", " + str(end_node.position_y))
    print(end_node.position_x - start_node.position_x)
    print(total_cost)"""



"""class PathFindWindow(Frame):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.master.title("Path Finding")
        self.master.minsize(1400, 725)

        #grid_canvas = Canvas(self.master, width=800, height=700, bg="blue")
        #grid_canvas.grid(row=0, column=1)


        # example values
        for x in range(50):
            for y in range(20):
                btn = Button()
                btn.grid(column=x, row=y, sticky=N + S + E + W)"""


"""grid_size_btn = Button(self.master, text="Create grid")
grid_size_btn.pack()
grid_size_btn.place(x=900, y=50)

grid_elements_num = Text(self.master, height=1, width=20)
grid_elements_num.pack()
grid_elements_num.place(x=980, y=54)"""

"""def main():

    root = Tk()
    app = PathFindWindow()
    root.mainloop()


if __name__ == '__main__':
    main()
"""

def reconstruct_path(came_from, current):
    total_path = current

def a_star(start, goal, h):
    came_from = []

"""q = PriorityQueue()
    q.put((float('inf'), grid[1][2]))
    q.put((2.0, grid[1][2]))
    q.put((1.1, grid[1][2]))
    q.put((3.3, grid[1][2]))

    i = 0
    while not q.empty():
        next_item = q.get()
        print(next_item)
        if next_item[0] == 2.0:
            q.put(next_item)
            i += 1
            print("aaaa")
        if i == 4:
            break"""