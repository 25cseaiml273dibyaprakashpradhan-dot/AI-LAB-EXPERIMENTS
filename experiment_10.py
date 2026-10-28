from itertools import permutations

def traveling_salesman(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)
    
    min_cost = float('inf')
    best_path = None
    
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start] + list(perm) + [start]
        
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i+1]]
            
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
            
    return best_path, min_cost

# MAIN PROGRAM
n = int(input("Enter no. of cities: "))
print("Enter the cost matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting city (0 to 3): "))

path, cost = traveling_salesman(graph, start)

print("\nOptimal Path:", " -> ".join(map(str, path)))
print("minimum cost:", cost)
