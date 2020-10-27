from sympy.abc import x
import sympy as sp
import math


def newton_iteration(x0, func, tol=1e-9, Max_iter=100):
    """ Solve non-linear equation by Newton iteratin method.

    Args:
        x0: double, the initial value of the iteration
        func: symbol object, the non-linear equation to be solved
        tol: double, the iteration accuracy
        Max_iter: int, maximum iteration number

    Returns:
        k: int, iteration number
        v: double, root of the non-linear equation
    """
    # derivative
    y_diff = sp.diff(func(x))

    # first iteration
    k = 1
    u = x0
    v = u - func(u)/y_diff.subs(x, u)

    # iteration
    while math.fabs(v - u) >= tol and y_diff.subs(x, v) != 0 and k < Max_iter:
        k += 1
        u = v
        v = u - func(u)/y_diff.subs(x, u)

    return k, v 


def f(x):
    return sp.Pow(x, 3) + sp.Pow(x, 2) - 3*x - 3


if __name__ == '__main__':
    """ The initial values
    When x0 = -2, it converges to another root -sqrt{3}
    When x0 = -1, it is the root of the function
    When x0 = 0, it converges to -1
    When x0 = 2, it converges to sqrt{3} quickly
    When x0 = 3000000, it converges to sqrt{3} slowly
    """
    x0_lst = [-2.0, -1.0, 0.0, 2.0, 9999999999999999.0]
    for x0 in x0_lst:
        n, root = newton_iteration(x0, f, 1e-6)
        print(f"The root of the non-linear equation with initial value {x0} is {root:.7f}.")
        print(f"Iteration number is {n}.")

