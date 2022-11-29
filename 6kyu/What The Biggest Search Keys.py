# https://www.codewars.com//kata/58ac1abdff4e78738f000805

def the_biggest_search_keys(*args):
    args = list(args)
    args.sort(key=len)
    if not args:
        return "''"
    lst = [x for x in args if len(x) == len(args[-1])]
    lst.sort()
    lst = ["'" + x + "'" for x in lst]
    if len(lst) > 1:
        return ", ".join(lst)
    return lst[0]
