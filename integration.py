
def trap(f, a, b, n):
    h = (b - a) / n

    mid = sum(map(lambda k: f(a + k * h), range(1, n)))
    return 0.5 * h * (f(a) + mid + f(b))


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


def romberg(f, a, b, extrapolations=5):
    partials = {}

    def h(i):
        return (b - a) * 0.5 ** (i - 1)

    def R(i, j):
        if prev := partials.get((i, j)):
            return prev

        elif i == 1 and j == 1:
            val = 0.5 * (b - a) * (f(a) + f(b))
            partials[(i, j)] = val
            return val

        elif j == 1:
            h_1 = h(i - 1)

            alpha = 0
            for k in range(1, 2 ** (i - 2) + 1):
                alpha += f(a + 0.5 * (2 * k - 1) * h_1)

            val = 0.5 * (R(i - 1, 1) + h_1 * alpha)
            partials[(i, j)] = val
            return val

        else:
            val = (4 ** (j - 1) * R(i, j - 1) -
                   R(i - 1, j - 1)) / (4 ** (j - 1) - 1)
            partials[(i, j)] = val
            return val

    return R(extrapolations, extrapolations)
