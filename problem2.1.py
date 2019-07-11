def pro(x):
    pre_list=[]
    post_list=[]
    for i in x:
        if not pre_list:
            pre_list.append(i)
        else:
            pre_list.append(pre_list[-1] * i)

    for i in reversed(x):
        if not post_list:
            post_list.append(i)
        else:
            post_list.append(post_list[-1] * i)

    post_list.sort(reverse=True)

    return pre_list,post_list


x=list(map(int,input().split()))
pre_list, post_list = pro(x)
res=[]
for i in range(len(x)):
    if i==0:
        res.append(post_list[i+1])
    elif i==len(x)-1:
        res.append(pre_list[i-1])
    else:
        res.append(pre_list[i-1] * post_list[i+1])

print(res)
