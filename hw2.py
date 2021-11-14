# №3 Сложить два списка поэлементно и вернуть новый список
ls1 = [1, 3, 5, 7, 9]
ls2 = [2, 4, 6, 8]
if len(ls1) > len(ls2):
    while len(ls2) != len(ls1):
        ls2.append('none')
else:
    while len(ls1) != len(ls2):
        ls1.append('none')
ls3 = []
for i in range(len(ls1)):
    ls3.append(ls1[i])
    ls3.append(ls2[i])
while 'none' in ls3:
    ls3.remove('none')
print(ls3)

# №4 Поменять два элемента местами (по ссылкам)
def switch(list, node1, node2):
    list[node1], list[node2] = list[node2], list[node1]
    return list
print(switch([2, 3, 4, 5], 0, 3))

# №5 Получить значение элемента по номеру его позиции
def get_by_index(list, position):
    for i in range(len(list)):
        if position == i:
            return list[i]
a = [2, 5, 8, 20, 100]
print(get_by_index(a, 3))

# №6 Измерить длину списка
def list_len(list):
    return len(list)
b = [2, 5, 8]
print(list_len(b))