t = int(input())
for case in range(t):
    n, q = map(int, input().split())
    *arr, = map(int, input().split())
    print("Case #"+str(case+1)+":", end = " ")
    for _ in range(q):
        ind, val = map(int, input().split())
        arr[ind] = val
        xor_val = 0
        max_len = -1
        for i in range(n):
            xor_val = 0
            for j in range(i, n):
                xor_val = xor_val ^ arr[j]
                # bin_val = bin(xor_val)[2:]
                if bin(xor_val).count('1') % 2 == 0 and max_len < j-i :
                    max_len = j-i
        print(max_len + 1, end = " ")
    print()
