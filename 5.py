n = 123456
s = list(str(n))
l = []
for i in s:
    if int(i) % 2 != 0:
        l.append(i)
print(int(''.join(l)))