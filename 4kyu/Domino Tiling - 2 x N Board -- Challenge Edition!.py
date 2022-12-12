# https://www.codewars.com/kata/5c1905cc16537c7782000783


import numpy as np


def two_by_n(n, k):
    if k == 1:
        return int(n == 1)
    if n == 1:
        return k
    v, m = np.array([[1, 1]]), np.asmatrix(np.zeros((2, 2), dtype=Modular))
    m[0, 0] = Modular((k - 1) ** 2)
    m[0, 1] = Modular((k-1) ** 2)
    m[1, 0] = Modular(-(k-1)*(k-2))
    m[1, 1] = Modular(-(k-1)*(k-2)-1)
    res = (m ** (n-2))
    return (k * (v * (res * m))[0, 0] + k * (k-1) * (v * res)[0, 1]).number


class Modular:
    def __init__(self, number=0):
        self.number = number % 12345787

    def __add__(self, other):
        return Modular(self.number + other.number) if isinstance(other, Modular) else Modular(self.number + int(other))

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return Modular(self.number * other.number) if isinstance(other, Modular) else Modular(self.number * int(other))

    def __rmul__(self, other):
        return self.__mul__(other)
