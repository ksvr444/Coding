*arr, = map(int, input("enter the elements of list").split())

end = int('0b' + '1' * (len(arr)), 2);
for i in range(1, end+1):
    temp = []
    ind = -1
    while i != 0 :
        if i & 1 == 1:
            temp = [arr[ind]] + temp
        ind -= 1
        i = i >> 1
    print(temp)
