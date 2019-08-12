n = int(input())

i2 = 0
i3 = 0
i5 = 0
arr = [0] * (n+1)
arr[0] = 1
next_i2 = 2
next_i3 = 3
next_i5 = 5
for i in range(1, n+1):
    next = min(next_i2, next_i3, next_i5)
    arr[i] = next
    if next == next_i2:
        i2 += 1
        next_i2 = arr[i2] * 2
    if next == next_i3:
        i3 += 1
        next_i3 = arr[i3] * 3
    if next == next_i5:
        i5 += 1
        next_i5 = arr[i5] * 5

print(arr[n])
