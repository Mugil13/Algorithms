#Input list 
size = int(input("Enter the size of the List: "))
nums = []

for k in range(size):
    nums.append(int(input("Enter element " + str(k+1) + ": ")))

print("\nList:", nums)

# Insertion Sort
def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("Sorted List using insertion sort: ",insertionSort(nums))

kthele1 = int(input("\nEnter the value of k: "))
print("The " + str(kthele1) + " smallest element using Insertion Sort algorithm is: ", nums[kthele1-1])

#Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr

sorted_nums_quickSort = quickSort(nums, 0, len(nums) - 1)
print("Sorted List using Quick sort:", sorted_nums_quickSort)

kthele2 = int(input("Enter the value of k: "))
print("The " + str(kthele2) + " smallest element using Quick Sort algorithm is:", sorted_nums_quickSort[kthele2 - 1])
