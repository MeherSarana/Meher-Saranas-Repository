t=int(input())
while t>0:
    n=int(input())
    A=list(map(int,input().split()))
    a=min(A)
    c=0
    for i in A:
        if i%a!=0:
            c=1 
            break
    if c == 1:
        print(n)
    else:        
        print(n-A.count(a))
    t-=1
