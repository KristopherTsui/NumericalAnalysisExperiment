import math


def secant_method(x_lst, func, tol=1e-9, Max_iter=100):
    """ Solve non-linear equation by sectant method.

    Args:
        x_lst: list/ndarray, two initial values of the iteration
        func: function object, the function to be solved
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        x2: double, root of the non-linear equation
    """
    # initial values
    x0, x1 = x_lst
    # first iteration
    k = 1
    x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))

    # iteration
    while math.fabs(x2 - x1) >= tol and k < Max_iter:
        k += 1
        x0, x1 = x1, x2
        x2 = x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))

    return k, x2


def f(x):
    return x**3 + x**2 - 3*x -3


if __name__ == '__main__':
    n, x = secant_method([1.5, 2], f, 1e-6)
    print(f"The root of the non-linear equation is {x:.7f} by secant method.")
    print(f"Iteration number is {n}.")

