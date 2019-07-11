global_val = 1000000007
def recur(arr, arr_lgth, n, ind, sum_val, temp):
    global global_val
    if ind == arr_lgth:
        return
    for i in range(n):
        recur(arr, arr_lgth, n, ind+1, sum_val + arr[ind], temp)
        temp[i] = sum_val+arr[ind]
        print(temp)
      # global_val = min(max(temp), global_val)

n = int(input("No of assinees "))
t = int(input("Time taken per unit job"))
*arr, = map(int, input().split())
temp = [0]*n
recur(arr, len(arr), n, 0, 0, temp)
print(global_val)
