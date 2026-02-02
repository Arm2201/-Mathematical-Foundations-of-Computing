import math
def is_inside(x,y):
    return math.sqrt(x**2 + y**2) <= 1

if __name__ == "__main__":
    a = -2
    b = 2

    c = -2
    d = 2

    n = 10

    h = (b-a)/n

    x = []
    y = []

    for i in range(n + 1):
        x.append(a + i * h)
        y.append(c + i * h)