n=int(input())
a=0
b=1
for _ in range(n-2):
    c=a+b
    if c==n:
        print("True")
        break
    a=b
    b=c
if c>n:
    print("False")