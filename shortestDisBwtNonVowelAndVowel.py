s = input()
arr = [100000]*len(s)
'''
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        arr[i] = 0
        for j in range(len(s)):
            if s[j] != 'a' and s[j] != 'e' and s[j] != 'i' and s[j] != 'o' and s[j] != 'u':
                arr[j] = min(arr[j], abs(j-i))

print(arr)
'''

vol_ind = -1
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        arr[i] = 0
        vol_ind = i
    else:
        if vol_ind != -1:
            arr[i] = abs(i - vol_ind)
        else:
            arr[i] = 100000

print(arr)
for i in range(len(s)-1, -1, -1):
    if arr[i] == 0:
        vol_ind = i
    else:
        arr[i] = min(abs(i - vol_ind), arr[i])

print(arr)
