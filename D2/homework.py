import math

def f(x):
    return x**3 - x - 2

def f_prime(x):
    return 3*x**2 - 1

def g(x):
    alp = -0.1
    return x + alp * f(x)

def test_bisection():
    a = 1
    b = 2
    eps = 0.0001

    iters_count = int(math.log2((b - a) / eps)) + 1

    for i in range(iters_count):
        xk = (a + b) / 2
        print(f"{i+1}: xk = {xk}, f(xk) = {f(xk)}")

        if f(a) * f(xk) < 0:
            b = xk
        else:
            a = xk

def test_fixed_point():
    xk = 1.5
    eps = 0.0001

    iter_num = 0
    while iter_num == 0 or abs(g(xk) - xk) > eps:
        iter_num += 1
        xk = g(xk)
        print(f"{iter_num}: xk = {xk}, f(xk) = {f(xk)}")

def test_newton():
    xk = 1.5
    eps = 0.0001

    iter_num = 0
    while iter_num == 0 or abs(f(xk)) > eps:
        iter_num += 1
        xk = xk - f(xk) / f_prime(xk)
        print(f"{iter_num}: xk = {xk}, f(xk) = {f(xk)}")


if __name__ == "__main__":
    print("Bisection:")
    test_bisection()

    print("\nFixed point:")
    test_fixed_point()

    print("\nNewton:")
    test_newton()


# conclusion: The bisection method is the most stable and always converges, but it is the slowest. The fastest method is Newton's method, which converges quickly when close to the root but can diverge if the initial guess is not close enough.