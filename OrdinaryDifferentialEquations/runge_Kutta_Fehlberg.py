import numpy as np


def f(x, y):
    return y**2


def g(x, y):
    return x/y


def runge_Kutta_Fehlberg(inte, ini, func, h_list, tol=1e-6):
    """ Solve ODE's IVP by Runge Kutta Fehlberg method.

    Args:
        inte: list/ndarray, the interval to be solved
        ini: double, initial value for the IVP
        func: function object, y' = func(x, y)
        h_list: list/ndarry, the boundary of h
        tol: double, iteration accuracy

    Returns:
        x: ndarray, list of independent variables
        y: ndarray, list of value of numberical solutions
    """
    x = [inte[0]]
    y = [ini]
    # set h = h_max
    h = h_list[1]

    # iteration
    while x[-1] + h <= inte[1]:
        k1 = h * func(x[-1], y[-1])
        k2 = h * func(x[-1] + h/4, y[-1] + k1/4)
        k3 = h * func(x[-1] + 3*h/8, y[-1] + 3*k1/32 + 9*k2/32)
        k4 = h * func(x[-1] + 12*h/13, y[-1] + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
        k5 = h * func(x[-1] + h, y[-1] + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
        k6 = h * func(x[-1] + h/2, y[-1] - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)
        R = np.abs(k1/360 - 128*k3/4275 - 2197*k4/75240 + k5/50 + 2*k6/55)
        # satisfy the accuracy, add to the list
        if R <= h * tol:
            x.append(x[-1] + h)
            y.append(y[-1] + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5)
        else:
            # modify the step length h
            q = 0.84 * (tol * h / R)**0.25
            if q <= 0.1:
                h = 0.1 * h
            elif q >= 4:
                h = 4 * h 
            else:
                h = q * h

            # the boundary of h
            if h <= h_list[0]:
                h = h_list[0]
            elif h >= h_list[1]:
                h = h_list[1]

    return np.array(x), np.array(y)


if __name__ == '__main__':
    inte1 = [0, 0.4]
    x1, y1 = runge_Kutta_Fehlberg(inte1, 1, f, [0.05, 0.1], 1e-6)
    y1_true = 1 / (1 - x1)
    print("Numerical solution, analytical solution and the error of queation 1 are as follows:")
    for item in zip(x1, y1, y1_true):
        print(f"{item[0]:.7f}\t{item[1]:.7f}\t{item[2]:.7f}\t{item[2]-item[1]:.8f}")

    inte2 = [2.0, 2.6]
    x2, y2 = runge_Kutta_Fehlberg(inte2, 1, g, [0.05, 0.1], 1e-6)
    y2_true = np.sqrt(x2**2 - 3)
    print("Numerical solution, analytical solution and the error of question 2 are as follows:")
    for item in zip(x2, y2, y2_true):
        print(f"{item[0]:.7f}\t{item[1]:.7f}\t{item[2]:.7f}\t{item[2]-item[1]:.8f}")

