import numpy as np


def simpson_formula(inte, func):
    """ Calculate integral of function func on interval [inte[0], inte[1]].

    Args:
        inte: list/ndarray, the intergration interval
        func: function object, the intergrand

    Returns:
        double, the integral value
    """
    x_lst = np.linspace(inte[0], inte[1], 3)
    # Simpson integral formula cofficients
    C = np.array([1, 4, 1])
    return (inte[1] - inte[0]) * np.sum(C @ func(x_lst)) / np.sum(C)


def adaptive_Simpson_formula(inte, func, tol=1e-9):
    """ Calculate integral of function func on interval[inte[0], inte[1]] with accuracy tol.

    Args:
        inte: list/ndarray, the intergration interval
        func: function, intergrand
        tol: double, accuracy of the integral value

    Returns:
        double, integral value
    """
    # Simpson formula
    S1 = simpson_formula(inte, func)
    S2 = simpson_formula([inte[0], sum(inte)/2], func)
    S3 = simpson_formula([sum(inte)/2, inte[1]], func)

    if np.abs(S1 - S2 - S3) >= 10 * tol:
        S2 = adaptive_Simpson_formula([inte[0], sum(inte)/2], func, 5 * tol)
        S3 = adaptive_Simpson_formula([sum(inte)/2, inte[1]], func, 5 * tol)

    return S2 + S3


def f(x):
    return np.exp(-1 * x**2)


def g(x):
    return np.sin(x) / x


if __name__ == '__main__':
    # integration interval
    inte = [1e-32, 1]
    # adaptive Simpson formula
    x1 = adaptive_Simpson_formula(inte, f)
    x2 = adaptive_Simpson_formula(inte, g)
    print(f"The first integral' value is {x1:.7f} by adaptive Simpson formula.")
    print(f"The second integral's value is {x2:.7f} by adaptive Simpson formula.")

