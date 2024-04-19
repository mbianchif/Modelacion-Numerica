from methods.fixed_point import fixed_point
from methods.utils import log_root


def newton_raphson_modified(f, df, d2f, pn, toll=0, max_iter=1000):
    return fixed_point(f, pn, toll, max_iter, lambda x: df(x) / (df(x) ** 2 - f(x) * d2f(x)))


def newton_raphson_modified_test():
    # sacado del ej. 12, b de la guia 2.
    def f(x):
        return x ** 3 - 9 * (x ** 2) + 24 * x - 20

    def df(x):
        return 3 * (x ** 2) - 18 * x + 24

    def d2f(x):
        return 6 * x - 18

    print("[Success]")
    table = newton_raphson_modified(f, df, d2f, 1.5, 10e-4)
    log_root(table)

    def f(x):
        return x ** 2 - 1

    def df(x):
        return 2 * x

    def d2f(_):
        return 2

    print("[Failure]")
    table = newton_raphson_modified(f, df, d2f, 0, 10e-5)
    log_root(table)
