# cook your dish here
t=int(input())
while t>0:
    t-=1 
    x,y=map(int,input().split())
    print(x//y+x%y)
