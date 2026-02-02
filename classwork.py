def f(x):
    return x**2 - 4

a = 0
b = 3

for i in range(100):
    c = (a + b) / 2
    if f(c) * f(a) < 0:
        b = c
    elif f(c) * f(b) < 0:
        a = c
    else:
        if (f(a) == 0):
            c = a
        elif (f(b) == 0):
            c = b
    print(c, f(c))

