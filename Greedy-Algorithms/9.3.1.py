def knapsack(values, weights, capacity):
    n = len(values)
    value_by_weight = [(values[i] / weights[i], i) for i in range(n)]
    value_by_weight.sort(reverse=True)
    
    total_value = 0.0
    included = []

    for _, i in value_by_weight:
        if weights[i] <= capacity:
            total_value += values[i]
            capacity -= weights[i]
            included.append((i, 1))  
        else:
            fraction = capacity / weights[i]
            total_value += fraction * values[i]
            included.append((i, fraction))  
            break
    
    return total_value, included

items = int(input("Enter the number of items: "))
print("\n")

values = []
weights = []

for i in range(items):
    value_item = int(input("Enter the value of item " + str(i + 1) + ": "))
    values.append(value_item)
    weight_item = int(input("Enter the weight of item " + str(i + 1) + ": "))
    weights.append(weight_item)
    print("\n")

capacity = int(input("Enter the capacity of the knapsack: "))

total_value, included_items = knapsack(values, weights, capacity)
print("\nTotal value:", total_value)
print("Items included:")
for item, fraction in included_items:
    if fraction == 1:
        print(f"Item {item + 1}: fully included")
    else:
        print(f"Item {item + 1}: {fraction * 100:.2f}% included")
