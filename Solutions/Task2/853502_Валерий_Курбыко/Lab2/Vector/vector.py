import math


class Vector:
    def __init__(self, *args):
        for dim in args:
            if not isinstance(dim, (int, float)):
                raise ValueError("Vector dimensions must be numbers!")

        self.coordinates = list(args)
        self.dimension = len(args)

    def __add__(self, other):
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Incorrect operands")

        if isinstance(other, Vector):
            if len(self) != len(other):
                raise TypeError("Different vector dimensions!")

            return Vector(*[x + y for x, y in zip(self.coordinates, other.coordinates)])

        else:
            return Vector(*[x + other for x in self.coordinates])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, (Vector, int, float)):
            raise ValueError("Incorrect operands")
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise TypeError("Different vector dimensions!")
        return self + (-other)

    def __neg__(self):
        return Vector(*[-x for x in self.coordinates])

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(*[x * other for x in self.coordinates])

        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise TypeError("Different vector dimensions!")

            return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

        else:
            raise ValueError("Incorrect operands!")

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.coordinates == other.coordinates

    def __len__(self):
        return self.dimension

    def get_norm(self):
        return math.sqrt(sum(x**2 for x in self.coordinates))

    def __getitem__(self, item):
        if item >= self.dimension:
            raise IndexError("Index out of range")
        return self.coordinates[item]

    def __setitem__(self, key, value):
        if isinstance(value, (int, float)):
            self.coordinates[key] = value
        else:
            raise ValueError("Value must be a number!")

    def __str__(self):
        return "(" + '; '.join(map(str, self.coordinates)) + ")"
