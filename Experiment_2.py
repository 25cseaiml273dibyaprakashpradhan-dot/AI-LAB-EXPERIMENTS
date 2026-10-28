def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Main program
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex name: ").strip()
    neighbors = input(
        f"Enter neighbors of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbors

start = input("Enter the starting vertex: ").strip()

print("\nGraph:", graph)
print("DFS Traversal:", end=" ")

visited = set()
dfs(graph, start, visited)

print()
