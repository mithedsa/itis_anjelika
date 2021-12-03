n = 1345726
n = list(str(n))
n.sort()
с = 0
for i in range(len(n)):
    if int(n[i])%2 == 0:
        с += int(n[i])
    else:
        с -= int(n[i])
print(abs(с))
