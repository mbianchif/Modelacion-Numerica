from fixed_point import fixed_point


def newton_raphson_modified(f, df, d2f, pn, toll=0, max_iter=1000):
    return fixed_point(f, pn, toll, max_iter, lambda x: df(x) / (df(x) ** 2 - f(x) * d2f(x)))
