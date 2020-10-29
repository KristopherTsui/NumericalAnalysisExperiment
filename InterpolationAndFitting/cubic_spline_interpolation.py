from sympy.abc import x
import sympy as sp
import numpy as np


def split(inte, n):
    """ Split the interval into n subintervals.
    
    Args:
        inte: list/ndarray, the interval to be splited
        n: int, the number of interpolation points

    Returns:
        t: ndarray, the split of the given interval
    """
    # endpoints of the interval
    a, b = inte
    # split
    t = np.linspace(a, b, n+1)
    return t


def second_order_difference(t, y):
    """ Calculate the second order difference.

    Args:
        t: ndarray, the list of the three independent variables
        y: ndarray, three values of the function at every t

    Returns:
        double: the second order difference of given points
    """
    # claculate the first order difference
    first_order_difference = (y[1:] - y[:-1]) / (t[1:] - t[:-1])
    return (first_order_difference[1] - first_order_difference[0]) / (t[2] - t[0])


def cubic_spline_interpolation(t, y, diff_list):
    """ Cubic spline interpoaltion with I boundary conditions.

    """
    # number of the points
    n = len(t)
    # calculate the steps
    h = t[1:] - t[:-1]

    # initialize
    D = np.zeros((n, n))
    d = np.zeros(n)
    # calculate the elements in matrix D
    for i in range(n):
        if i == 0:
            D[0, 0] = 2
            D[0, 1] = 1
        elif i == n-1:
            D[n-1, n-2] = 1
            D[n-1, n-1] = 2
        else:
            D[i, i-1] = h[i-1] / (h[i-1] + h[i]) # mu
            D[i, i] = 2
            D[i, i+1] = h[i] / (h[i-1] + h[i])   # lambda

    # calculate the elements in vector d
    for i in range(n):
        if i == 0:
            # repeat node difference quotient
            d[i] = 6 * ((y[1] - y[0])/(t[1] - t[0]) - diff_list[0]) / (t[1] - t[0])
        elif i == n-1:
            # repeat node difference quotient
            d[i] = 6 * (diff_list[1] - (y[n-1] - y[n-2])/(t[n-1] - t[n-2])) / (t[n-1] - t[n-2])
        else:
            d[i] = 6 * second_order_difference(t[i-1:i+2], y[i-1:i+2])

    # get M by solving the equation DM=d
    M = np.linalg.solve(D, d)

    # iteraton
    S = []
    for i in range(n-1):
        s = M[i] * (t[i+1] - x)**3 / 6 / h[i]
        s += M[i+1] * (x - t[i])**3 / 6 / h[i]
        s += (y[i] - M[i] * h[i]**2 / 6) * (t[i+1] - x) / h[i]
        s += (y[i+1] - M[i+1] * h[i]**2 / 6) * (x - t[i]) / h[i]
        S.append((sp.simplify(s), sp.And(x>=t[i], x<=t[i+1])))

    return sp.Piecewise(*S)


def f(x):
    return 1 / (1 + x**2)


def draw_cubic_spline_interpolation(inte, func, n_lst):
    """ Draw figure of the function's cubic spline interpolation for various endpoints.

    Args:
        inte: list/ndarray, the interpolation itnerval
        func: function object, the function to be interpolated
        n_lst: list/ndarray, list of the endpoints number
    """
    # draw the original function fugure
    fig = sp.plot(func(x), (x, -5, 5), line_color='r', label='Original Function', legend=True, show=False)
    # control color
    i = 0
    colors_lst = ['b', 'y', 'g']

    for n in n_lst:
        t = split(inte, n)
        y = cubic_spline_interpolation(t, func(t), [5/338, -5/338])
        # output
        print(f"The interpoaltion polinomial with n={n} is:")
        print(y)
        # draw
        color = colors_lst[i]
        i += 1
        p = sp.plot(y, (x, -5, 5), line_color=color, label=f'n={n}', legend=True, show=False)
        fig.extend(p)

    # save figure
    fig.save('cubic_spline_interpolation.png')



if __name__ == '__main__':
    inte = [-5, 5]
    n_lst = [5, 10, 20]

    draw_cubic_spline_interpolation(inte, f, n_lst)

