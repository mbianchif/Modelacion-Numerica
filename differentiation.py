
def back_diff(f, x, h):
    return (f(x) - f(x - h)) / h


def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h


def centered_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def richardson(f, x, n=5):
    partials = {}

    def R(k, h):
        if prev := partials.get((k, h)):
            return prev

        elif k == 1:
            val = centered_diff(f, x, h)
            partials[(k, h)] = val
            return val

        else:
            val = (4 ** k * R(k - 1, h / 2) - R(k - 1, h)) / (4 ** k - 1)
            partials[(k, h)] = val
            return val

    return R(n, 0.01)
