# https://www.codewars.com//kata/5a99d851fd5777f746000066

import math


def distance(c1, c2):
    l = []
    for a in c1:
        for b in c2:
            l.append(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))
    return sum(l)/len(l)


def minimum_distance(tab):
    if (not tab) or len(tab) < 2:
        return None
    else:
        mind = -1
        for i in range(0,len(tab)):
            for j in range(i+1,len(tab)):
                d = distance(tab[i],tab[j])
                if mind == -1 or d < mind:
                    mind = d
                    minc = (i, j)
        return minc


def cluster(points, n):
    points = [[p] for p in sorted(points)]
    while n < len(points):
        (i, j) = minimum_distance(points)
        points[i].extend(points[j])
        points[i].sort()
        points.pop(j)
    return points
