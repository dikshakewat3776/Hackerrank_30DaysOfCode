import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
# Write Your Code Here

for i in range(n):
    for j in range(0, n-1):
        if (a[j] > a[j+1]):
            a[j] = a[j] ^ a[j+1];
            a[j+1] = a[j] ^ a[j+1];
            a[j] = a[j] ^ a[j+1];
            numSwaps+=1;


print("Array is sorted in {} swaps." .format(numSwaps))
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))