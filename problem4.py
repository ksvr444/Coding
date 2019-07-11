
x=list(map(int, input().split()))

m=min(x)
if m<2:
    m=0
    while m+1 in x:
        m+=1
    print(m+1)
else:
    print(m-1)
            
        
