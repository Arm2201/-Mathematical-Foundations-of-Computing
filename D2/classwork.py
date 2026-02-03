import math

a = 1
b = 5

eps = 0.001
iters_count = int(math.log2((b-a)/eps)) + 1



for i in range(iters_count):
    c = (b - a) / 2
    if f(c)*f(a) < 0:
        b = c
    elif f(c)*f(b) < 0:
        a = c
    else:
        break