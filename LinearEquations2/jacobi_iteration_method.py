import numpy as np


def jacobi_iteration(A, b, tol=1e-9, Max_iter=5000):
    """ Solve linear equations by Jacobi iteration method.

    Args:
        A: ndarray, coefficients matrix
        b: ndarray, constant vector
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        y: ndarray, solution of the linear equations
        k: int, iteration number
    """
    # decompose coefficients matrix
    D = np.diag(np.diag(A))
    L_plus_U = D - A

    # construct iterative coefficients matrix
    B = np.linalg.inv(D).dot(L_plus_U)
    f = np.linalg.inv(D).dot(b)

    # initial solution vector
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
    # Jacobi iteration method
    x, n = jacobi_iteration(A, b, 1e-5)

    print("The solution of the linear euqations is:")
    for i in range(len(x)):
        print(f'x_{i+1} = {x[i]}')
    print(f"The iteration number is {n}.")

