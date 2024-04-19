from methods.fixed_point import fixed_point
from methods.utils import log_root


def newton_raphson(f, df, pn, toll=0, max_iter=1000):
    return fixed_point(f, pn, toll, max_iter, lambda x: 1 / df(x))


def newton_raphson_test():
    # sacado del ej. 12 de la guia 2.
    def f(x):
        return (x ** 3) - 9 * (x ** 2) + 24 * x - 20

    def df(x):
        return 3 * (x ** 2) - 18 * x + 24

    print("[Success]")
    table = newton_raphson(f, df, 1.5, 0)
    log_root(table)

    from sys import float_info

    def f(x):
        return 2 * x ** 3 - 15 * x ** 2 + 109

    def df(x):
        return 6 * x ** 2 - 30 * x

    print("[Failure]")
    table = newton_raphson(f, df, float_info.epsilon)
    log_root(table)

    # Este es un caso de falla porque habiendo elegido el intervalo (0, 5)
    # donde no se anula la derivada y la función es continua, la raíz encontrada
    # está por fuera del intervalo.
