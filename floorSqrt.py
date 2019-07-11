def squareRoot(n, low, high):
    mid = (low + high)//2
    if mid*mid <= n and (mid+1)*(mid+1) > n:
        return mid
    elif mid * mid > n:
        return squareRoot(n, low, mid-1)
    else:
        return squareRoot(n, mid+1, high)

n = int(input())
print(squareRoot(n, 1, n))
