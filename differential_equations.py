def euler(fs, x0s, a, b, n):
    dp = [(a, x0s)] + [None] * n
    h = (b - a) / n
    m = len(fs)

    for i in range(1, n + 1):
        tn1, xns = dp[i - 1]
        xn1s = [xns[j] + h * fs[j](tn1, *xns) for j in range(m)]
        dp[i] = a + i * h, xn1s

    return dp


def runge_kutta_4(fs, x0s, a, b, n):
    dp = [(a, x0s)] + [None] * n
    h = (b - a) / n

    for i in range(1, n + 1):
        tn1, xns = dp[i - 1]
        m1s = (f(tn1, *xns) for f in fs)

        x2s = [xn + 0.5 * h * m1 for xn, m1 in zip(xns, m1s)]
        m2s = (f(tn1 + 0.5 * h, *x2s) for f in fs)

        x3s = [xn + 0.5 * h * m2 for xn, m2 in zip(xns, m2s)]
        m3s = (f(tn1 + 0.5 * h, *x3s) for f in fs)

        x4s = [xn + h * m3 for xn, m3 in zip(xns, m3s)]
        m4s = (f(tn1 + h, *x4s) for f in fs)

        xn1s = [
            xn + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
            for xn, m1, m2, m3, m4 in zip(xns, m1s, m2s, m3s, m4s)
        ]

        dp[i] = a + i * h, xn1s

    return dp
