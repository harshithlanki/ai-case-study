## Case Study: Hogwarts School of Witchcraft and Wizardry

Hogwarts is a complex environment filled with magical obstacles and dynamic elements. This case study applies Artificial Intelligence (AI) search algorithms to solve problems within Hogwarts, such as navigating the castle, traversing a Triwizard Maze, and customizing a magic wand.

### Algorithm: Bidirectional Search - Triwizard Maze Challenge

**[Link to program: `[Your_GitHub_Link_Here]`]** (Replace with the actual link to your bidirectional search code file)

**Narrative:**

The Triwizard Tournament's final task requires students to navigate a treacherous maze filled with magical traps and dynamic obstacles. Two students, starting from different points (Gryffindor and Hufflepuff entrances), must work independently to find the Triwizard Cup (Goblet of Fire) at the maze's center. The maze dynamically changes its layout due to magical forces, adding to the complexity.

**Task:**

Implement a bidirectional search algorithm that simulates two students simultaneously searching the maze from their respective starting points towards the goal (the Goblet of Fire).  The maze has dynamic trap placement and modifications during the search process.

**Challenges:**

*   **Dynamic Maze:** The maze's structure changes randomly during the search due to magical forces, adding or removing traps. The algorithm must adapt to these changes.
*   **Two Starting Points:** The algorithm must manage two simultaneous searches, one from each starting location.
*   **Meeting Point:**  The algorithm needs to efficiently detect when the two searches meet in the middle to reconstruct the complete path.
*   **Optimality:** Due to the dynamic maze changes, optimality cannot be guaranteed, and the algorithm aims to find a good (but not necessarily perfect) path quickly.

**Extension:**

*   **Varying Maze Change Frequency:**  Implement different frequencies for the maze changes to observe the algorithm's performance under various levels of dynamism.
*   **Weighted Trap Costs:**  Assign different "costs" to different traps to simulate varying levels of danger.
*   **Heuristic Guidance:** Explore incorporating heuristic functions to guide the search, such as estimating the distance to the center of the maze.

**Algorithm Flowchart:**

1.  **Initialization:**
    *   Create two queues: `forward_queue` (starting from `start_a`) and `backward_queue` (starting from `goal`).
    *   Create two visited sets: `forward_visited` and `backward_visited`, initialized with their respective starting positions.
2.  **Search Loop:** While both queues are not empty:
    *   a. **Dynamic Maze Change:** With a probability (e.g., 20%), apply a `magic()` function to randomly alter the maze (add/remove traps).
    *   b. **Process Forward Queue:**
        *   Dequeue a node from `forward_queue`.
        *   Check if the node is in `backward_visited`:
            *   If yes, a meeting point is found. Reconstruct and return the path.
        *   Otherwise, add valid neighbors to `forward_queue`, updating `forward_visited` with their costs.
    *   c. **Process Backward Queue:**
        *   Dequeue a node from `backward_queue`.
        *   Check if the node is in `forward_visited`:
            *   If yes, a meeting point is found. Reconstruct and return the path.
        *   Otherwise, add valid neighbors to `backward_queue`, updating `backward_visited` with their costs.
3.  **No Path Found:** If both queues become empty without finding a meeting point, return "No path found."
4.  **Path Reconstruction:** Combine the paths from the forward and backward searches to create the complete path.

**Code:**

```python
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
