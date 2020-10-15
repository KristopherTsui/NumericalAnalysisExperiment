import numpy as np


def f(x):
    return np.exp(-1*x**2)


def g(x):
    return np.sin(x) / x


def compound_trapezoid_formula(inte, func, tol):
    """ Calculate the integral by compound trapezoid formula

    Args:
        inte: ndarray, the integrand interval
        func: function object, the integrand function
        tol: double, the iteration accurancy

    Returns:
        (T1, n): 
            T1: double, the integral value by compound trapezoid formula
            n: int, the number of iteration
    """
    # calculate the initial value by trapezoid formula
    T0 = (inte[1] - inte[0]) * np.sum(func(inte)) / 2
    # calculate another integral value by compound trapezoid iteration formula
    n = 1
    x_list = np.linspace(inte[0], inte[1], 2**n + 1)
    T1 = T0 / 2 + (x_list[1] - x_list[0]) * np.sum(func(x_list[1::2]))
    # iteration
    while np.fabs(T1 - T0) >= tol:
        T0 = T1
        n += 1
        x_list = np.linspace(inte[0], inte[1], 2**n + 1)
        T1 = T0 / 2 + (x_list[1] - x_list[0]) * np.sum(func(x_list[1::2]))

    return (T1, n)


def compound_simpson_formula(inte, func, tol):
    """ Calculate the integral by compound Simpson formula

    Args:
        inte: ndarray, the integrand interval
        func: ndarray, the integrand function
        tol: double, the iteration accurancy

    Returns:
        (S1, n):
            S1: double, the integral value by compound Simpson formula
            n: int, the interation number
    """
    # calculate the initial by Simpson formula
    x_list = np.linspace(inte[0], inte[1], 3)
    S0 = (x_list[1] - x_list[0]) * np.sum(np.array([1, 4, 1]).dot(func(x_list))) / 3 
    # calculate another integral value by compound Simpson iteration formula
    n = 1
    x_list = np.linspace(inte[0], inte[1], 2**(n+1)+1)
    S1 = S0 / 2 + (x_list[1] - x_list[0]) * (4 * np.sum(func(x_list[1::2])) - 2 * np.sum(func(x_list[2::4]))) / 3
    # iteration
    while np.fabs(S1 - S0) >= tol:
        S0 = S1
        n += 1
        x_list = np.linspace(inte[0], inte[1], 2**(n+1)+1)
        S1 = S0 / 2 + (x_list[1] - x_list[0]) * (4 * np.sum(func(x_list[1::2])) - 2 * np.sum(func(x_list[2::4]))) / 3

    return (S1, n)


if __name__=='__main__':
    # interval
    inte = np.array([1e-32, 1])
    # compound trapezoid formula
    value, n = compound_trapezoid_formula(inte, f, 1e-6)
    print(f"The first integral's value is {value:.6f} by compound trapezoid formula after {n} iterations")
    value, n = compound_trapezoid_formula(inte, g, 1e-6)
    print(f"The second integral's value is {value:.6f} by compound trapezoid formula after {n} iterations")
    # compound Simpson formula
    value, n = compound_simpson_formula(inte, f, 1e-6)
    print(f"The first integral's value is {value:.6f} by compound Simpson formula after {n} iterations")
    value, n = compound_simpson_formula(inte, g, 1e-6)
    print(f"The second integral's value is {value:.6f} by compound Simpson formula after {n} iterations")

