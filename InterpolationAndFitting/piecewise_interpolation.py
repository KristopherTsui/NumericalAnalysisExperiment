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
                l *= (x - t[j]) / (t[i] - t[j])

        L += l

    return sp.simplify(L)


def draw_polinomial(inte, func, lst):
    """ Draw the original function and the interpolation function

    Args:
        inte: list, the interval of the function
        func: symbol object, the original function
        lst: list, the list of the endpoints number
    """
    # draw the original function
    fig = sp.plot(func(x), (x, -5, 5), line_color='r', label='Original Fuction', legend=True, show=False)
    # control color
    i = 0
    colors = ['b', 'y', 'g']
    for n in lst:
        # polinomial interpolation
        t = split(inte, n)
        y = lagrange_interpolation(t, func(t))
        print(f"The {n}-order interpolation polinomial is {y}")
        # draw polinomial interpolation
        color = colors[i]
        i += 1
        p = sp.plot(y, (x, -5, 5), line_color=color, label=f'n={n}', lengend=True, show=False)
        fig.extend(p)
    fig.save('polinomial_interpolation.png')


def piecewise_linear_interpolation(t, y):
    """ Piecewise linear interpolation
    
    Args:
        t: list/ndarray, the split of the interval
        y: list/ndarray, the value of the function at every interpolation point

    Returns:
        L: list, the expresion of the interpolation at every little interval
    """
    # the number of the interpolation points
    n = len(t)

    # iteration
    L = []
    for i in range(n-1):
        l = lagrange_interpolation(t[i:i+2], y[i:i+2])
        L.append((sp.simplify(l), sp.And(x >= t[i], x <= t[i+1])))

    return sp.Piecewise(*L) 


def draw_piecewise(inte, func, lst):
    """ Draw the piecewise linear interpolation function and original function

    Args:
        y: symbol object, the piecewise linear interpolation function
        func: symbol object, the original function
        file_name: string, the name of figure name
    """
    # draw the original function
    fig = sp.plot(func(x), (x, -5, 5), line_color='r', label='Original Fuction', legend=True, show=False)
    # control color
    i = 0
    colors = ['b', 'y', 'g']
    for n in lst:
        # piecewice linear interpolation
        t = split(inte, n)
        y = piecewise_linear_interpolation(t, func(t))
        # draw polinomial interpolation
        color = colors[i]
        i += 1
        p = sp.plot(y, (x, -5, 5), line_color=color, label=f'n={n}', lengend=True, show=False)
        fig.extend(p)
    fig.save('piecewise_interpolation.png')
    


if __name__ == '__main__':
    inte = [-5, 5]
    n_list = [5, 10, 20]

    # polinomial interpolation
    draw_polinomial(inte, f, n_list)
    # piecewise interpolation
    draw_piecewise(inte, f, n_list)

