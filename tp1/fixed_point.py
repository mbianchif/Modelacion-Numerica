def fixed_point(f, pn, toll=0, max_iter=1000, psy=lambda _: 1):
    def g(x): return x - psy(x) * f(x)

    ps = []
    pn1 = None
    for _ in range(max_iter):
        pn1 = pn
        pn = g(pn)
        ps.append((pn, f(pn)))
        if pn1 and abs(pn1 - pn) <= toll:
            break

    return ps
