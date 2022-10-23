def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1

    i = 0
    val = 1
    while True:
        i += 1
        val = val * 10 % n
        if (val == 1):
            return i