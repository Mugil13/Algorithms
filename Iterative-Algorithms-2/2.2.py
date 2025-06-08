#Method 1

n = int(input("Enter the value of n: "))
sum = (n*(n+1)*(n+2))/6
print(int(sum))

#Method 2

m = int(input("Enter the value of m: "))
final_sum = 0
sum = 0

for i in range(m):
    sum = ((i+1)*(i+2))/2
    final_sum += sum
    sum = 0

print(int(final_sum))

