import numpy as np


def split(x, h):
    """ Split the interval
    
    Args:
        x: list/ndarray, the interval to be splited
        h: double, the step length of the split

    Returns:
        t: ndarray/list, the split of the interval t
    """
    # the endpoints of the interval
    a, b = x 
    n = int((b - a)/h)
    t = np.linspace(a, b, n+1)
    
    return t


def improved_Euler(x, func, ini):
    """ Solve IVP by improved Euler method
    
    Args:
        x: list/ndarray, the splitiation of the interval
        func: the function f(x, y) which satisfies y'(x) = f(x, y)
        ini: the initial value for IVP

    Returns:
        y: ndarray, the list of values of y at every t
    """
    n = len(x)
    h = x[1] - x[0]

    # begin iteration
    y = np.zeros(n)
    y[0] = ini
    for i in range(1, n):
        y0 = y[i-1] + h*func(x[i-1], y[i-1])
        y[i] = y[i-1] + h*(func(x[i-1], y[i-1]) + func(x[i], y0))/2

    return y


def f1(x, y):
    return y**2


def f2(x, y):
    return x/y 


def g(x, y):
    return np.sin(x)/x


if __name__ == '__main__':
    h = 0.1
    # the solution for ordinary differential equation 1
    t1 = [0, 0.4]
    x1 = split(t1, h)
    y1 = improved_Euler(x1, f1, 1)
    y1_true = 1/(1 - x1)
    print("The numerical solution, analytic solution and the error of question 1 are as follows:")
    for item in zip(x1, y1, y1_true):
        print(f"{item[0]:.1f}\t{item[1]:.6f}\t{item[2]:.6f}\t{item[2] - item[1]:.6f}")
    # the solution for ordinary differential equation 2
    t2 = [2.0, 2.6]
    x2 = split(t2, h)
    y2 = improved_Euler(x2, f2, 1)
    y2_true = np.sqrt(x2**2 - 3)
    print("The numerical solution, analytic solution and the error of question 2 are as follows:")
    for item in zip(x2, y2, y2_true):
        print(f"{item[0]:.1f}\t{item[1]:.6f}\t{item[2]:.6f}\t{item[2] - item[1]:.6f}")

    # thinking question
    # calculate the integral \int_0^1 \frac{\sin x}{x} dx
    x3 = split([1e-32, 1], 0.01)
    y3 = improved_Euler(x3, g, 0)
    print(f"The value of Si(1) is {y3[-1]:.5f}.")

