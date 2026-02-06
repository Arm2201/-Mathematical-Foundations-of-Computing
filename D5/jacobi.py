import random

def generate_diagonally_dominant_matrix(n):
    A = [[0 for _ in range(n)] for _ in range(n)]
    b = [0 for _ in range(n)]

    for i in range(n):
        row_sum = 0
        for j in range(n):
            if j != i:
                A[i][j] = random.randint(-5, 5)
                row_sum += abs(A[i][j])

        A[i][i] = row_sum + random.randint(1, 5)
        b[i] = random.randint(-10, 10)

    return A, b

if __name__ == "__main__":
    n = 2
    eps = 0.0001
    max_iter = 200

    A, b = generate_diagonally_dominant_matrix(n)

    print("Matrix A:")
    for row in A:
        print(row)
    print("Vector b:", b)

    x_prev = [0.5 for _ in range(n)]
    x = [0 for _ in range(n)]

    it = 0
    diff = eps + 1

    while diff >= eps and it < max_iter:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x_prev[j]

            x[i] = (b[i] - s) / A[i][i]

        diff = 0
        for i in range(n):
            diff += abs(x[i] - x_prev[i])

        print(f"iter {it+1}: x = {x}, diff = {diff}")

        x_prev = x[:]
        it += 1
