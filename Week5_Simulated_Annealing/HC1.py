
import random
from itertools import combinations

N = 4

def cost(state):
    conflicts = 0

    for i, j in combinations(range(N), 2):
        if abs(state[i] - state[j]) == abs(i - j):
            conflicts += 1

    return conflicts

def hill_climbing():
    current = [3, 1, 2, 0]

    while True:
        print("Current:", current, "Cost:", cost(current))

        if cost(current) == 0:
            return current

        neighbors = []

        for i, j in combinations(range(N), 2):
            neighbor = current.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

            neighbors.append((cost(neighbor), i, j, neighbor))

        best_cost = min(x[0] for x in neighbors)

        if best_cost >= cost(current):
            current = random.sample(range(N), N)
            print("Random Restart:", current)
            continue

        best = min(
            (x for x in neighbors if x[0] == best_cost),
            key=lambda x: (x[1], x[2])
        )

        current = best[3]

solution = hill_climbing()

print("Goal State:", solution)
print("Final Cost:", cost(solution))
