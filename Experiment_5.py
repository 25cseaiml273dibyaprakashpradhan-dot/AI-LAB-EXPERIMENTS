def minmax(depth, node_index, is_max, scores, height):
    if depth == height:
        return scores[node_index]
    
    if is_max:
        return max(
            minmax(depth + 1, node_index * 2, False, scores, height),
            minmax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minmax(depth + 1, node_index * 2, True, scores, height),
            minmax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# MAIN PROGRAM
scores = list(map(int, input("Enter 8 node value space-separated: ").split()))
height = 3

result = minmax(0, 0, True, scores, height)

print(f"The optimal value is :{result}")
print("Result:- We have successfully implemented min-max algorithm using python.")
