import math

def g(x):
    return math.sqrt(x + 2)

a = 1
b = 4

eps = 0.001
iters_count = int(math.log2((b - a) / eps)) + 1

x0 = 3

print("xk")

for i in range(iters_count):
    x_new = g(x0)
    if a <= x_new <= b:
        print(x_new)
    else:
        break

    if abs(x_new - x0) < eps:
        break

    x0 = x_new
