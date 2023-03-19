print('write the number of coins then write their state - 1 for heads and 0 for tails.')
n = int(input())
heads, tails = 0, 0
for i in range(n):
    f = int(input())
    heads += f == 0
    tails += f == 1
print('minimum number of flips is', min(tails, heads))

