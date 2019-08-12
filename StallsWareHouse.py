import itertools as it
t = int(input())
for case in range(t):
    k, n = map(int, input().split())
    *arr, = map(int, input().split())
    *cost, = map(int, input().split())
    min_val = 1000000007 * (k+1)
    # for i in range(n):
    #     ind_arr = [j for j in range(n)]
    #     ind_arr.pop(i)
    #     for val in it.combinations(ind_arr, k):
    #         sum = cost[i]
    #         for ind in val:
    #             sum += (cost[ind]) + abs(arr[i] - arr[ind])
    #         if min_val > sum:
    #             min_val = sum
    ind_arr = [j for j in range(n)]

    for val in it.combinations(ind_arr, k+1):
        for ind_hou in val:
            sum = 0
            for ind in val:
                sum += (cost[ind]) + abs(arr[ind_hou] - arr[ind])
            if min_val > sum:
                min_val = sum
    print("Case #"+str(case+1)+":", min_val)
