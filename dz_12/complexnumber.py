import math

class ComplexNumber:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def add(self, new):
        new_a = self.a + new.a
        new_b = self.b + new.b
        z = ComplexNumber(new_a, new_b)
        return z

    def add2(self, new):
        self.a += new.a
        self.b += new.b
        return self.a, self.b

    def sub(self, new):
        new_a = self.a - new.a
        new_b = self.b - new.b
        z = ComplexNumber(new_a, new_b)
        return z

    def sub2(self, new):
        self.a -= new.a
        self.b -= new.b
        return self.a, self.b

    def multNumber(self, x):
        new_a = self.a * x
        new_b = self.b * x
        z = ComplexNumber(new_a, new_b)
        return z

    def multNumber2(self, x):
        self.a *= x
        self.b *= x
        return self.a, self.b

    def mult(self, new):
        new_a = self.a * new.a - self.b * new.b
        new_b = self.a * new.b + self.b * new.a
        z = ComplexNumber(new_a, new_b)
        return z

    def mult2(self, new):
        self.a = self.a * new.a - self.b * new.b
        self.b = self.a * new.b + self.b * new.a
        return self.a, self.b

    def div(self, new):
        new_a = (self.a * new.a + self.b + new.b) / (new.a**2 + new.b**2)
        new_b = (self.b * new.a - self.a * new.b) / (new.a**2 + new.b**2)
        z = ComplexNumber(new_a, new_b)
        return z

    def div2(self, new):
        self.a = (self.a * new.a + self.b + new.b) / (new.a ** 2 + new.b ** 2)
        self.b = (self.b * new.a - self.a * new.b) / (new.a ** 2 + new.b ** 2)
        return self.a, self.b

    def len(self):
        print((self.a**2 + b**2)**0.5)

    def str(self):
        print(f'{self.a} + {self.b}*i')

    def arg(self):
        print(math.degrees(math.atan((self.a) / self.b)))

    def pow(self, double):
        f = self.arg()
        k = self.len() ** double
        self.a = k * math.cos(f * double)
        self.b = k * math.sin(f * double)
        return (self.a, self.b)

    def equals(self, new):
        if self.len() > new.len():
            print('Первое число больше')
        if self.len() < new.len():
            print('Второе число больше')
        else:
            print('числа равны')
