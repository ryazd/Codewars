def reverse_by_center(s):
    if len(s) % 2 == 0:
        return s[len(s)//2:] + s[0:len(s)//2]
    else:
        return s[len(s)//2+1:] + s[len(s)//2] + s[0:len(s)//2]