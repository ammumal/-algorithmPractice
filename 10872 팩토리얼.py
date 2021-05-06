n = int(input())

def recursion (n) :
    fac = 1
    if n == 1:
        return 1
    else:
        return n * recursion(n-1)

print(recursion(n))
