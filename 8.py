#Задание №8 Палиндром. Строка зеркальна за исключением пробелов и спецсимволов (запятых например).

a = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
s = ' , шалаш .      '
#s1 = s.strip()
k = ''
for i in s:
    if i in a:
        k += i
if k == k[::-1]:
    print('слово является палиндромом')
else:
    print('слово не является палиндромом')