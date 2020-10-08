import numpy as np


def f(y):
    return -50*y


def split(inte, h):
    """ Split the interval

    Args: 
        inte: list/ndarray, the interval to be splited
        h: double, the step length of the split

    Returns:
        x: list/ndarray, the split of the interval
    """
    # the endpoints of the interval
    a, b = inte
    n = int((b - a)/h)
    x = np.linspace(a, b, n+1)
    
    return x


def implict_Euler(x, func, ini):
    """ Solve the ordinary equation y' = -50y, y(0)=100

    Args:
        x: list/ndarray, the split of the interval
        func: the function f(y)
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
        y[i] = y[i-1]/(1 + 50*h)

    return y


if __name__ == '__main__':
    h = [0.1, 0.05, 0.01, 0.001]
    for h0 in h:
        print(f"The numerical solution of ODE for h = {h0} is as follows:")
        inte = [0, 20*h0]
        x = split(inte, h0)
        y = implict_Euler(x, f, 100)
        for item in zip(x, y):
            print(f"{item[0]:.3f}\t{item[1]:.16f}")

