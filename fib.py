import functools

@functools.lru_cache(maxsize=128)
def fib_rec(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    if n== 1:
        return 0
    elif n== 2:
        return 1
    else:
        prev = 0
        curr = 1
        
        for _ in range(3, n+1):
            val = prev + curr
            prev, curr = curr, val
        return val



print(fib_rec(50))
print(fib_it(50))