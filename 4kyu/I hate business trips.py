# https://www.codewars.com/kata/5e9c8a54ae2b040018f68dd9

from typing import List


def fit_bag(height: int, width: int, items: List[List[List[int]]]) -> List[List[int]]:
    def to_coord(item):
        r = []
        for y, line in enumerate(item):
            for x, c in enumerate(line):
                if c != 0:
                    r.append((x, y))
                    n = c
        return n, len(item), len(item[0]), r

    items = sorted(map(to_coord, items), key=lambda x: len(x[3]))
    res = [[0 for _ in range(width)] for _ in range(height)]

    def dfs(items, res):
        if not items:
            return

        n, h, w, item = items.pop()

        for y in range(height - h + 1):
            for x in range(width - w + 1):
                if all(res[y + j][x + i] == 0 for i, j in item):

                    for i, j in item:
                        res[y + j][x + i] = n

                    dfs(items, res)
                    if not items:
                        return

                    for i, j in item:
                        res[y + j][x + i] = 0

        items.append((n, h, w, item))

    dfs(items, res)
    return res