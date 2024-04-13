from sys import maxsize
from methods.fixed_point import fixed_point


def newton_raphson_modified(f, df, d2f, pn, toll=0, max_iter=maxsize):
    return fixed_point(f, pn, toll, max_iter, lambda x: df(x) / (df(x) ** 2 - f(x) * d2f(x)))


if __name__ == "__main__":
    # sacado del ej. 12, b de la guia 2.
    def f(x):
        return x ** 3 - 9 * (x ** 2) + 24 * x - 20

    def df(x):
        return 3 * (x ** 2) - 18 * x + 24

    def d2f(x):
        return 6 * x - 18

    print("\nNewton-Raphson-Modified")
    table = newton_raphson_modified(f, df, d2f, 1.5, 10e-4)
    for x in table:
        print(x)

    print("\nNewton-Raphson")
    from methods.newton_raphson import newton_raphson
    table = newton_raphson(f, df, 1.5, 10e-4)
    for x in table:
        print(x)
