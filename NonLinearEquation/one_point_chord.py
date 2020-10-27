import math


def one_point_chord(x_lst, func, tol=1e-9, Max_iter=100):
    """ Solve the non-linear equation by one point chord.

    Args:
        x_lst: list/ndarray, two initial values of the iteration
        func: function object, the non-linear function to be solved
        tol: double, the iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        v: double, root of the non-linear equation
    """
    # initial values
    x0, u = x_lst
    # first iteration
    k = 1
    v = u - func(u) * (u - x0) / (func(u) - func(x0))

    # iteration
    while math.fabs(v - u) >= tol and k < Max_iter:
        k += 1
        u = v
        v = u - func(u) * (u - x0) / (func(u) - func(x0))

    return k, v


def f(x):
    return x**3 + x**2 - 3*x - 3


if __name__ == '__main__':
    n, x = one_point_chord([1.5, 2], f, 1e-6)
    print(f"The root of the non-linear equation is {x:.7f} by one point chord.")
    print(f"Iteration number is {n}.")

