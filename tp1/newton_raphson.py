from fixed_point import fixed_point


def newton_raphson(f, df, pn, toll=0, max_iter=1000):
    return fixed_point(f, pn, toll, max_iter, lambda x: 1 / df(x))
