import numpy as np


def f(x):
    return np.exp(-1*x**2)


def g(x):
    return np.sin(x) / x


def romberg_algorithm(inte, func, tol, Max_iter=10):
    """ Calculate the integral by Romberg Algorithm

    Args:
        inte: ndarray, the integrand interval
        func: function boject, the integrand function
        tol: double, the interation accurancy
        Max_iter: int, the maximum number of iterations

    Returns:
        (T[-1], m):
            T[-1]: double, the integral value by Romberg algorithm
            m: the number of iterations
    """
    # initial values 
    m = 0
    T = [(inte[1] - inte[0]) * np.sum(func(inte)) / 2]
    for i in range(1, Max_iter+1):
        x_list = np.linspace(inte[0], inte[1], 2**i+1)
        T.append(T[i-1]/2 + (x_list[1] - x_list[0]) * np.sum(func(x_list[1::2])))
    T = np.array(T)

    # iteration
    m += 1
    S = (4 * T[1:] - T[:-1]) / (4 - 1)
    
    # mark whether getting the given iteration accurancy
    flag = 1
    while np.fabs(S[-1] - T[-1] >= tol):
        if m == Max_iter:
            flag = 0
            break
        else:
            m += 1
            T = S
            S = (4**m * T[1:] - T[:-1]) / (4**m - 1)
    
    if flag:
        return (T[-1], m)
    else:
        reutnr (nan, Max_iter)


if __name__ == '__main__':
    # interval
    inte = np.array([1e-32, 1])
    # the first integral
    value, n = romberg_algorithm(inte, f, 1e-6)
    print(f"The first integral's value is {value:.6f} by Romberg algorithm after {n} iterations")
    # the second integral
    value, n = romberg_algorithm(inte, g, 1e-6)
    print(f"The second integral's value is {value:.6f} by Romberg algorithm after {n} iterations")

