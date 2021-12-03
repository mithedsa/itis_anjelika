ind = [1, 2, 3, 4, 5]
p = [2, 3, 5, 4, 1]
q = [5, 4, 3, 2, 1]
a = []
for i in range(len(p)):
    for j in range(len(q)):
        if p[i] == q[j]:
            a.insert(i, q[j])
print(ind, a)