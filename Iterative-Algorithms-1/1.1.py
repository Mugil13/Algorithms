import random
import time

def generate_unique_random_list(n):
    start = time.time()
    if n <= 0:
        return [], 0
    unique_values = set()
    while len(unique_values) < n:
        unique_values.add(random.randint(1, 1000))  
    end = time.time()
    return list(unique_values), end - start

n = int(input("Enter the number of unique random values to generate: "))
random_list, time_taken = generate_unique_random_list(n)
print("Generated list of unique random values:", random_list)
print("Time taken:", time_taken, "seconds")
