t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if s[:n//2]==s[n//2:]:
        print('YES')
    else:
        print("NO")
