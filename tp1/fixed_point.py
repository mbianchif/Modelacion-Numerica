def fixed_point(f, pn, toll=0, max_iter=1000, psy=lambda _: 1):
    pn_1 = None
    ps = []

    def g(xn):
        return xn - psy(xn) * f(xn)

    for _ in range(max_iter):
        ps.append((pn, f(pn)))
        if pn_1 and abs(pn_1 - pn) <= toll:
            break

        pn_1 = pn
        pn = g(pn)

    return ps
