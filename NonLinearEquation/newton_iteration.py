import math
import sympy as sp


def newton_iteration(x0, func, tol):
    """ Solve non-linear equation by Newton iteratin method

    Args:
        x0: double, the initial value of the iteration
        func: Symbol function, the non-linear equation to be solved
        tol: double, the iteration accurancy

    Returns:
        iter_list: list, the value of x every iteration
    """
    x = sp.Symbol('x')
    # derivative
    y_diff = sp.diff(func(x))
    # begin iteration
    u = x0
    v = u - func(u)/y_diff.subs(x, u)

    iter_list = []
    while math.fabs(v - u) >= tol:
        iter_list.append(v)
        u = v
        v = u - func(u)/y_diff.subs(x, u)

    return iter_list


def f(x):
    """ The equation to be solved

    Args:
        x: symbol variable, independent variable

    Returns:
        y: symbol, the symbol expression of the function
    """
    y = sp.Pow(x, 3) + sp.Pow(x, 2) - 3*x - 3
    return y


if __name__ == '__main__':
    """ The initial values
    When x0 = -2, it converges to another root -sqrt{3}
    When x0 = -1, it is the root of the function
    When x0 = 0, it doesn't converge
    When x0 = 2, it converges to sqrt{3} quickly
    When x0 = 3000000, it converges to sqrt{3} slowly
    """
    x = [-2.0, -1.0, 0.0, 2.0, 3000000.0]
    for x0 in x:
        iter_ls = newton_iteration(x0, f, 1e-6)
        print(f"The iteration list with the initial value {x0} is:")
        for item in iter_ls:
            print(item)
