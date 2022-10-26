t=int(input())
while t>0:
    t-=1 
    n,x,y=map(int,input().split())
    if y%x*n==0:
        print("Yes")
    else:
        print("No")
