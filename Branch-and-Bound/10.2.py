def calculate_cost(cost_matrix, assignment):
    cost = 0
    for i, job in enumerate(assignment):
        cost += cost_matrix[i][job]
    return cost

def branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    branches = []
    branches.append((0, 0, []))
    
    best_cost = float('inf')
    best_assignment = None
    
    while branches:
        branches.sort(reverse=True)
        cost, level, assignment = branches.pop()
        
        if cost >= best_cost:
            continue
        
        if level == n:
            if cost < best_cost:
                best_cost = cost
                best_assignment = assignment
            continue
        
        for job in range(n):
            if job not in assignment:
                new_assignment = assignment + [job]
                new_cost = calculate_cost(cost_matrix, new_assignment)
                branches.append((new_cost, level + 1, new_assignment))
    
    return best_cost, best_assignment

n = int(input("Enter the number of jobs: "))
print("\n")

cost_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        cost = int(input(f"Enter the cost for person {i + 1} to job {j+ 1}: "))
        row.append(cost)
    print("\n")
    cost_matrix.append(row)

best_cost, best_assignment = branch_and_bound(cost_matrix)

print("Total cost:", best_cost)
print("Best assignment:", ["Job " + str(job + 1) for job in best_assignment])
