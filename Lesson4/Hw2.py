n = int(input("How many bushes are there? "))
a = list(map(int, input("How many berries are there on each bush (separated by space): ").split()))

maxB = 0

for i in range(n):
    b = a[i] + a[(i-1)%n] + a[(i+1)%n]
    maxB = max(maxB, b)  

print(f"Maximum of berries can be obtained at once is {maxB}")