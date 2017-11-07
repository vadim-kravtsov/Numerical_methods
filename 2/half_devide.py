import math

def half_devide_method(f, a = -100.0, b = 100.0, e = 0.000000000001):
    x = (a + b) / 2
    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2