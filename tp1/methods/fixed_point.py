from sys import maxsize


def fixed_point(f, pn, toll=0.0, max_iter=maxsize, psy=lambda _: 1):
    def g(x): return x - psy(x) * f(x)

    ps = []
    for n in range(0, max_iter):
        fpn = f(pn)
        ps.append((n, pn, fpn))
        if abs(fpn) <= toll:
            break

        pn = g(pn)

    return ps


if __name__ == "__main__":
    from math import sin

    # sacado del ej. 4 de la guia 2.
    def f(x):
        return (x ** 2) / 4 - sin(x)

    print("[Success]")
    table = fixed_point(f, 1.75, 10e-6)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return 0.99999999999999999 * x

    print("[Failure]")
    table = fixed_point(f, 20)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")
    print(table)
