import math


def dichotomy(inte, func, tol=1e-9):
    """ Solve non-linear equation by dichotomy.

    Args:
        inte: list/ndarry, the interval with zero
        func: function object, the equation to be solved
        tol: double, the iteration accuracy

    Returns:
        info_dict: dictionary, containing the endpoints of the inteval, the value of midpoint
                   and the function value of the midpoint
        x: double, root of the quation
    """
    # the endpoints of the interval
    a, b = inte

    # the number of the iteration
    N = math.ceil(math.log2((b - a)/tol))

    # first iteration
    n = 1
    x = (a + b)/2
    # iteration information
    info_dict = {n: [a, b, x, func(x)]}

    # iteration
    while func(x) != 0 and n < N:
        n += 1

        if func(a) * func(x) < 0:
            b = x
        else:
            a = x

        x = (a + b)/2
        info_dict[n] = [a, b, x, func(x)]

    return info_dict, x


def f(x):
    return x**3 + x**2 - 3*x - 3


if __name__ == '__main__':
    # Find the root of the equation f(x)=0 around 1.5 by dichotomy
    # the interval with zero is [1, 2]
    info_dict, x = dichotomy([1,2], f, 1e-6)
    for key, value in info_dict.items():
        print(f"{key}\t[{value[0]:.7f}, {value[1]:.7f}]\t{value[2]:.7f}\t{value[3]:.7f}")
    print(f"The root of the equation is {x:.7f}.")

