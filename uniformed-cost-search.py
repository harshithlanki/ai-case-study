import heapq

def uniform_cost_search(start_node, goal_node, get_neighbors, cost_function):
    """
    Finds the least-cost path from start_node to goal_node using UCS.

    Args:
        start_node: The starting node.
        goal_node: The goal node.
        get_neighbors: A function that takes a node and returns a list of (neighbor, cost) tuples.
        cost_function: A function that calculates the cost of moving from one node to another.

    Returns:
        A list of nodes representing the least-cost path, or None if no path is found.
    """

    priority_queue = [(0, start_node, [])]  # (cost, node, path)
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal_node:
            return path + [current_node]

        for neighbor, neighbor_cost in get_neighbors(current_node):
            new_cost = cost + neighbor_cost
            heapq.heappush(priority_queue, (new_cost, neighbor, path + [current_node]))

    return None #No path found

def example_cost_function(current_node, next_node):
    """
    Example cost function considering danger level, distance, and energy.
    """
    # This is just an example, you would need to adapt this to your Hogwarts world
    danger_level = get_danger_level(next_node)
    distance = calculate_distance(current_node, next_node)
    energy_cost = calculate_energy_cost(current_node, next_node)

    cost = danger_level * 1.2 + distance * 1.0 + energy_cost * 0.8  # Adjust weights as needed
    return cost

def get_danger_level(node):
  #Dummy function to get danger level
  return 1

def calculate_distance(node_1, node_2):
  #Dummy function to find distance
  return 1

def calculate_energy_cost(node_1, node_2):
  #Dummy function to calc energy cost
  return 1

def get_neighbors_example(node):
    """
    Example function to return neighbors with costs. Adapt to Hogwarts map.
    """
    neighbors = []

    if node == "Great Hall":
        neighbors.append(("Potions Classroom", example_cost_function("Great Hall", "Potions Classroom")))
        neighbors.append(("Library", example_cost_function("Great Hall", "Library")))
    elif node == "Potions Classroom":
        neighbors.append(("Great Hall", example_cost_function("Potions Classroom", "Great Hall")))
    #Add the remaining cases here.

    return neighbors

# Example Usage
start = "Great Hall"
goal = "Potions Classroom"
path = uniform_cost_search(start, goal, get_neighbors_example, example_cost_function)

if path:
    print("Path found:", path)
else:
    print("No path found.")
