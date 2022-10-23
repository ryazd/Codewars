def initials(name):
    name = name.split()
    res = ''
    for i in range(0, len(name) - 1):
        res += name[i][0].upper() + '.'
    return res + name[-1].capitalize()