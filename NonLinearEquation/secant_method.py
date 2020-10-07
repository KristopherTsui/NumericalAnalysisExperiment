import math


def secant_method(x, func, tol):
    """ Solve non-linear equation by sectant method

    Args:
        x: list, two initial values of the iteration
        func: the function to be solved
        tol: double, iteration accurancy

    Returns:
        iter_ls: list, the values of the iteration
    """
    # iteration
    x0, x1 = x
    x2 = x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))

    iter_ls = []
    while math.fabs(x2 - x1) >= tol:
        iter_ls.append(x2)
        x0, x1 = x1, x2
        x2 = x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))

    return iter_ls


def f(x):
    """ The function to be solved

    Args:
        x: double, dependent variable

    Returns:
        y: double, the value of the function at x
    """
    y = x**3 + x**2 - 3*x -3
    return y


if __name__ == '__main__':
    iter_ls = secant_method(x=[1.5, 2], func=f, tol=1e-6)
    for item in iter_ls:
        print(item)

