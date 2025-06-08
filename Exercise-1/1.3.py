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

t = insertionSort(a)
print("Time taken for sorting an unsorted array:", t)

t = insertionSort(a)
print("Time taken for sorting an ascending sorted array:", t)

a.reverse()
t = insertionSort(a)
print("Time taken for sorting a descending sorted array:", t)
