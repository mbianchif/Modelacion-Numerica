def fixed_point(f, pn, toll=0, max_iter=1000, psy=lambda _: 1):
    def g(x): return x - psy(x) * f(x)

    ps = []
    pn1 = None
    for _ in range(max_iter):
        ps.append((pn, f(pn)))
        if pn1 and abs(pn1 - pn) <= toll:
            break

        pn = g(pn)
        pn1 = pn

    return ps


if __name__ == "__main__":
    from math import sin

    # sacado del ej. 4 de la guia 2.
    def f(x):
        return (x ** 2) / 4 - sin(x)

    print("[Success]")
    table = fixed_point(f, 1.75, 10e-6)
    print(f"found x = {table[-1][0]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return 0

    print("[Failure]")
    table = fixed_point(f, 20)
    print(f"found x = {table[-1][0]} with f(x) = {f(table[-1][1])}")
