'''
import numpy as np
import random

class Task5:
    def __init__(self, distance_matrix, n_ants=10, n_best=5, n_iterations=100,
                 decay=0.5, alpha=1, beta=2):
        """
        Ant Colony Optimization for finding the shortest route.

        Parameters:
        - distance_matrix: 2D numpy array of travel times/distances.
        - n_ants: number of ants per iteration
        - n_best: number of top ants depositing pheromone
        - n_iterations: total iterations
        - decay: pheromone evaporation rate
        - alpha: pheromone importance
        - beta: distance importance
        """
        self.distances = distance_matrix
        self.pheromone = np.ones(self.distances.shape) / len(distance_matrix)
        self.all_nodes = range(len(distance_matrix))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self, start=0):
        best_route = None
        best_cost = float('inf')

        for iteration in range(self.n_iterations):
            all_paths = self._generate_all_paths(start)
            # update pheromones based on best routes
            self._spread_pheromone(all_paths)
            # get the best route in this iteration
            shortest_path = min(all_paths, key=lambda x: x[1])

            if shortest_path[1] < best_cost:
                best_route, best_cost = shortest_path

            # evaporate pheromone
            self.pheromone *= (1 - self.decay)

            if (iteration + 1) % 10 == 0:
                print(f"Iteration {iteration+1}: Best Cost = {best_cost:.2f}")

        return best_route, best_cost

    def _spread_pheromone(self, paths):
        # deposit pheromone only from n_best paths
        sorted_paths = sorted(paths, key=lambda x: x[1])
        for path, cost in sorted_paths[:self.n_best]:
            for move in path:
                a, b = move
                self.pheromone[a][b] += 1.0 / cost

    def _generate_all_paths(self, start):
        all_paths = []
        for _ in range(self.n_ants):
            path = self._generate_path(start)
            total_cost = self._path_distance(path)
            all_paths.append((path, total_cost))
        return all_paths

    def _generate_path(self, start):
        path = []
        visited = set([start])
        current = start

        for _ in range(len(self.distances) - 1):
            next_node = self._pick_next_node(current, visited)
            path.append((current, next_node))
            current = next_node
            visited.add(current)

        path.append((current, start))  # return to start
        return path

    def _pick_next_node(self, current, visited):
        pheromone = np.copy(self.pheromone[current])
        pheromone[list(visited)] = 0  # ignore visited nodes

        prob = (pheromone ** self.alpha) * ((1.0 / (self.distances[current] + 1e-9)) ** self.beta)
        prob /= prob.sum()

        return np.random.choice(self.all_nodes, 1, p=prob)[0]

    def _path_distance(self, path):
        return sum(self.distances[a][b] for a, b in path)


# --- Example Use ---
distances = np.array([
 [0, 10, 12, 11, 14],
 [10, 0, 13, 15, 8],
 [12, 13, 0, 9, 14],
 [11, 15, 9, 0, 16],
 [14, 8, 14, 16, 0]
])

aco =Task5(distances, n_ants=10, n_best=5, n_iterations=50, decay=0.4, alpha=1, beta=2)
best_route, best_cost = aco.run()

print("\nBest Route:", best_route)
print("Total Trip Duration:", round(best_cost, 2), "minutes")
'''
import numpy as np

class ACO:
    def __init__(s, d, ants=10, best=5, iters=50, decay=0.5, a=1, b=2):
        s.d, s.p = d, np.ones(d.shape)/len(d)
        s.ants, s.best, s.iters, s.decay, s.a, s.b = ants, best, iters, decay, a, b
        s.nodes = range(len(d))

    def run(s):
        best_path, best_cost = None, 1e9
        for _ in range(s.iters):
            paths = [(p, s.cost(p)) for p in [s.path(0) for _ in range(s.ants)]]
            s.update(paths)
            p, c = min(paths, key=lambda x: x[1])
            if c < best_cost: best_path, best_cost = p, c
            s.p *= s.decay
        return best_path, best_cost

    def path(s, start):
        p, v, cur = [], {start}, start
        for _ in range(len(s.d)-1):
            nxt = s.next(cur, v)
            p.append((cur, nxt)); v.add(nxt); cur = nxt
        p.append((cur, start))
        return p

    def next(s, cur, v):
        ph = np.copy(s.p[cur]); ph[list(v)] = 0
        prob = (ph**s.a)*((1/(s.d[cur]+1e-9))**s.b); prob /= prob.sum()
        return np.random.choice(s.nodes, p=prob)

    def cost(s, p): return sum(s.d[a][b] for a,b in p)

    def update(s, paths):
        for p,c in sorted(paths, key=lambda x:x[1])[:s.best]:
            for a,b in p: s.p[a][b] += 1.0/c


# Example
d = np.array([[0,10,12,11,14],
              [10,0,13,15,8],
              [12,13,0,9,14],
              [11,15,9,0,16],
              [14,8,14,16,0]])

aco = ACO(d, ants=10, best=5, iters=30, decay=0.4, a=1, b=2)
path, cost = aco.run()
print("Best Path:", path)
print("Total Cost:", round(cost,2))
