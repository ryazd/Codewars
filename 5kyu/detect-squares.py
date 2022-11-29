# https://leetcode.com/problems/detect-squares/


class DetectSquares:

    def __init__(self):
        self.pc = {}
        self.points = []

    def add(self, point) -> None:
        self.pc[tuple(point)] = 1 + self.pc.get(tuple(point), 0)
        self.points.append(point)

    def count(self, point) -> int:
        px, py = point
        res = 0

        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            res += self.pc.get((px, y), 0) * self.pc.get((x, py), 0)
        return res
