def secant(f, pn0, pn1, toll=0, max_iter=1000):
    def g(pn0, pn1):
        return pn0 - f(pn0) * (pn0 - pn1) / (f(pn0) - f(pn1))

    ps = []
    for _ in range(max_iter):
        if f(pn0) == f(pn1):
            break

        ps.append((pn1, f(pn1)))
        gpn = g(pn0, pn1)
        if abs(gpn - pn1) <= toll:
            break

        pn1 = pn0
        pn0 = gpn

    return ps


if __name__ == "__main__":
    from math import sin, cos

    # sacado del ej. 16 de la guia 2.
    def f(x):
        return (x ** 2) / 4 - sin(x)

    print("[Success]")
    table = secant(f, 1.5, 2, 10e-6)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return x * cos(10 * x) / 20 + 1

    print("[Failure]")
    table = secant(f, -1, 2, 0)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")
