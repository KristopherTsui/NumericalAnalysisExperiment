import math
import numpy as np


def f(x):
    return np.exp(-1*x**2)


def g(x):
    return np.sin(x) / x


def trapezoid_formula(inte, func):
    """ Calculate the integral by trapezoid formula

    Args:
        inte: ndarray, the integrand interval
        func: function object, the integrand function

    Returns:
        double, the integral value by trapezoid formula
    """
    
    return (inte[1] - inte[0]) * np.sum(func(inte)) / 2


def simpson_formula(inte, func):
    """ Calculate the integral by Simpson formula

    Args:
        inte: ndarray, the integrand interval
        func: function object, the integrand function

    Returns:
        double, the integral value by Simpson formula
    """
    # get the nodes
    x_list = np.linspace(inte[0], inte[1], 3)
    # cofficient vector
    C = np.array([1, 4, 1])

    return (inte[1] - inte[0]) * np.sum(C.T.dot(func(x_list))) / sum(C) 


if __name__ == '__main__':
    # integrand interval
    inte = np.array([1e-32, 1])
    # trapezoid formula
    print(f"The value of the first integral by trapezoid formula is {trapezoid_formula(inte, f)}")
    print(f"The value of the second integral by trapezoid formula is {trapezoid_formula(inte, g)}")
    # Simpson formula
    print(f"The value of the first integral by Simpson formula is {simpson_formula(inte, f)}")
    print(f"The value of the second integral by Simpson formula is {simpson_formula(inte, g)}") 

