#INVERSIONS IN A LIST

#Input list 
size = int(input("Enter the size of the List: "))
nums = []

for k in range(size):
    nums.append(int(input("Enter element " + str(k+1) + ": ")))

print("\nList:", nums)

#Time Complexity: O(n*logn)
#Mergesort algorithm

def count_inversions2(nums):
    return merge_sort(nums, 0, len(nums) - 1)

def merge_sort(nums, left, right):
    count2 = 0
    if left < right:
        mid = (left + right) // 2
        count2 += merge_sort(nums, left, mid)
        count2 += merge_sort(nums, mid + 1, right)
        count2 += merge(nums, left, mid, right)
    return count2

def merge(nums, left, mid, right):
    count2 = 0
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            k += 1
            i += 1
        else:
            temp[k] = nums[j]
            k += 1
            j += 1
            count2 += mid - i + 1

    while i <= mid:
        temp[k] = nums[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = nums[j]
        k += 1
        j += 1

    for p in range(len(temp)):
        nums[left + p] = temp[p]

    return count2

print("Number of inversions using mergesort algorithm is: ", count_inversions2(nums))
