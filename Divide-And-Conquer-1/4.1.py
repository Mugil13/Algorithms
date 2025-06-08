# Input list 
size = int(input("Enter the size of the List: "))
nums = []

for k in range(size):
    nums.append(int(input("Enter element " + str(k+1) + ": ")))

print("\nList:", nums)

# Finding MAX using divide-and-conquer
def findMax(nums, i, j):
    if (i == j):
        return nums[i]
    elif ((j - i) == 1):
        if (nums[i]>nums[j]):
            return nums[i]
        else:
            return nums[j]
    else:
        mid = (i + j) // 2  
        
        leftMax = findMax(nums, i, mid)
        rightMax = findMax(nums, mid+1, j)

        if (leftMax > rightMax):
            return leftMax
        else:
            return rightMax

print("The maximum of the given list is: ", findMax(nums, 0, size-1))
