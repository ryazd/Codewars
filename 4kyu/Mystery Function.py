# https://www.codewars.com/kata/56b2abae51646a143400001d

def mystery(n):
    return n ^ (n >> 1)


def mystery_inv(n):
    mask = n >> 1
    while mask:
        n = n ^ mask
        mask = mask >> 1
    return n


def name_of_mystery():
    return "Gray code"