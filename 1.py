import gmpy2

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return gmpy2.ackermann(m-1, gmpy2.ackermann(m, n-1))

print(ackermann(4, 2))
