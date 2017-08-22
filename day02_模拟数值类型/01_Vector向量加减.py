'''
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1+v2
print(v3) -->Vector(4,5)

v = Vector(3, 4)
print(abs(v)) -->5.0

v*3
print(v) -->Vector(9, 12)
'''


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __str__(self):
        return 'str_Vector(%s, %s)' % (self.x, self.y)

    def __repr__(self):
        return 'repr_Vector(%s, %s)' % (self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x*other, self.y)
        elif isinstance(other, Vector):
            return Vector(self.x*other.x, self.y*other.y)

if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(2, 3)
    v3 = v1*v2
