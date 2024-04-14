from sys import maxsize


def secant(f, pn0, pn1, toll=0, max_iter=maxsize):
    ps = []

    def g(pn0, pn1):
        return pn1 - (f(pn1)) * (pn1 - pn0) / (f(pn1) - f(pn0))

    for n in range(0, max_iter):
        gpn = g(pn0, pn1)
        fpn = f(gpn)
        ps.append((n, pn0, pn1, gpn))
        if abs(fpn) <= toll:
            break

        pn0 = pn1
        pn1 = gpn
    return ps


if __name__ == "__main__":
    from math import sin

    # sacado del ej. 16 de la guia 2.
    table = secant(lambda x: (x**2) / 4 - sin(x), 1.5, 2, 10e-6)
    for x in table:
        print(x)
