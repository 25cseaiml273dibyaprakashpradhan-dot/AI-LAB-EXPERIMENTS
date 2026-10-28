from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("O/P")
    print("BFS Traversal : ", end="")
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end="")  # Printed side-by-side with no spaces as per your output
        
        # Check if the vertex exists in the graph to avoid KeyError
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    print()  # Final new line

# --- Main Program Execution ---
print("simple input:-")
n = int(input("Enter the number of vertices: "))

graph = {}

# Looping dynamically based on the number of vertices provided
for i in range(1, n + 1):
    vertex = input(f"Enter vertex {i}: ")
    
    # Matching the exact format: "Enter adjacent of vertex [Name] (space-separated): "
    adjacent_input = input(f"Enter adjacent of vertex {vertex} (space-separated): ")
    
    # Split the input string into a list of neighboring nodes. 
    # If the user leaves it blank (like for E and F), it saves an empty list [].
    if adjacent_input.strip():
        graph[vertex] = adjacent_input.split()
    else:
        graph[vertex] = []

# Getting the starting vertex to run the algorithm
start_vertex = input("Enter the starting vertex: ")

# Executing the BFS algorithm
bfs(graph, start_vertex)
