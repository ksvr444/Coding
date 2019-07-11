x = int(input())
a = [i for i in range(x + 1)]
for i in range(1, x+1):
    if i - 10 >= 0:
        a[i] = min(a[i], 1 + a[i - 10])
    if i - 7 >= 0:
        a[i] = min(a[i], 1 + a[i - 7])
    if i - 5 >= 0:
        a[i] = min(a[i], 1 + a[i - 5])
    if i - 1 >= 0:
        a[i] = min(a[i], 1 + a[i - 1])

    print(i,a[i])


'''

def count_change(amount, coins):
    #start writing your code here
    arr = [0 for i in range(amount+1)]
    for j in range(amount+1):
        for i in range(len(coins)):
            if j >= coins[i]:
                arr[j] = min(arr[j], 1+arr[j-coins[i]])
    return arr[amount]

print(count_change(5, [10, 7, 5, 1]))


'''
