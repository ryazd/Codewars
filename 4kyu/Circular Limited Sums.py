# https://www.codewars.com/kata/59951f21d65a27e95d00004f


def circular_limited_sums(max_n, max_fn):
    counts = {(i, i): 1 for i in range(max_fn + 1)}
    for _ in range(max_n - 1):
        counts = {
            (i, j):
            sum(counts.get((i, k), 0) for k in range(max_fn - j + 1))
            for i in range(max_fn + 1)
            for j in range(max_fn + 1)
        }
    return sum(
        counts.get((i, j), 0)
        for i in range(max_fn + 1)
        for j in range(max_fn - i + 1)
    ) % 12345787