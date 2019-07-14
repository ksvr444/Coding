s = input("enter a string")
max_pal = ''
max_lgth = 0
for i in range(len(s)):
    for j in range(i+2, len(s)+1):
        temp = s[i : j] m
        lgth = len(temp)
        if temp == ''.join(reversed(temp)) and max_lgth < lgth:
            max_pal = temp
            max_lgth = lgth

print(max_pal)
