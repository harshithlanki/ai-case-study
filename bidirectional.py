import heapq
import random

class HogwartsMaze:
    def __init__(self, grid, start_a, start_b, goal):
        self.grid = grid
        self.start_a = start_a
        self.start_b = start_b
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != "T"  # 'T' represents traps

    def neighbors(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                yield (nx, ny)

    def apply_magic(self):
        """Randomly change the maze by adding/removing traps or moving walls."""
        for _ in range(random.randint(1, 3)):  # Simulate 1-3 magical changes
            x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.grid[x][y] == ".":
                self.grid[x][y] = "T"  # Add a trap
            elif self.grid[x][y] == "T":
                self.grid[x][y] = "."  # Remove a trap

    def bidirectional_search(self):
        forward_queue = [(0, self.start_a)]  # (cost, position)
        backward_queue = [(0, self.goal)]
        forward_visited = {self.start_a: 0}
        backward_visited = {self.goal: 0}

        def process_queue(queue, visited, other_visited):
            cost, current = heapq.heappop(queue)
            if current in other_visited:
                return current, cost + other_visited[current]

            for neighbor in self.neighbors(*current):
                new_cost = cost + 1
                if neighbor not in visited or new_cost < visited[neighbor]:
                    visited[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))
            return None, None

        while forward_queue and backward_queue:
            # Magical maze changes periodically
            if random.random() < 0.2:  # 20% chance of maze alteration
                self.apply_magic()

            # Expand forward search
            result, path_cost = process_queue(forward_queue, forward_visited, backward_visited)
            if result:
                return self.reconstruct_path(result, forward_visited, backward_visited), path_cost

            # Expand backward search
            result, path_cost = process_queue(backward_queue, backward_visited, forward_visited)
            if result:
                return self.reconstruct_path(result, backward_visited, forward_visited, reverse=True), path_cost

        return None, float('inf')  # No path found

    def reconstruct_path(self, meeting_point, visited_a, visited_b, reverse=False):
        path = []
        current = meeting_point
        while current:
            path.append(current)
            current = self.get_parent(visited_a, current)
        if not reverse:
            path.reverse()
        current = self.get_parent(visited_b, meeting_point)
        while current:
            path.append(current)
            current = self.get_parent(visited_b, current)
        return path

    def get_parent(self, visited, node):
        for neighbor in self.neighbors(*node):
            if visited.get(neighbor, float('inf')) == visited[node] - 1:
                return neighbor
        return None


# Example Hogwarts maze
hogwarts_maze = [
    [".", ".", ".", "T", ".", "."],
    [".", "T", ".", "T", ".", "."],
    [".", ".", ".", ".", ".", "T"],
    ["T", ".", "T", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", "T", ".", "G"]  # 'G' represents Goblet
]

# Initialize maze
start_a = (0, 0)  # Gryffindor entry
start_b = (5, 0)  # Hufflepuff entry
goal = (5, 5)
maze = HogwartsMaze(hogwarts_maze, start_a, start_b, goal)

# Run bidirectional search
path, cost = maze.bidirectional_search()
print("Path to the Goblet:", path)
print("Path cost:", cost)
