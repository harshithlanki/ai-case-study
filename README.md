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

# Example Hogwarts maze
hogwarts_maze = [
    [".", ".", ".", "T", ".", "."],
    [".", "T", ".", "T", ".", "."],
    [".", ".", ".", ".", ".", "T"],
    ["T", ".", "T", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", "T", ".", "G"] 
**OUTPUT**
Path to the Goblet: [(0, 0), (1, 0), (2, 0), ..., (5, 5)]
Path cost: 11



    
## Case Study: Hogwarts School of Witchcraft and Wizardry

Hogwarts is a complex environment filled with magical obstacles and dynamic elements. This case study applies Artificial Intelligence (AI) search algorithms to solve problems within Hogwarts, such as navigating the castle, traversing a Triwizard Maze, and customizing a magic wand.

### Algorithm: Simulated Annealing - Wand Customization

**[Link to program: `[Your_GitHub_Link_Here]`]** (Replace with the actual link to your Simulated Annealing code file)

**Narrative:**

A young witch or wizard needs to customize their wand to maximize its compatibility and magical power. Wand properties such as core type (phoenix feather, dragon heartstring, unicorn hair), wood type (holly, willow, elder, oak), and length all contribute to its overall performance. Some combinations are inherently more powerful, while others might lead to malfunctions. The student uses simulated annealing to find the best combination of wand properties.

**Task:**

Implement a simulated annealing algorithm to optimize the wand's properties (core, wood, length) to achieve the highest possible fitness score, considering both power and stability (avoiding malfunctions).

**Challenges:**

*   **Defining a Fitness Function:** Designing a fitness function that accurately reflects the desired properties of a good wand (power, compatibility, stability) is crucial. The fitness function should reward desirable traits and penalize undesirable ones (e.g., high malfunction probability).
*   **Neighborhood Generation:** Creating a `get_neighbor` function that generates slightly modified wands (neighbors) is essential. The modifications should be reasonable and allow for exploration of the search space.
*   **Temperature Schedule:** Choosing appropriate initial temperature and cooling rate is important for balancing exploration (avoiding local optima) and exploitation (finding the best solution). A temperature that cools too rapidly may trap the search in a suboptimal region.
*   **Malfunctions:** Simulating random wand malfunctions helps to promote wands that offer robust performance despite imperfections.

**Extension:**

*   **Adding More Wand Properties:** Include additional wand properties (flexibility, handle design) and incorporate their impact on the fitness function.
*   **Rare Materials:** Introduce rare magical materials that can provide significant boosts but may also increase instability.
*   **User Preferences:** Allow the user to specify preferences for certain wand properties and incorporate these into the fitness function.

**Algorithm Flowchart:**

1.  **Initialize:**
    *   Create an initial wand with random or default properties.
    *   Set initial temperature, cooling rate, and maximum iterations.
2.  **Iterate:** For each iteration:
    *   a. **Generate Neighbor:** Create a new wand by slightly modifying the properties of the current wand.
    *   b. **Calculate Fitness Change:** Determine the change in fitness between the neighbor wand and the current wand.
    *   c. **Acceptance Probability:** Calculate the probability of accepting the neighbor wand based on the change in fitness and the current temperature:
        *   If `fitness(neighbor) > fitness(current_wand)` (better fitness), accept the neighbor.
        *   Otherwise, accept the neighbor with probability `exp(delta_fitness / current_temperature)`.
    *   d. **Update Current Wand:** If the neighbor is accepted, update the current wand.
    *   e. **Cool Temperature:** Reduce the temperature using the cooling rate: `temperature = temperature * cooling_rate`.
    *   f.  **Best Wand** Check if it's the best wand.
3.  **Termination:** When the maximum number of iterations is reached or the temperature is sufficiently low, return the best wand found.
**OUTPUT**
Initial Wand: {'core': 'unicorn', 'wood': 'willow', 'length': 9.0}
Best Wand: {'core': 'phoenix', 'wood': 'holly', 'length': 11.23456789012345}
Best Wand Fitness: 10.0







## Case Study: Hogwarts School of Witchcraft and Wizardry

Hogwarts is a complex environment filled with magical obstacles and dynamic elements. This case study applies Artificial Intelligence (AI) search algorithms to solve problems within Hogwarts, such as navigating the castle, traversing a Triwizard Maze, and customizing a magic wand.

### Algorithm: Uniform Cost Search (UCS) - Magical Item Retrieval

**[Link to program: `[Your_GitHub_Link_Here]`]** (Replace with the actual link to your UCS code file)

**Narrative:**

A student needs to retrieve a set of magical items, such as potion ingredients or enchanted books, scattered throughout Hogwarts. The student must navigate the castle while minimizing the use of energy, avoiding dangerous areas (e.g., patrolled by Filch or Dementors), and taking the least amount of time. Each path through Hogwarts carries a different cost.

**Task:**

Implement the Uniform Cost Search (UCS) algorithm to find the least-cost path for collecting all the required magical items, considering energy consumption, danger levels, and time taken as cost factors.

**Challenges:**

*   **Defining the Cost Function:**  Creating an accurate cost function that combines energy consumption, danger levels, and time taken is crucial.  Assigning appropriate weights to each factor will impact the resulting path.
*   **Dynamic Costs:**  The cost of traversing certain paths may change dynamically (e.g., an area becomes more dangerous because Dementors are patrolling, or a shortcut opens up). The algorithm must adapt to these changes.
*   **Multiple Items:** The algorithm must be able to handle the retrieval of multiple items in an optimal order, considering the cost of traveling between them. This could be modeled as a Traveling Salesperson Problem variation.
*   **Restricted Areas/Spells**: Some spells might cost extra energy or specific areas will give penalties.

**Extension:**

*   **Time-Varying Costs:**  Implement costs that vary based on the time of day (e.g., certain corridors are more dangerous at night).
*   **Limited Inventory:**  Introduce a limited inventory to carry items, requiring the student to return to a storage location periodically.
*   **Partial Credit:** Allowing partial credit for collecting some items even if all can't be collected in a feasible path.

**Algorithm Flowchart:**

1.  **Initialization:**
    *   Create a priority queue containing the starting location with a cost of 0.
    *   Initialize a set of visited locations.
2.  **Iterate:** While the priority queue is not empty:
    *   a. **Dequeue Node:** Remove the location with the lowest cost from the priority queue.
    *   b. **Visited Check:** If the location has already been visited, continue to the next iteration.
    *   c. **Mark Visited:** Mark the current location as visited.
    *   d. **Goal Check:** If the current location contains the required item, add the item to a 'collected' set (or inventory). If all the required items have been collected, return the path.
    *   e. **Expand Neighbors:** Find all accessible neighboring locations.
    *   f. **Calculate Costs:** For each neighbor:
        *   Calculate the cost of moving from the current location to the neighbor (using the cost function).
        *   Add the neighbor to the priority queue with the updated cost.
3.  **No Path Found:** If the priority queue becomes empty before collecting all items, return "No path found."
**OUTPUT**
Path found: ['Great Hall', 'Potions Classroom'] 
