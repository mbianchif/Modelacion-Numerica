def secant(f, pn0, pn1, toll=0, max_iter=1000):
    def g(pn0, pn1):
        return pn0 - f(pn0) * (pn0 - pn1) / (f(pn0) - f(pn1))

    ps = []
    for _ in range(max_iter):
        try:
            gpn = g(pn0, pn1)
        except ZeroDivisionError:
            raise ValueError("f(pn) - f(pn-1) = 0")

        ps.append((gpn, f(gpn)))
        if abs(gpn - pn0) <= toll:
            break

        pn1 = pn0
        pn0 = gpn

    return ps


if __name__ == "__main__":
    from sys import float_info

    def f(x):
        return -x ** 3 + 3 * x ** 2

    print("[Failure]")
    table = secant(f, -1, 2 - float_info.epsilon)
    print(table)
