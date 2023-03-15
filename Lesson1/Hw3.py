print("write your ticket number")

n = input()

s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
s3 = int(n[0]) + int(n[2]) + int(n[4])
s4 = int(n[1]) + int(n[3]) + int(n[5])

if s1 == s2 and s3 == s4:
    print('luckiest ticket ever!')
elif s1 == s2:
    print('Lucky ticket in Moscow')
elif s3 == s4:
    print('Lucky ticket in St.Petersburg')
else:
    print('Not lucky anywhere')
