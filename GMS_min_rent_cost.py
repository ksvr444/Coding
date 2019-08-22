m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

min_val = 99999999
for i in range(m):
    for j in range(n):
        sum_val = arr[i][j]
        temp_min = arr[i][j]

        for k in range(i-1, -1, -1):
            sum_val = sum_val + arr[k][j]
            temp_min = min(temp_min, sum_val)

        sum_val = temp_min
        for k in range(j-1, -1, -1):
            sum_val = sum_val + arr[i][k]
            temp_min = min(temp_min, sum_val)

        sum_val = temp_min
        for k in range(i+1, m, 1):
            sum_val = sum_val + arr[k][j]
            temp_min = min(temp_min, sum_val)

        sum_val = temp_min
        for k in range(j+1, n, 1):
            sum_val = sum_val + arr[i][k]
            temp_min = min(temp_min, sum_val)
        min_val = min(min_val, temp_min)

print(min_val)
