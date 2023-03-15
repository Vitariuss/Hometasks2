print('write the size of the bar and the number of squares one by one')
n = int(input())
m = int(input())
k = int(input())

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('yes, you can')
else:
    print('no, you cannot do it')