def fac_rec(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError('n should be positive integer')
    if n == 1:
        return 1
    else:
        return n * fac_rec(n-1)
    
def fac_it(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError('n should be positive integer')
    if n == 1:
        return 1
    else:
        fac = 1
        for i in range(2, n+1):
            fac = fac * i
        return fac

n = 5
print(fac_rec(5))
print(fac_it(2))