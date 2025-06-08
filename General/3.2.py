#COUNT SORTING ALGORITHM

#Input list 
size = int(input("Enter the size of the List: "))
nums = []

for k in range(size):
    nums.append(int(input("Enter element " + str(k+1) + ": ")))

print("\nList:", nums)

#Method 1
#Time Complexity: O(n^2)

def comparison_count_sort(nums):
    count = [0] * len(nums)
    nums_sorted = [0] * len(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] >= nums[j]:
                count[i] += 1
            elif nums[i] <= nums[j]:
                count[j] += 1
    for i in range(len(nums)):
        nums_sorted[count[i]] = nums[i]
    return nums_sorted

print("\nSorted List:",comparison_count_sort(nums))

#Method 2
#Time Complexity: O(n)

def comparison_count_sort1(nums):
    n = len(nums)
    count = [0] * (max(nums) + 1)  # Initialize count array with length max(nums) + 1
    nums_sorted = [0] * n

    # Count occurrences of each element
    for num in nums:
        count[num] += 1

    # Calculate Cumulative Sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Sorted array
    for num in reversed(nums):
        nums_sorted[count[num] - 1] = num
        count[num] -= 1

    return nums_sorted

print("Sorted List:",comparison_count_sort1(nums))


