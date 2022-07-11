import math

class Vector2D:

    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return NotImplementedError

        self.x, self.y = x, y

    def __str__(self):
        return 'Vector ({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return repr((self.x, self.y))

    def dot(self, other):

        if not isinstance(other, Vector2D):
            raise TypeError('Can only take dot product of two Vector2D objects')
        return self.x * other.x + self.y * other.y

    # Creating an alias for 'dot' to be able to use @ b as well as a.dot(b)
    __matmul__ = dot

    def __sub__(self, other):
        # Vector Subtraction
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        # Vector Addition
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # Multiplication of a vector by a scalar
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector2D(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multipy Vector2D by a scalar')

    def __rmul__(self, scalar):
        # Reflected multiplication so vector * scalar also works.
        return self.__mul__(scalar)

    def __neg__(self):
        # Negation of the vector (invert through origin)
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, scalar):
        # True division of the vector by a scalar
        return Vector2D(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):
        # Implementation of modulus operation for each component
        return Vector2D(self.x % scalar, self.y % scalar)

    def __abs__(self):
        # Absolute value (magnitude) of the vector
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        # Distance between vectors self and other
        return abs(self - other)

    def to_polar(self):
        # Vector's coordinates in polar coordinates
        return self.__abs__(), math.atan2(self.y, self.x)
