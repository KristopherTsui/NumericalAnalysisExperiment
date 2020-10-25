import numpy as np


def gauss_seidel_iteration(A, b, tol=1e-9, Max_iter=5000):
    """ Solve linear equations by Gauss Seidel iteration method.

    Args:
        A: ndarray, coefficients matrix.
        b: ndarray, constant vector.
        tol: double, iteration accuracy, default=1e-9.
        Max_iter: int, maximum iteration number, default=5000.

    Returns:
        y: ndarray, solution vector.
        k: int, iteration number.
    """
    # decompose coefficients matrix
    D = np.diag(np.diag(A))
    L = -1 * np.tril(A - D)
    U = -1 * np.triu(A - D)
    
    # construct iterative coefficients matrix
    B = np.linalg.inv(D - L).dot(U)
    f = np.linalg.inv(D - L).dot(b)

    # initial iteration vector
    x = np.ones_like(b)
    # first iteration
    k = 1
    y = B.dot(x) + f

    # iteration
    while np.max(np.abs(y - x)) >= tol and k < Max_iter:
        k += 1
        x = y
        y = B.dot(x) + f
    
    return (y, k)
        

if __name__ == '__main__':
    # cofficients matrix
    A = np.array([[5, 2, 1], [2, 8, -3], [1, -3, -6]])
    # constant vector
    b = np.array([8, 21, 1])
    # Gauss-Seidel iteration method
    x, n = gauss_seidel_iteration(A, b, 1e-5)
    # output
    print("The solution of the linear euqations is:")
    for i in range(len(x)):
        print(f"x_{i+1} = {x[i]}")
    print(f"The iteration number is {n}.")

