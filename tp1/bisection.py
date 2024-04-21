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
            raise ValueError("Panic: f(x) has no sign")

        pn1 = pn

    return ps
