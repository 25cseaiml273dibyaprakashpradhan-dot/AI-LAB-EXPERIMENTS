from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, [(0, 0)]))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        if jug1 == target or jug2 == target:
            return path
            
        next_states = [
            (capacity1, jug2),             # Fill Jug 1
            (jug1, capacity2),             # Fill Jug 2
            (0, jug2),                     # Empty Jug 1
            (jug1, 0),                     # Empty Jug 2
            # Pour Jug 1 to Jug 2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),
            # Pour Jug 2 to Jug 1
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path + [state]))
                
    return None

# MAIN PROGRAM
jug1_cap = int(input("Enter capacity of jug 1: "))
jug2_cap = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target volume: "))

solution = water_jug(jug1_cap, jug2_cap, target)

if solution:
    print("steps to reach target:")
    for step in solution:
        print(step)
else:
    print("NO solution exists")
