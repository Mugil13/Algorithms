def max_score(grid):
    n = len(grid[0])
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]

    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1] + abs(grid[0][j] - grid[1][j]))
        dp[1][j] = max(dp[1][j-1], dp[0][j-1] + abs(grid[0][j] - grid[1][j]))

    return max(dp[0][-1], dp[1][-1])
    
grid = []
row1 = []
row2 = []

n = int(input("Enter the number of columns: "))
print("Enter elements in row 1: ")
for i in range(n):
    row1.append(int(input("Enter element at column " + str(i+1) + ": ")))
print("Enter elements in row 2: ")
for l in range(n):
    row2.append(int(input("Enter element at column " + str(l+1) + ": ")))

grid.append(row1)
grid.append(row2)

print("Maximum Score is: ", max_score(grid))