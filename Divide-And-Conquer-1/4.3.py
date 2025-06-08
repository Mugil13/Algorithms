#Input list 
size = int(input("Enter the size of the List: "))
nums = []

for k in range(size):
    nums.append(int(input("Enter element " + str(k+1) + ": ")))

print("\nList:", nums)

#Maximum SubArray sum
def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
    
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
    
    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    left_sum = max_subarray_sum(arr, low, mid)
    right_sum = max_subarray_sum(arr, mid + 1, high)
    cross_sum = max_crossing_subarray(arr, low, mid, high)
    
    return max(left_sum, right_sum, cross_sum)

print("Maximum Subarray Sum:", max_subarray_sum(nums, 0, len(nums) - 1))
