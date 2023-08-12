n = input()
a = n.split()
cnt = 0
s = 'aeiou'
for i in a:
    i = i.lower()
    b = i[0]
    c = i[-1]
    if b in s and c not in s:
        cnt = cnt+1
print(cnt)