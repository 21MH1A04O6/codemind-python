n = input()
l1 = n.split()
l = l1[-1]
b = min(l)
c = b.lower()
if c in n:
    print(c)
else:
    print(b)