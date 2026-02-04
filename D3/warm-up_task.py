import math

def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

a = -3
b = 2
eps = 0.0001
step = 0.1

roots = []

def bisection(a, b, eps):
    while (b - a) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

x = a
while x < b:
    x_next = x + step

    if f(x) * f(x_next) < 0:
        root = bisection(x, x_next, eps)
        roots.append(root)

    x = x_next


print("Roots found:")
for r in roots:
    print(r)