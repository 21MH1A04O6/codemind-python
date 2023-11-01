n=int(input())
ar=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    if ar[i] >= a and ar[i] <= b:
        s += ar[i]
print(s)