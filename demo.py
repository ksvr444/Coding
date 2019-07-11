def fun(i, temp):
    if i == 5:
        return
    temp.append(i)
    fun(i+1, temp)
    print(temp)

temp = []
fun(0, temp)
print()
temp.append(5)
print(temp)
