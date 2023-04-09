arr = [1, 5, 10, 15, 20, 25, 30]
min_value = int(input())
max_value = int(input())

for i in range(len(arr)):
    if min_value <= arr[i] <= max_value:
        print(i)
