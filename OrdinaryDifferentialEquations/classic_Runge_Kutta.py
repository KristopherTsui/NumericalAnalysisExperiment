import numpy as np


def split(inte, h):
    """ Split the interval

    Args:
        inte: list/ndarray, the interval to be splited
        h: the step length of the split

    Returns:
        x: list/ndarray, the split of the interval
    """
    # the endpoints of the interval
    a, b = inte
    n = int((b - a)/h)
    x = np.linspace(a, b, n+1)
    
    return x


def classical_Runge_Kutta(x, func, ini):
    """ Solve ordinary differential equation by 4-th Runge Kutta Method

    Args:
        x: list/ndarray, the split of the interval
        func: the function which satisifies y'(x) = f(x, y)
        ini: double, the initial value for IVP

    Returns:
        y: list/ndarray, the values of the function y(x) at every point x
    """
    n = len(x)
    h = x[1] - x[0]
    A = np.diag([1/2, 1/2, 1], k=-1)
    B = np.array([1/6, 1/3, 1/3, 1/6])
    C = np.array([0, 1/2, 1/2, 1])

    # begin iteration
    y = np.zeros(n)
    y[0] = ini
    for i in range(1, n):
        k = np.zeros(4)
        for j in range(4):
            y_step = 0
            for m in range(4):
                y_step += A[j, m]*k[m]
            k[j] = func(x[i-1]+C[j]*h, y[i-1]+h*y_step)
        phi = 0
        for j in range(4):
            phi += B[j]*k[j]
        y[i] = y[i-1] + h*phi

    return y


def f1(x, y):
    z = y**2
    return z


def f2(x, y):
    z = x/y
    return z


if __name__ == '__main__':
    h = 0.1
    # solve the ordinary differential equation 1 by 4-th Runge-Kutta method
    interval1 = [0, 0.4]
    x1 = split(interval1, h)
    y1 = classical_Runge_Kutta(x1, f1, 1)
    y1_true = 1/(1 - x1)
    print("The numerical solution, analytic solution and the error of the question 1 are as follows:")
    for item in zip(x1, y1, y1_true):
        print(f"{item[0]:.1f}\t{item[1]:.7f}\t{item[2]:.7f}\t{item[2]-item[1]:.7f}")
    # solve the ordinary differential equation 2 by 4-th Runge-Kutta method
    interval2 = [2, 2.6]
    x2 = split(interval2, h)
    y2 = classical_Runge_Kutta(x2, f2, 1)
    y2_true = np.sqrt(x2**2 - 3)
    print("The numerical solution, analytic solution and the error of the question 2 are as follows:")
    for item in zip(x2, y2, y2_true):
        print(f"{item[0]:.1f}\t{item[1]:.7f}\t{item[2]:.7f}\t{item[2]-item[1]:.7f}")

