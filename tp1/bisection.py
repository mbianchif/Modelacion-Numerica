def bisection(f, a, b, toll=0, max_iter=1000):
    pn_1 = None
    ps = []

    for _ in range(max_iter):
        pn = (a + b) / 2

        fx = f(pn)
        ps.append((pn, fx))
        if pn_1 and abs(pn_1 - pn) <= toll:
            break

        fa_fx = fx * f(a)
        if fa_fx > 0:
            a = pn
        elif fa_fx < 0:
            b = pn
        else:
            raise ValueError("f(pn) has no sign")

        pn_1 = pn

    return ps
