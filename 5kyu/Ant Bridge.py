# https://www.codewars.com//kata/599385ae6ca73b71b8000038

def ant_bridge(ants, terrain):
    bridge = []
    ants = list(ants)
    i = 0
    while i < len(terrain) - 1:
        if terrain[i] == '-' and terrain[i + 1] == '.':
            bridge.append(ants.pop())
            i += 1
        while terrain[i] == '.':
            bridge.append(ants.pop())
            i += 1
        if terrain[i] == '-' and terrain[i - 1] == '.':
            bridge.append(ants.pop())
        while len(bridge) > 0:
            ants = [bridge.pop(0)] + ants
        i += 1
    return ''.join(ants)
