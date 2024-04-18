from sys import maxsize


def secant(f, pn0, pn1, toll=0, max_iter=maxsize):
    def g(pn0, pn1):
        return pn1 - (f(pn1)) * (pn1 - pn0) / (f(pn1) - f(pn0))

    ps = [(0, pn0, f(pn0))]
    for n in range(1, max_iter):
        gpn = g(pn0, pn1)
        fpn = f(gpn)
        ps.append((n, pn1, gpn))
        if abs(fpn) <= toll:
            break

        pn0 = pn1
        pn1 = gpn

    return ps


if __name__ == "__main__":
    from math import sin

    # sacado del ej. 16 de la guia 2.
    def f(x):
        return (x ** 2) / 4 - sin(x)

    print("[Success]")
    table = secant(f, 1.5, 2, 10e-6)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return 0

    print("[Failure]")
    table = secant(f, 0, 1, 2)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")
