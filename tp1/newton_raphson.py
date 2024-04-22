from fixed_point import fixed_point


def newton_raphson(f, df, pn, toll=0, max_iter=1000):
    def psy(xn):
        return 1 / df(xn)

    return fixed_point(f, pn, toll, max_iter, psy)
