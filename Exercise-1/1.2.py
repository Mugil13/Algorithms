import random
import time

n = int(input("Enter the number of elements: "))
a = random.sample(range(1, 1000000), n)
l = a.copy()

# Insertion Sort
def insertionSort(arr):
    start = time.time()
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
    end = time.time()
    return end - start

# Shell Sort
def shellSort(arr):
    start = time.time()
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap = gap // 2
    end = time.time()
    return end - start

# Counting Sort (used in Radix Sort)
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[int((index) % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Radix Sort
def radixSort(arr):
    start = time.time()
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10
    end = time.time()
    return end - start

t_insertion = insertionSort(a.copy())
print("Time Taken for Insertion Sort:", t_insertion)
a = l.copy()

t_shell = shellSort(a.copy())
print("Time Taken for Shell Sort:", t_shell)
a = l.copy()

t_radix = radixSort(a.copy())
print("Time Taken for Radix Sort:", t_radix)
