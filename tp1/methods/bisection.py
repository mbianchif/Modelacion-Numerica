from methods.utils import log_root


def bisection(f, a, b, toll=0, max_iter=1000):
    ps = []
    pn1 = None
    for _ in range(max_iter):
        pn = (a + b) / 2

        fpn = f(pn)
        ps.append((pn, fpn))
        if pn1 and abs(pn1 - pn) <= toll:
            break

        fa = f(a)
        if fa * fpn > 0:
            a = pn
        elif fa * fpn < 0:
            b = pn
        else:
            raise ValueError("found 0")

        pn1 = pn

    return ps


def bisection_test():
    from math import sin, cos, exp, pi

    # sacado del ej. 1 de la guia 2.
    def f(x):
        return exp(x) * (sin(x) + cos(x) - 2 * x - 2)

    print("[Success]")
    table = bisection(f, -2.5, -0.5, 10e-5)
    log_root(table)

    def f(x):
        # R = 1
        return pi * (x ** 2) * (3 - x) / 3

    print("[Failure]")
    try:
        table = bisection(f, -4, 4)
    except ValueError as v:
        print(v)
