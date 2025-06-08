import random
import time

n = int(input("Enter the number of elements: "))
a = random.sample(range(1, 1000000), n)
a.sort()

# Recursive Binary Search
def binarySearch(L, low, high, key):
    # Measure start time
    start = time.time()  
    if high >= low:  
        mid = (low + high) // 2  
        if L[mid] == key:  
            # Measure end time if key is found
            end = time.time()
            return end - start  
        elif L[mid] > key:     
            return binarySearch(L, low, mid - 1, key)  
        else:   
            return binarySearch(L, mid + 1, high, key)  
    else: 
        # Measure end time if key is not found
        end = time.time()  
        return end - start  

element = random.randint(1, 1000000)



# Perform recursive binary search
time_recursive = binarySearch(a, 0, len(a) - 1, element)  
print("Time taken for Recursive Binary Search:", time_recursive)

# Non-Recursive Binary Search
def binary_search(L, key):
    # Measure start time
    start = time.time()
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low) // 2
        if L[mid] < key:
            low = mid + 1
        elif L[mid] > key:
            high = mid - 1
        else:
            # Measure end time if key is found
            end = time.time()
            return end - start

    # Measure end time if key is not found
    end = time.time()
    return end - start

# Perform non-recursive binary search
time_non_recursive = binary_search(a, element)  
print("Time taken for Non-Recursive Binary Search:", time_non_recursive)

