import math


def dichotomy(intev, func, tol):
    """ Solve non-linear equation by dichotomy

    Args:
        intev: list/ndarry, the inteval with zero
        func: the equation to be solved
        tol: double, the iteration accurancy

    Returns:
        info_dict: dictionary, contains the endpoints of the inteval, the value of midpoint
        and the function value of the midpoint
    """
    # the endpoints of the inteval
    a, b = intev
    # the number of the iteration
    N = math.ceil(math.log2((b - a)/tol))
    x = (a + b)/2
    # begin iteration
    n = 1

    info_dict = {}
    while func(x) != 0 and n < N:
        info_dict[n] = [a, b, x, func(x)]

        if func(a)*func(x) < 0:
            b = x
        else:
            a = x

        x = (a + b)/2
        n += 1

    return info_dict


def f(x):
    """ the equation to be solved
    
    Args:
        x: double, independent variable

    Returns:
        y: double, the value of the function at x
    """
    y = x**3 + x**2 - 3*x - 3
    return y


if __name__ == '__main__':
    # Find the root of the equation f(x)=0 around 1.5 by dichotomy
    info_dict = dichotomy(intev=[1,2], func=f, tol=1e-6)
    for key, value in info_dict.items():
        print(f"{key}\t[{value[0]:.7f}, {value[1]:.7f}]\t{value[2]:.7f}\t{value[3]:.7f}")

