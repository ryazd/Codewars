# https://www.codewars.com//kata/5a6663e9fd56cb5ab800008b

def human_years_cat_years_dog_years(human_years):
    cat = 15
    dog = 15
    if human_years > 1:
        cat += 9
        dog += 9
    for i in range(2, human_years):
        cat += 4
        dog += 5
    return [human_years, cat, dog]


