cnt = 0
temp = 0
arr = []
for i in range(12, 12345):
    odd = 0
    even = 0
    temp = i
    while i != 0:
        if (i % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        i = i // 10
    if even % 2 != 0 and odd % 2 == 0:
        cnt += 1



x = 12
y = 12345
cnt = 0
i = x

while i <= y:
    dig = (int(math.log10(i)) + 1)
    temp = pow(10, dig)
    if dig % 2 == 0:
        i = temp
    elif temp <= y:
        cnt += math.ceil((temp - i) / 2)
        i = temp
    else:
        cnt += math.ceil((y - i) / 2)
        i = temp
