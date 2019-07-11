fib = [-1] * (10**8)
def Nfib(n):
    global fib
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif fib[n] == -1:
        fib[n] = Nfib(n-1) + Nfib(n-2)
    return fib[n]

n = int(input())
print(Nfib(n))
print(fib[n])

