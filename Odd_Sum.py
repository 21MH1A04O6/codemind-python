n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in arr:
    if i%2 != 0:
        c+=i #0 1 4 9 16
print(c)