def valid_scores(scores):
    if not (5 <= scores[0] <= 100 and scores[0] % 5 == 0):
        return False
    if len(scores) == 2:
        if not (5 <= scores[1] <= 100 and scores[1] % 5 == 0):
            return False
    return True


def winner(candidates):
    if len(candidates) != 3:
        return False
    c = []
    for i in range(0, 3):
        if len(candidates[i]) != 2:
            return False
        if not (1 <= len(candidates[i]['scores']) <= 2):
            return False
        if not valid_scores(candidates[i]['scores']):
            return False
        c.append(100 - sum(candidates[i]['scores']))
    c1 = sorted(c)
    for i in range(0, 3):
        if c1[i] >= 0:
            return candidates[c.index(c1[i])]['name']
        elif i == 2:
            return False