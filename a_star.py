import math


def calculate_node_distance(node_a, node_b):
    return math.sqrt(((node_a.position_x - node_b.position_x)**2) + ((node_a.position_y - node_b.position_y)**2))


def solve_a_star(grid, start_coord, end_coord):
    open_list = []
    closed_list = []

    start_node = grid[start_coord[0]][start_coord[1]]
    end_node = grid[end_coord[0]][end_coord[1]]
    current_node = start_node
    open_list.append(current_node)

    while len(open_list) > 0 and current_node != end_node:

        # Get node from the list
        current_node = open_list[0]

        # Find node with smallest cost
        current_index = 0
        for index, node in enumerate(open_list):
            if node.f_cost < current_node.f_cost:
                current_node = node
                current_index = index

        # Move current node to a closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        current_node.visited = True

        for neighbour in current_node.neighbours:
            if neighbour.visited is True or neighbour.obstacle is True:
                continue
            lower_goal = current_node.g_cost + calculate_node_distance(current_node, neighbour)

            if lower_goal < neighbour.g_cost:
                neighbour.g_cost = lower_goal
                neighbour.h_cost = neighbour.g_cost + calculate_node_distance(neighbour, end_node)
                neighbour.parent = current_node
                open_list.append(neighbour)
                neighbour.visited = True

    total_cost = calculate_node_distance(start_node, end_node)
    print("Start: " + str(start_node.position_x) + ", " + str(start_node.position_y) )
    print("End: " + str(end_node.position_x) + ", " + str(end_node.position_y))
    print(end_node.position_x - start_node.position_x)
    print(total_cost)



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

