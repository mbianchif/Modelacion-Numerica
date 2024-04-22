def secant(f, p0, p1, toll=0, max_iter=1000):
    prev, curr = p0, p1
    ps = []

    def g(x1, x2):
        return x1 - f(x1) * (x1 - x2) / (f(x1) - f(x2))

    for _ in range(max_iter):
        ps.append((curr, f(curr)))

        post = g(curr, prev)
        if abs(post - curr) <= toll:
            break

        prev = curr
        curr = post

    return ps
