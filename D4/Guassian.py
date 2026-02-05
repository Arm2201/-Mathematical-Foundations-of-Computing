# experiment with hilbert matrix task is at the bottom, line 45 - 86.


A = [[1, 1, 1], [3, 2, 1], [2, -1, 4]]
b = [6, 10, 12]

A = [row[:] for row in A]
b = b[:]

n = len(A)

# Forward pass of elimination
for i in range(n-1):
    if A[i][i] == 0:
        raise ValueError("Zero pivot encountered")
    for j in range(i+1, n):
        k_temp = -A[j][i] / A[i][i]
        print(f"Step {i+1} {j+1}: k = {k_temp:.2f}")

        temp_row = [a * k_temp for a in A[i]]
        print(f"Temp row: {temp_row}")

        for k in range(n):
            A[j][k] += temp_row[k]

        b[j] += k_temp * b[i]

        print(f"Updated A = {A}")
        print(f"Updated b = {b}")

x_sol = [None for _ in range(n)]
for i in range(n):
    row_idx = n - i - 1
    res = b[row_idx]
    for j in range(n - i, n):
        res -= A[row_idx][j] * x_sol[j]
    x_sol[row_idx] = res / A[row_idx][row_idx]

    print(f"x_{n-i-1} = {x_sol[n-i-1]:.2f}")

print(f"Solution: {x_sol}")



# def gaussian_elimination(A, b):
#     A = [row[:] for row in A]
#     b = b[:]

#     n = len(A)

#     for i in range(n-1):
#         if A[i][i] == 0:
#             raise ValueError("Zero pivot encountered")
#         for j in range(i+1, n):
#             k_temp = -A[j][i] / A[i][i]
#             temp_row = [a * k_temp for a in A[i]]

#             for k in range(n):
#                 A[j][k] += temp_row[k]

#             b[j] += k_temp * b[i]
#     x_sol = [None for _ in range(n)]
#     for i in range(n):
#             row_idx = n - i - 1
#             res = b[row_idx]
#             for j in range(n - i, n):
#                 res -= A[row_idx][j] * x_sol[j]
#             x_sol[row_idx] = res / A[row_idx][row_idx]

#     return x_sol

# def hilbert_matrix(n):
#     return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]

# sizes = [5, 10, 20, 50, 100]

# for n in sizes:
#     A = hilbert_matrix(n)

#     x_exact = [1.0] * n
#     b = [sum(A[i][j] * x_exact[j] for j in range(n)) for i in range(n)]

#     x_computed = gaussian_elimination(A, b)

#     max_error = max(abs(x_computed[i] - 1.0) for i in range(n))
#     print(f"n = {n:3d} | max error = {max_error:.6e}")