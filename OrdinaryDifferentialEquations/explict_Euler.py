import numpy as np
import matplotlib.pyplot as plt


def split(inte, h):
    """ Split the interval

    Args:
        inte: list/ndarray, the interval to be splited
        h: the step length of the split

    Returns:
        x: list/ndarray, the split of the inteval
    """
    # the endpoints of the interval
    a, b = inte
    n = int((b - a)/h)
    x = np.linspace(a, b, n+1)

    return x


def explict_Euler(x, func, ini):
    """ Solve ODEs by explict Euler method

    Args:
        x: list/ndarray, the split of the interval
        func: binary funciton, satisfies y'(x) = f(x, y)
        ini: double, the initial value for IVP
    
    Returns:
        y: list/ndarray, the values of the function y(x) at every x
    """
    n = len(x)
    h = x[1] - x[0]

    # iteration
    y = np.zeros(n)
    y[0] = ini
    for i in range(1, n):
        y[i] = y[i-1] + h*func(x[i-1], y[i-1])

    return y


def f(x, y):
    z = -50 * y
    return z


if __name__ == '__main__':
    h = [0.1, 0.05, 0.01, 0.001]
    for h0 in h:
        print(f"The numerical solution which h is equal to {h0} is as follows:")
        inte = [0, 20*h0]
        x = split(inte, h0)
        y = explict_Euler(x, f, 100)
        for item in zip(x, y):
            print(f"{item[0]:.3f}\t{item[1]:.16f}")

