def subset_sum_backtracking(numbers, target):
    subsets = []

    def backtrack(start, path_sum, path, subsets):
        if path_sum == target:
            subsets.append(path[:])  # found a valid subset
            return
        if path_sum > target or start >= len(numbers):
            return

        # Include the current element
        path.append(numbers[start])
        backtrack(start + 1, path_sum + numbers[start], path, subsets)
        path.pop()

        # Exclude the current element
        backtrack(start + 1, path_sum, path, subsets)

    backtrack(0, 0, [], subsets)
    return subsets

numbers = []
size = int(input("Enter the number of elements in the set: "))

for i in range(size):
    ele = int(input("Enter element " + str(i + 1) + ": "))
    numbers.append(ele)

target = int(input("\nEnter the target sum: "))

print("\nThe given set is: ", numbers)
print("Target: ", target)
print("\nSubsets:", subset_sum_backtracking(numbers, target))
