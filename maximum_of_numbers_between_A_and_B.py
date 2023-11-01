n=int(input())
ar=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in range(n):
    if ar[i] >= a and ar[i] <= b:
        s.append(ar[i])
if len(s) == 0:
    print(-1)
else:
    print(max(s))