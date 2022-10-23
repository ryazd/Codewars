def a(n):
    if n < 4:
        return ''
    if n <= 5:
        return "   A   \n  A A  \n A A A \nA     A"
    if n % 2 != 0:
        n -= 1
    vr = (n - 1) * ' '
    res = [f'{vr}A{vr}']
    for i in range(2, n + 1):
        vr = (n - i) * ' '
        spl = ((2 * i) - 3) * " "
        if i - 1 == n / 2:
            res.append(vr + " ".join(["A"] * i) + vr)
        else:
            res.append(f'{vr}A{spl}A{vr}')
    return "\n".join(res)