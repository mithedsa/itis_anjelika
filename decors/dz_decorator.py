from datetime import datetime

def time_counter(func):
    def tm(q):
        start = datetime.now()
        file = open('decor.txt', 'w', encoding='utf-8')
        done = func(q)
        end = datetime.now()
        s = '\n'
        file.write(f'Вызвана в {start}{s}Завершена в {end}{s}Выполнялась {end - start} секунд')
        return done
    return tm

@time_counter
def factorial(n):
    f = 1
    l = []
    for i in range(0, n):
        f *= i + 1
        l.append(f)
    return l

factorial(60)

