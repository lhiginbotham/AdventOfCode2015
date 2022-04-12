from collections import defaultdict
import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

edges = defaultdict(lambda: defaultdict(lambda: None))
cities = set()

for edge in inp:
    components = edge.split()
    edges[components[0]][components[2]] = int(components[4])
    edges[components[2]][components[0]] = int(components[4])
    cities.add(components[0])
    cities.add(components[2])

best_route_cost = None
for city_path in itertools.permutations(cities):
    path_edge_costs = [ edges[city_path[i]][city_path[i + 1]] for i in range(len(city_path) - 1) ]
    if any([ edge_cost is None for edge_cost in path_edge_costs ]):
        continue

    path_cost = sum(path_edge_costs)
    if best_route_cost is None or best_route_cost > path_cost:
        best_route_cost = path_cost

print(best_route_cost)
