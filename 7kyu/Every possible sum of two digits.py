def digits(num):
    num = list(str(num))
    res = []
    for i in range(0, len(num) - 1):
        for j in range(i + 1, len(num)):
            res.append(int(num[i]) + int(num[j]))
    return res