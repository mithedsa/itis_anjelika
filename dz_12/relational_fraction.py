class RelationalFraction:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def reduce(self):
        if self.x > self.y:
            divis = self.x
        else:
            divis = self.y
        while divis != 1:
            if self.x % divis == 0 and self.y % divis == 0:
                return self.x // divis, self.y // divis
            else:
                divis -= 1
        return self.x, self.y

    def add(self, new):
        new_x = self.x * new.y + new.x * self.y
        new_y = self.y * new.y
        z = RelationalFraction(new_x, new_y)
        return z.reduce()

    def add2(self, new):
        self.x = self.x * new.y + new.x * self.y
        self.y = self.y * new.y
        return (self.x, self.y)

    def sub(self, new):
        new_x = self.x * new.y - new.x * self.y
        new_y = self.y * new.y
        z = RelationalFraction(new_x, new_y)
        return z.reduce()

    def sub2(self):
        self.x = self.x * new.y - new.x * self.y
        self.y = self.y * new.y
        return (self.x, self.y)

    def mult(self, new):
        new_x = self.x * new.x
        new_y = self.y * new.y
        z = RelationalFraction(new_x, new_y)
        return z.reduce()

    def mult2(self, new):
        self.x = self.x * new.x
        self.y = self.y * new.y
        return (self.x, self.y)

    def div(self, new):
        new_x = self.x * new.y
        new_y = self.y * new.x
        z = RelationalFraction(new_x, new_y)
        return z.reduce()

    def div2(self, new):
        self.x *= new.y
        self.y *= new.x
        return (self.x, self.y)

    def str(self):
        print(f'{self.x}/{self.y}')

    def value(self):
        print(self.x/self.y)

    def equals(self, new):
        if self.x / self.y > new.x / new.y:
            print('первая дробь больше')
        elif self.x / self.y < new.x / new.y:
            print('вторая дробь больше')
        else:
            print('дроби равны')

    def numberPart(self):
        print(int(self.x/self.y))
