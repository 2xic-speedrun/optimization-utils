
def trapezoidal(f, a, b, n=1_000):
    dx = (b - a) / n
    results = 0
    for i in range(0, n):
        x_k = dx * i
        if i > 0 and (i + 1) < n:
            results += 2 * f(x_k)
        else:
            results += f(x_k)
    return dx/2 * results
