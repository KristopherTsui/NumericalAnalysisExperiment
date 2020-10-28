import numpy as np


def power_method(A, ini_vec, tol=1e-9, Max_iter=100):
    """ Calculate maximum eigenvalue of matrix A by power method.

    Args:
        A: ndarray, the matrix to be solved
        ini_vec: list/ndarray, the initial eigenvector
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        eig: double, main eigenvalue(maximum) of matrix A
        eigv: ndarray, corresponding eigenvector
    """
    # initialization
    # iteration number
    k = 0
    # initial eigenvalue
    eig = 0 
    # initial eigenvector
    eigv = np.array(ini_vec)

    # iteration
    while k < Max_iter and np.linalg.norm(A @ eigv - eig * eigv) >= tol:
        k += 1
        x = A @ eigv
        eig = x[np.argmax(x)]
        eigv = x / eig

    return k, eig, eigv


def acceleration_power_method(A, alpha, tol=1e-9, Max_iter=100):
    """ Calculate maximum eigenvalue of matrix A by origin translation acceration power method.

    Args:
        A: ndarray, the matrix to be solved
        alpha: double, acceleration parameter
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        eig: double, main eigenvalue(maximum) of matrix A
        eigv: ndarray, corresponding eigenvector
    """
    # initialization
    B = A - alpha * np.eye(A.shape[0])
    
    # power method
    k, eig, eigv = power_method(B, np.ones(A.shape[0]), tol, Max_iter)

    eig += alpha

    return k, eig, eigv


if __name__ == '__main__':
    A = np.array([[4, -1, 1], [-1, 3, -2], [1, -2, 3]])
    # power method
    ini_vecs = [[1, 1, 1], [2.001, 1.999, 0], [0, 1, 1]]
    for ini_vec in ini_vecs:
        n, eig, eigv = power_method(A, ini_vec, 1e-6)
        print(f"When selecting the initial values {ini_vec},") 
        print(f"main eigenvalue is {eig:.7f}, corresponding eigenvector is {eigv},") 
        print(f"the iteration number is {n}.")

    # acceleration power method
    alpha_lst = np.linspace(1, 3, 5)
    for alpha in alpha_lst:
        n, eig, eigv = acceleration_power_method(A, alpha, 1e-6)
        print(f"Whene selection the parameter alpha = {alpha},")
        print(f"main eigenvaluue is {eig:.7f}, corresponding eigenvector is {eigv},")
        print(f"the iteration number is {n}")

