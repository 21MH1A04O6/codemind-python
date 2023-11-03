def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
m = int(input())
s=0
for i in range(1,m+1):
    if m%i == 0 and not fun(i):
        s+=1
print(s)        
        