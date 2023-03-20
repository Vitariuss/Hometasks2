n = int(input("Write the number of elements: "))

array = []
for i in range(n):
    array.append(int(input(f"Write the element # {i+1}: ")))

x = int(input("Write the number on the base of which we will find the closest number: "))

cl = array[0]

for i in array:
    if abs(x - i) < abs(x - cl):
        cl = i

print(f"The closest number to {x} in your array is {cl}")
