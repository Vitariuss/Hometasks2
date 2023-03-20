n = int(input("Write the number of elements in array: "))

array = []
for i in range(n):
    array.append(int(input(f"Write the number # {i+1}: ")))

x = int(input("What number should we find: "))

count = 0

for i in array:
    if i == x:
        count += 1

print(f"There are {count} instances of {x} in your array.")