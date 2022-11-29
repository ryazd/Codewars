# https://www.codewars.com//kata/5b114e854de8651b6b000123

def who_would_win(mon1, mon2):
    hp1 = mon1['hitpoints'] * mon1['number']
    hp2 = mon2['hitpoints'] * mon2['number']
    while hp1 > 0 and hp2 > 0:
        hp2 -= mon1['damage'] * mon1['number']
        if hp2 < 0:
            return f"{mon1['number']} {mon1['type']}(s) won"
        mon2['number'] = (hp2 // mon2['hitpoints']) + (0 if hp2 % mon2['hitpoints'] == 0 else 1)
        hp1 -= mon2['damage'] * mon2['number']
        mon1['number'] = (hp1 // mon1['hitpoints']) + (0 if hp1 % mon1['hitpoints'] == 0 else 1)
    if hp1 > 0:
        return f"{mon1['number']} {mon1['type']}(s) won"
    return f"{mon2['number']} {mon2['type']}(s) won"
