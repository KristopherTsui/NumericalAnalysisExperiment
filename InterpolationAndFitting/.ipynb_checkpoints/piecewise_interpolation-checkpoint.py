import sympy as sp
from sympy.abc import x
import numpy as np


def split(inte, n):
    """ Split the interval

    Args:
        inte: list/ndarray, the interval to be splited
        n: int, the number of interpolation points

    Returns:
        t: list/ndarray, the split of the given interval
    """
    # the endpoints of the interval
    a, b = inte
    t = np.linspace(a, b, n+1)
    return t 


def f(t):
    """ The original function to be interpolated

    Args:
        t: double, independent variable

    Returns:
        double, the value of f(x)
    """
    return 1/(1 + t**2)


def lagrange_interpolation(t, y):
    """ Lagrange interpolation polinomials

    Args:
        t: list/ndarray, the interpolation points
        y: list/ndarray, the value of the interpolated function at every point

    Returns:
        L: sympy object, the Lagrange interpolation polinomials
    """
    # the number of the interpolation points
    n = len(t)

    # Lagrange interpolation polinomial
    L = 0
    # iteration
    for i in range(n):
        # the base function of Lagrange interpolation polinomial
        l = y[i]
        for j in range(n):
            if j == i:
                continue
            else:
                l *= (x - x[j]) / (t[i] - t[j])

        L += l

    return sp.simplify(L)


def main():
    sp.plot(f(x), (x, -5, 5))


if __name__ == '__main__':
    t = [-5, 5]
    n_list = [5, 10, 20]


