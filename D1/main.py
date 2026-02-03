import math
def is_inside(x,y):
    return math.sqrt(x**2 + y**2) <= 1

if __name__ == "__main__":
    a = -2
    b = 2

    c = -2
    d = 2

    eps = 0.01
    n = 10

    prev_approx_area = None
    approx_area = None
    while prev_approx_area is None or abs(approx_area - prev_approx_area) > eps:
        prev_approx_area = approx_area
        h_x = (b - a) / n
        h_y = (d - c) / n

        x = []
        y = []

        for i in range(n + 1):
            x.append(a + i * h_x)
            y.append(c + i * h_y)

        print(x)
        print(y)

        inside_count = 0
        on_the_edge_count = 0

        for i in range(n):
            for j in range(n):
                x1, y1 = x[i], y[i]
                x2, y2 = x[i], y[j + 1]
                x3, y3 = x[i + 1], y[j]
                x4, y4 = x[i + 1], y[j + 1]

                if is_inside(x1, y1) and is_inside(x2, y2) and is_inside(x3, y3) and is_inside(x4, y4):
                    inside_count += 1

                elif is_inside(x1, y1) or is_inside(x2, y2) or is_inside(x3, y3) or is_inside(x4, y4):
                    on_the_edge_count += 1

        rect_area = h_x * h_y
        inside_area = inside_count * rect_area
        edge_area = on_the_edge_count * rect_area

        approx_area = (inside_count * rect_area + on_the_edge_count * rect_area * 0.5)

        print(approx_area)

        n *= 2