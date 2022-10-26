t=int(input())
while t>0:
    t=t-1
    a,b,c=map(int,input().split())
    print(max(a,b,c)-min(a,b,c))
