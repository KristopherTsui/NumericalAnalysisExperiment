import numpy as np


def inverse_power_method(A, tol=1e-9, Max_iter=100):
    """ Calculate the minimum eigenvalue and the corresponding eigenvector by inverse power method.

    Args:
        A: ndarray, the matrix to be solved
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Retruns:
        k: int, interation number
        eig: double. minimum eigenvalue of the matrix A
        eigv: ndarray, corresponding eigenvector
    """
    # initialization
    # iteration number
    k = 0
    # initial eigenvalue
    eig = 0
    # initial eigenvector
    eigv = np.ones(A.shape[0])

    # iteration
    while k < Max_iter and np.linalg.norm(A @ eigv - eig * eigv) >= tol:
        k += 1
        x = np.linalg.solve(A, eigv)
        eig = 1 / x[np.argmax(x)]
        eigv = x * eig

    return k, eig, eigv


def acceleration_inverse_power(A, alpha, tol=1e-9, Max_iter=100):
    """ Calculate the eigenvalue around alpha and corresponding eigenvector by inverse power method.

    Args:
        A: ndarray, the matrix to be solved
        alpha: double, acceleration number
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        eig: double, eigenvalue around alpha of the matrix A
        eigv: ndarray, corresponding eigenvector
    """
    # initialization
    B = A - alpha * np.eye(A.shape[0])

    # inverse power method
    k, eig, eigv = inverse_power_method(B, tol, Max_iter)

    eig += alpha

    return k, eig, eigv


if __name__ == '__main__':
    A = np.array([[4, -1, 1], [-1, 3, -2], [1, -2, 3]])
    n, eig, eigv = inverse_power_method(A, 1e-6)
    print(f"The eigenvalue is {eig:.7f}, and corresponding eigenvector is {eigv}.")
    print(f"Iteration number is {n}.")
    n, eig, eigv = acceleration_inverse_power(A, 2.5, 1e-6)
    print(f"The eigenvalue around 2.5 is {eig:.7f}, and corresponding eigenvector is {eigv}.")
    print(f"Iteration number is {n}.")

