import numpy as np

"""
ex:
 5x1 + 10x2 +  3x3 +   x4 = 6.7
 6x1 +  7x2 + 20x3 -   x4 = 5.8
12x1 +  2x2 +  3x3 - 30x4 = 4.3
15x1 -   x2 +   x3 +   x4 = 2.1

A . x = B
[
[5, 10, 3, 1],
[6, 7, 20, -4],
[12, 2, 3, -30],
[15, -1, 1, 1]
]

Re-arrange to be diagonally dominant
15x1 -   x2 +   x3 +   x4 = 2.1
 5x1 + 10x2 +  3x3 +   x4 = 6.7
 6x1 +  7x2 + 20x3 -   x4 = 5.8
12x1 +  2x2 +  3x3 - 30x4 = 4.3


A = np.array([
[15, -1,  1,   1],
[ 5, 10,  3,   1],
[ 6,  7, 20,  -4],
[12,  2,  3, -30]
])

B = np.array([2.1, 6.7, 5.8, 4.3])
"""
X = []

# Function to implement the Jacobi method
def jacobi_def(A, B, initial, tolerance=1e-10, max_iterations=100000000):
    n = len(B)
    X = initial.copy()
    new_X = X.copy()
    
    for iteration in range(max_iterations):

        # Print the current iteration and updated values
        print(f"Iteration {iteration + 1}: x1 = {new_X[0]:.6f}, x2 = {new_X[1]:.6f}, x3 = {new_X[2]:.6f}, x4 = {new_X[3]:.6f}")

        for i in range(n):
            # Calculate the sum of A[i][j] * X[j] for all j except i (to remove dialgonal elements)
            sum_Ax = 0
            for j in range(n):
                if j != i:
                    sum_Ax += A[i][j] * X[j]

            # update X[i] using the Jacobi method
            new_X[i] = (B[i] - sum_Ax) / A[i][i]
        
        # check if the solution has converged
        if np.allclose(X, new_X, atol=tolerance):
            break
        
        # Update X to the new values for next iteration
        X = new_X.copy()

    return X

# Function to implement the Gauss-Seidel method
def gauss_seidel(A, B, initial, tolerance=1e-10, max_iterations=100000000):
    n = len(B)
    X = initial.copy()  # Initial guess
    
    for iteration in range(max_iterations):

        # Print the current iteration and updated values
        print(f"Iteration {iteration + 1}: x1 = {X[0]:.6f}, x2 = {X[1]:.6f}, x3 = {X[2]:.6f}, x4 = {X[3]:.6f}")

        # Iterate over each variable
        for i in range(n):
            # Calculate the sum of A[i][j] * X[j] for all j except i
            sum_Ax = 0
            for j in range(n):
                if j != i:
                    sum_Ax += A[i][j] * X[j]

            # Update X[i] directly using the Gauss-Seidel formula
            X[i] = (B[i] - sum_Ax) / A[i][i]
        
        # Check if the solution has converged
        if np.allclose(B, np.dot(A, X), atol=tolerance):
            break

    return X

A = np.array([
[15, -1,  1,   1],
[ 5, 10,  3,   1],
[ 6,  7, 20,  -4],
[12,  2,  3, -30]
])

B = np.array([2.1, 6.7, 5.8, 4.3])

# Initial guess
initial_guess = np.zeros(len(B))

# Call the Jacobi method
solution = jacobi_def(A, B, initial_guess)
print("Final jacobi Solution:", solution)

# Call the Gauss-seidel method
solution = gauss_seidel(A, B, initial_guess)
print("Final gauss_seidel Solution:", solution)
