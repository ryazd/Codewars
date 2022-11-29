# https://www.codewars.com//kata/5da06d425ec4c4001df69c49


from typing import List, Tuple, Set
from collections import defaultdict


def remove_internal(triangles: List[Tuple[int, int, int]]) -> Set[int]:
    table = defaultdict(int)
    for i, j, k in triangles:
        table[(min(i, j), max(i, j))] += 1
        table[(min(k, j), max(k, j))] += 1
        table[(min(i, k), max(i, k))] += 1
    return {k for i, j in table.items() for k in i if j == 1}
