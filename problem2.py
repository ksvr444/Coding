x=list(map(int,input().split()))
sum=1
b=[]
for i in x:
    sum*=i
for i in x:
    b.append(sum//i)
print(b)
