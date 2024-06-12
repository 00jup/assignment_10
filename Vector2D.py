import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            if self.x == other.x and self.y == other.y:
                return True
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def distance(cls, a, b):
        try:
            return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
        except Exception as e:
            return repr(e)


class Line2D:
    def __init__(self, v1, v2):
        self.__v1 = v1
        self.__v2 = v2

    def __len__(self):
        return int(math.sqrt(math.pow(self.__v1.x - self.__v2.x, 2) + math.pow(self.__v1.y - self.__v2.y, 2)))

    def __eq__(self, other):
        if isinstance(other, Line2D):
            if self.__v1 == other.__v1 and self.__v2 == other.__v2:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f"({self.__v1.x}, {self.__v1.y}) - ({self.__v2.x}, {self.__v2.y})"


v1 = Vector2D(10, 20)
v2 = Vector2D(10, 10)
# print(f"{v1} + {v2} = {v1+v2}")
# print(f"{v1} - {v2} = {v1-v2}")
# print(f"{v1} * {v2} = {v1*v2}")
# print(f"{v1} / {v2} = {v1/v2}")
# print(f"-{v1} = {-v1}")
# print(f"{v1} == {v2} = {v1 == v2}")
# print(f"{v1} == {v1} = {v1 == v1}")
# print(f"{v1} == {10} = {v1 == 10}")

print(f"{v1}와 {v2}사이의 거리 : {Vector2D.distance(v1, v2)}")

line1 = Line2D(v1, v2)
line2 = Line2D(v2, v1)
print(line1)
print(len(line1))

print(line1 == line1)
print(line1 == line2)

print("20192294 박정욱")
