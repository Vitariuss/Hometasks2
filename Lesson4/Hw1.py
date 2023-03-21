n = int(input("How many elements are there in the first array? "))
m = int(input("How many elements are there in the second array? "))

set1 = set()
set2 = set()

for i in range(n):
    e = int(input(f"Write the element # {i+1} in the first array: "))
    set1.add(e)

for i in range(m):
    e = int(input(f"Write the element # {i+1} in the second array: "))
    set2.add(e)

i = sorted(list(set1.intersection(set2)))

print("Элементы, которые встречаются в обоих множествах:", i)