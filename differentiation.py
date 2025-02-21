def back_diff(f, x, h):
    return (f(x) - f(x - h)) / h


def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h


def centered_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def richardson(f, x, n, h=0.001):
    dp = [centered_diff(f, x, 0.5**i * h) for i in range(n)]

    for k in range(1, n):
        for i in range(n - 1, k - 1, -1):
            dp[i] = (4**k * dp[i - 1] - dp[i]) / (4**k - 1)

    return dp[-1]
