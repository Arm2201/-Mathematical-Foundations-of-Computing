A = [
    [2, 1],
    [1, -3]
]

b = [3, -2]

x_prev = [0.5, 0.5]
x = x_prev

if __name__ == "__main__":
    iter_num = 20

    for i in range(iter_num):
        x[0] = (b[0] - A[0][1] * x_prev[1]) / A[0][0]
        x[1] = (b[1] - A[1][0] * x_prev[0]) / A[1][1]
        x_prev = x

        print(f"x = {x}")
