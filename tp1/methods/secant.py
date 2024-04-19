from methods.utils import log_root


def secant(f, pn0, pn1, toll=0, max_iter=1000):
    def g(pn0, pn1):
        return pn0 - f(pn0) * (pn0 - pn1) / (f(pn0) - f(pn1))

    ps = []
    for _ in range(max_iter):
        if f(pn0) == f(pn1):
            raise ValueError()

        gpn = g(pn0, pn1)
        ps.append((gpn, f(gpn)))
        if abs(gpn - pn0) <= toll:
            break

        pn1 = pn0
        pn0 = gpn

    return ps


def secant_test():
    from math import sin

    # sacado del ej. 16 de la guia 2.
    def f(x):
        return (x ** 2) / 4 - sin(x)

    print("[Success]")
    table = secant(f, 1.5, 2, 10e-6)
    log_root(table)

    from sys import float_info

    def f(x):
        return -(x ** 3) + 3 * x ** 2

    print("[Failure]")
    table = secant(f, -1, 2 - float_info.epsilon)
    log_root(table)
