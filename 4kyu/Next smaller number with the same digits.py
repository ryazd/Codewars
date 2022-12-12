# https://www.codewars.com/kata/5659c6d896bc135c4c00021e

def next_smaller(n):
    print(n)
    a = list(str(n))
    b = len(a)
    if b == 1:
        return -1
    for j in range(b-2,-1,-1):
        if a[j] > a[j+1]:
            t = a[j:]
            m = max(filter(lambda x: x < t[0], t))
            t.remove(m)
            c = []
            while len(t) > 0:
                d = max(t)
                c.append(d)
                t.remove(d)
            a[j:] = [m]+c
            if a[0] == '0':
                return -1
            return int(''.join(a))
    return -1