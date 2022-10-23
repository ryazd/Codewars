def my_parse_int(string):
    try:
        string = int(string)
        return string
    except:
        return 'NaN'