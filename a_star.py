import math
import time
from queue import PriorityQueue


# Calculate distance between the nodes (euclidean distance)
def calculate_node_distance(node_a, node_b):
    return math.sqrt((node_b.position_x - node_a.position_x)**2 + (node_b.position_y - node_a.position_y)**2)


def solve_a_star(grid, start_node_coords, end_node_coords, visited_list):

    alg_start = time.perf_counter()

    # Reset parameters of all visited nodes considered in previous path creation
    for node in visited_list:
        if not node.obstacle:
            node.g_cost = float('inf')
            node.h_cost = float('inf')
            node.visited = False
            node.parent = None

    # Create priority queue for nodes
    open_list = PriorityQueue()
    old_visited_list = visited_list
    visited_list = []

    # Get node objects for start and end of the path
    start_node = grid[start_node_coords[0]][start_node_coords[1]]
    end_node = grid[end_node_coords[0]][end_node_coords[1]]

    # Set initial local distance from starting node (0 for starting node of course)
    # and calculate distance from start to end node
    start_node.g_cost = float(0)
    start_node.h_cost = calculate_node_distance(start_node, end_node)

    # Add start node to the priority queue to have a starting point
    open_list.put((start_node.h_cost, (start_node.position_x, start_node.position_y)))
    visited_list.append(start_node)

    while not open_list.empty():

        # Get node with the shortest distance to the end node from the list
        element = open_list.get()
        current_node = grid[element[1][0]][element[1][1]]

        # If the node happens to be the end node just finish the loop as we reached the target
        if current_node == end_node:
            break

        # Move current node to a closed list and set it as visited
        current_node.visited = True

        # Loop through all neighbours of a current node
        for neighbour in current_node.neighbours:
            visited_list.append(neighbour) if neighbour not in visited_list else visited_list
            # Skip the node if it was already visited or is an obstacle
            if neighbour.visited is True or neighbour.obstacle is True:
                continue
            # Calculate distance from current node to its neighbour
            cost_to_parent = current_node.g_cost + calculate_node_distance(current_node, neighbour)

            # Update the neighbour if calculated distance is lower than currently stored distance from node to start
            if cost_to_parent < neighbour.g_cost:
                neighbour.g_cost = cost_to_parent
                neighbour.h_cost = neighbour.g_cost + calculate_node_distance(neighbour, end_node)
                neighbour.f_cost = neighbour.g_cost + neighbour.h_cost
                neighbour.parent = current_node

                # Add neighbour to a list of not visited nodes
                open_list.put((neighbour.h_cost, (neighbour.position_x, neighbour.position_y)))
                neighbour.visited = True

    # Calculate total path cost from start to end
    total_cost = round(calculate_node_distance(start_node, end_node), 5)

    # Get time after algorithm is finished and calculate total time
    alg_end = time.perf_counter()
    alg_cost = round(alg_end - alg_start, 5)
    return visited_list, old_visited_list, total_cost, alg_cost
