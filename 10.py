n = int(input('введите количество цифр'))
print('введите столько чисел')
l = []
for _ in range(n):
    q = input()
    l.append(q)
c = 0
num = []
for i in l:
    if len(i) == 3 or len(i) == 5:
        for j in range(len(i)):
            chet = 0
            nechet = 0
            if int(i[j]) % 2 != 0:
                chet += 1
            else:
                nechet += 1
            if len(i) == chet or len(i) == nechet:
                c += 1
                num.append(i)
if c == 2:
     print(num)