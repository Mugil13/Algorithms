def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for j in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    included = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included.append(i - 1)
            w -= weights[i - 1]
        i -= 1
    
    return dp[n][capacity], included[::-1]

items = int(input("Enter the number of items: "))
print("\n")

values = []
weights = []

for i in range(items):
    value_item = int(input("Enter the value of item " + str(i+1) + ": "))
    values.append(value_item)
    weight_item = int(input("Enter the weight of item " + str(i+1) + ": "))
    weights.append(weight_item)
    print("\n")

capacity = int(input("Enter the capacity of the knapsack: "))

total_value, included_items = knapsack(values, weights, capacity)
print("\nTotal value:", total_value)
print("Items included:", [i + 1 for i in included_items])

