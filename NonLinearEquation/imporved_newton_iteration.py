from sympy.abc import x
import sympy as sp
import math


def improved_Newton_iteration(x0, func, tol=1e-9, Max_iter=100):
    """ Solve non-linear equation by improved Newton iteration method.

    Args:
        x0: double, iteration initial value
        func: function object, the function to be solved
        tol: double, iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        z: double, root of the non-linear equation
    """
    # derivative
    y_diff = sp.diff(func(x))

    # first iteration
    k = 1
    u = x0
    v = u - func(u) / y_diff.subs(x, u)
    z = u - 2 * func(u) / (y_diff.subs(x, u) + y_diff.subs(x, v))

    # iteration
    while math.fabs(z - u) >= tol and y_diff.subs(x, z) != 0 and k < Max_iter:
        k += 1
        u = z
        v = u - func(u) / y_diff.subs(x, u)
        z = u - 2 * func(u) / (y_diff.subs(x, u) + y_diff.subs(x, v))

    return k, z


def f(x):
    return sp.Pow(x, 3) + sp.Pow(x, 2) - 3 * x - 3


if __name__ == '__main__':
    n, root = improved_Newton_iteration(2.0, f, 1e-6)
    print(f"The root of the non-linear equation is {root:.7f} by improved Newton iteration method.")
    print(f"Iteration number is {n}")

