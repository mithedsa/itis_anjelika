def is_prime(limit):
    num = 1
    prime = False
    while num != limit:
        for i in range(2, num+1):
            if num % i == 0:
                prime = False
                if i == num:
                    prime = True
                break
        if prime:
            yield num
            num += 1
        else:
            num += 1

prime = is_prime(12)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))