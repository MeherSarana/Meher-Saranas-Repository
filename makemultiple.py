t=int(input())
while t>0 :
    t-=1 
    a,b=map(int,input().split())
    if b//a>1 or b%a==0 :
        print("YES")
    else:
        print("NO")
