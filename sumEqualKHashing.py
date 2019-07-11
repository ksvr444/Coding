n = int(input("enter the length of array "))
*arr, = map(int, input().split())
sum = int(input("enter the sum value "))
c = 0
d={}
for val in arr:
    d[val] = sum - val

for val in d:
    try:
        if val == d[d[val]]:
            c += 1
    except:
        d[val] = 'not included'
print(c//2)
