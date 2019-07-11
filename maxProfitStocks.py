def maxProfit(arr):
    max_diff = 0
    cur_min = arr[0]
    global_min = arr[0]
    for i in range(1, len(arr)):
        if cur_min < arr[i]:
            cur_diff = arr[i] - cur_min
            if max_diff < cur_diff:
                max_diff = cur_diff
                global_min = cur_min
        else:
            cur_min = arr[i]
    return global_min

*a, = map(int, input().split())
print(maxProfit(a))

        
