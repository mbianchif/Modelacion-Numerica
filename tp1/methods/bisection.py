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
            raise ValueError()

        pn1 = pn

    return ps


if __name__ == "__main__":
    from math import sin, cos, exp, pi

    # sacado del ej. 1 de la guia 2.
    def f(x):
        return exp(x) * (sin(x) + cos(x) - 2 * x - 2)

    print("[Success]")
    table = bisection(f, -2.5, -0.5, 10e-5)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        # R = 1
        return pi * (x ** 2) * (3 - x) / 3

    print("[Failure]")
    bisection(f, -4, 4)
