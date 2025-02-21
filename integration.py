def trap(f, a, b, n):
    h = (b - a) / n

    partial_sum = sum(map(lambda k: f(a + k * h), range(1, n)))
    return 0.5 * h * (f(a) + partial_sum + f(b))


def simpson13(f, a, b, n):
    h = (b - a) / n

    odds = f(a + h)
    evens = 0
    for k in range(1, (n - 2) // 2 + 1):
        odds += f(a + (2 * k + 1) * h)
        evens += f(a + 2 * k * h)

    return (h / 3) * (f(a) + 4 * odds + 2 * evens + f(b))


def simpson38(f, a, b, n):
    h = (b - a) / n

    ones = f(a + h)
    twos = f(a + 2 * h)
    threes = 0
    for k in range(1, (n - 3) // 3 + 1):
        ones += f(a + (3 * k + 1) * h)
        twos += f(a + (3 * k + 2) * h)
        threes += f(a + 3 * k * h)

    return (3 * h / 8) * (f(a) + 3 * (ones + twos) + 2 * threes + f(b))


def romberg(f, a, b, n):
    dp = [0.5 * (b - a) * (f(a) + f(b))] + [0.0] * (n - 1)

    for i in range(1, n):
        h_i = (b - a) * 0.5 ** (i - 1)
        partial_sum = sum(
            f(a + 0.5 * (2 * k - 1) * h_i) for k in range(1, 2 ** (i - 1) + 1)
        )
        dp[i] = 0.5 * (dp[i - 1] + h_i * partial_sum)

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            dp[i] = (4 ** j * dp[i] - dp[i - 1]) / (4 ** j - 1)

    return dp[-1]
