#Задание №4 Дано две строки. Определить являются ли они анаграммами "автор" "товар"
#первый вариант решения
s1 = 'автор'
s2 = 'товар'

c = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            c += 1
if c == 5:
    print('слова "автор" и "товар" являются анаграммами')
else:
    print('слова "автор" и "товар" не являются анаграммами')

#второй вариант решения

k = 0
for i in s2:
    if i in s1:
        k += 1
if k == len(s1):
    print('слова "автор" и "товар" являются анаграммами')
else:
    print('слова "автор" и "товар" не являются анаграммами')
