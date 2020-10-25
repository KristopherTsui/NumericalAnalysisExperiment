import numpy as np
from jacobi_iteration_method import jacobi_iteration
from gauss_seidel_iteration import gauss_seidel_iteration


def successive_over_relaxation(A, b, omega, tol=1e-9, Max_iter=5000):
    """ Solve linear equations by successive over relaxation method.

    Args:
        A: ndarray, coefficients matrix
        b: ndarray, constant vector
        omega: double, hyperrelaxation factor
        tol: double, iteration accuracy
        Max_iter: maximum iteration number

    Returns:
        y: ndarray, solution of the linear euqations
        k: int, iteration number
    """
    # decompose coefficients matrix
    D = np.diag(np.diag(A))
    L = -1 * np.tril(A - D)
    U = -1 * np.triu(A - D)

    # construct iteration coefficients matrix
    B = np.linalg.inv(D - omega * L).dot((1 - omega) * D + omega * U)
    f = omega * np.linalg.inv(D - omega * L).dot(b)

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


def print_solution_and_iteration_number(x, n):
    """ Print the solution and iteration number.

    Args:
        x: ndarray, solution vector
        n: int, iteration number
    """
    for i in range(len(x)):
        print(f"x_{i+1} = {x[i]}")
    print(f"The iteration number is {n}.")


if __name__ == '__main__':
    # coefficients matrix
    A = np.array([[-4, 1, 1, 1], [1, -4, 1, 1], [1, 1, -4, 1], [1, 1, 1, 1 -4]])
    # constant vector
    b = np.ones(4)
    # Jacobi iteration method
    x1, n1 = jacobi_iteration(A, b)
    print("The solution of the linear equations by Jacobi iteration method is:")
    print_solution_and_iteration_number(x1, n1)
    # Gauss Seidel iteration method
    x2, n2 = gauss_seidel_iteration(A, b)
    print("The solution of the linear equations by Gauss Seidel iteration method is:")
    print_solution_and_iteration_number(x2, n2)
    # successive over relaxation method
    # when selecting the hyperrelaxation factor, it should be between 1.285 and 1.307
    # then the minumum iteration number is 21
    x3, n3 = successive_over_relaxation(A, b, 1.3)
    print("The solution of the linear equations by successive over relaxation method is:")
    print_solution_and_iteration_number(x3, n3)

