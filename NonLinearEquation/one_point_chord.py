import math


def one_point_chord(x, func, tol):
    """ Solve the non-linear equation by one point chord

    Args:
        x: list, two initial values of the iteration
        func: the non-linear function to be solved
        tol: double, the iteration accurancy

    Returns:
        iter_ls: list, the values of the iteration
    """
    # iteration
    x0, u = x
    v = u - func(u)*(u - x0)/(func(u) - func(x0))

    iter_ls = []
    while math.fabs(v - u) >= tol:
        iter_ls.append(v)
        u = v
        v = u - func(u)*(u - x0)/(func(u) - func(x0))

    return iter_ls


def f(x):
    """ The non-linear equation to be solved

    Args:
        x: double, dependent variable

    Returns:
        y: double, the value of the function at x
    """
    y = x**3 + x**2 - 3*x - 3
    return y


if __name__ == '__main__':
    iter_ls = one_point_chord(x=[1.5, 2], func=f, tol=1e-6)
    for item in iter_ls:
        print(item)

