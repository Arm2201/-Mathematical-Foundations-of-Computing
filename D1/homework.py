def f(x):
    return x**2 - 2


def bisection(a, b):
    for i in range(100):
        c = (a + b) / 2
        print(f"Iteration {i+1}: c = {c}")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c


if __name__ == "__main__":
    a = 1
    b = 2
    bisection(a, b)
