n=int(input())
arr=list(map(int,input().split()))
s=[]
for i in arr:
    if i%2!=0:
        s.append(i)
print(s[-1])        
        
        