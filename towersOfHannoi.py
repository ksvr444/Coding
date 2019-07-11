cnt = 0
def hannoi (n, sou, aux, dest):
    global cnt
    if n == 1:
        cnt += 1
        print("move disk 1 from",sou,"to",dest)
    else:
        hannoi(n - 1, sou, dest, aux)
        print("move disk",n,"from",sou,"to",dest)
        cnt += 1
        hannoi(n-1, aux, sou, dest)
    return cnt

n = int(input("enter the no of disks"))
print("the total no of moves are", hannoi(n, 'S', 'A', 'D'))
