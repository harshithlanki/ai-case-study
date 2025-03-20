import random
import math

def fitness(wand):
    """Scores a wand based on criteria."""
    score = 0
    
    # Example Scoring function (can be anything you want)
    if wand["core"] == "phoenix": score += 5
    if wand["wood"] == "holly": score += 3
    if wand["length"] > 10 and wand["length"] < 12: score += 2
    if wand["wood"] == "elder" and wand["core"] == "dragon": score += 10 # Powerful combo
    if wand["wood"] == "willow" and wand["core"] == "unicorn": score -= 5 # Bad combo

    # Simulate malfunctions (e.g. more prone if the length is off)
    if wand["length"] < 8 or wand["length"] > 14:
      malfunction_prob = (abs(wand["length"] - 11) - 3 ) * 0.1 # max malfunction is 20% if wand is far away from 11
      if malfunction_prob > random.random():
        score -= 10
    return score

def get_neighbor(wand):
    """Generates a slightly modified wand."""
    new_wand = wand.copy()
    
    # Randomly modify one of the wand properties
    choice = random.randint(1,3)
    
    if choice == 1:
        new_wand["core"] = random.choice(["phoenix", "dragon", "unicorn"])
    elif choice == 2:
      new_wand["wood"] = random.choice(["holly", "willow", "elder", "oak"])
    else:
        new_wand["length"] += random.uniform(-1.5, 1.5) # Add or subtract 1.5
        new_wand["length"] = max(7, min(15, new_wand["length"])) # Keep length between 7 and 15

    return new_wand


def simulated_annealing(initial_wand, max_iterations, initial_temperature, cooling_rate):
    current_wand = initial_wand
    best_wand = initial_wand
    current_temperature = initial_temperature

    for _ in range(max_iterations):
      
        neighbor = get_neighbor(current_wand)
        delta_fitness = fitness(neighbor) - fitness(current_wand)

        if delta_fitness > 0 or random.random() < math.exp(delta_fitness / current_temperature):
            current_wand = neighbor
        if fitness(current_wand) > fitness(best_wand):
          best_wand = current_wand

        current_temperature *= cooling_rate
        if current_temperature < 0.00001:
            break # Stop if temperature is too low.
    return best_wand

if __name__ == "__main__":
    initial_wand = {"core": "unicorn", "wood": "willow", "length": 9.0}
    max_iterations = 10000
    initial_temperature = 100
    cooling_rate = 0.95

    best_wand = simulated_annealing(initial_wand, max_iterations, initial_temperature, cooling_rate)

    print("Initial Wand:", initial_wand)
    print("Best Wand:", best_wand)
    print("Best Wand Fitness:", fitness(best_wand))
