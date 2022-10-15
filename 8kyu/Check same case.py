def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        return 1 if (a.islower() and b.islower()) or (a.isupper() and b.isupper()) else 0
    return -1