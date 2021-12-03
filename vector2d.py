class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def add(self, new):
        new_x = self.x + new.x
        new_y = self.y + new.y
        z = Vector2D(new_x, new_y)
        print('это новый объект', z.x, z.y)

    def add2(self, new):
        self.x += new.x
        self.y += new.y
        return self.x, self.y

    def sub(self, new):
        new_x = self.x - new.x
        new_y = self.y - new.y
        z = Vector2D(new_x, new_y)
        print('это новый объект', z.x, z.y)

    def sub2(self):
        self.x -= new.x
        self.y -= new.y
        return self.x, self.y

    def mult(self, a):
        new_x = a * self.x
        new_y = a * self.y
        z = Vector2D(new_x, new_y)
        print('это новый объект', z.x, z.y)

    def mult2(self, a):
        self.x *= self.x
        self.y *= self.y
        return self.x, self.y

    def str(self):
        print(self.x, self.y)

    def len(self):
        print((self.x**2 + self.y**2)**0.5)

    def scalarProduct(self, new):
        new_x = self.x * new.x
        new_y = self.y * new.y
        print(new_x + new_y)

    def cos(self, new):
        print(((self.x * new.x + self.y * new.y) / ((self.x**2 + self.y**2)/2))**0.5 * (new.x**2 + new.y**2)**0.5)

    def equals(self, new):
        if self.len() > new.len():
            print(self, '>', new)
        elif self.len() < new.len():
            print(self, '<', new)
        else:
            print('вектора равны')