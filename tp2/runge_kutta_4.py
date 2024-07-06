
def next_iter_rk4(f, g, tn, xn, yn, h):
    m1 = f(tn, xn, yn)
    k1 = g(tn, xn, yn)

    m2 = f(tn + h / 2, xn + h * m1 / 2, yn + h * k1 / 2)
    k2 = g(tn + h / 2, xn + h * m1 / 2, yn + h * k1 / 2)

    m3 = f(tn + h / 2, xn + h * m2 / 2, yn + h * k2 / 2)
    k3 = g(tn + h / 2, xn + h * m2 / 2, yn + h * k2 / 2)

    m4 = f(tn + h, xn + h * m3, yn + h * k3)
    k4 = g(tn + h, xn + h * m3, yn + h * k3)

    xn1 = xn + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
    yn1 = yn + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return xn1, yn1


def runge_kutta_4(f, g, x, y, h, a, b):
    table = [(a, x, y)]

    tn = a + h
    while tn <= b:
        xn = table[-1][1]
        yn = table[-1][2]
        xn1, yn1 = next_iter_rk4(f, g, tn, xn, yn, h)
        table.append((tn, xn1, yn1))
        tn += h

    return table
