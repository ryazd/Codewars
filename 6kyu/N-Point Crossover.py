def crossover(ns, xs, ys):
    ns = list(set(ns))
    for n in ns:
        xs, ys = xs[:n] + ys[n:], ys[:n] + xs[n:]
    return (xs, ys)