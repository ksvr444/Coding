import math
import itertools as it

def permutate(cand, rem, cnt):
    global count
    if len(rem) == 0:
        lo = 1
        while(lo < cnt and cand[lo-1] - cand[lo] != -1):
            lo += 1
        if lo == cnt:
            count +=1
    else:
        for i in range(len(rem)):
            newCand = [rem[i]]
            newRem = list(rem[:i]) + list(rem[i+1:])
            permutate(cand+newCand, newRem, cnt)

t = int(input())
count = 0
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1, int(math.sqrt(n)) +1):
        if n % i == 0:
            if i*i == n:
                cnt += 1
            else:
                cnt += 2
    arr =[i for i in range(1, cnt+1)]
##    per = list(it.permutations(arr))
    count = 0
    permutate([], arr, cnt)
##    for val in per:
##        lo = 1
##        while(lo < cnt and val[lo-1] - val[lo] != -1):
##            lo += 1
##        if lo == cnt:
##            c +=1
    print(count)
