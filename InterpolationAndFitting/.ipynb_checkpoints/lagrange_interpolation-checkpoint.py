import math
import sympy as sp


def lagrange_interpolation(t, y):
    """ Lagrange Interpolation Polinomial

    Args:
        t: list/ndarray, the interpolation points
        y: list/ndarray, the values of the function at every t

    Returns:
        L: symbol object, Lagrange interpolation Polinomial 
    """
    x = sp.Symbol('x')
    # the number of the points
    n = len(t)

    # Lagrange interpolation polinomial 
    L = 0
    for i in range(n):
        # the base function of Lagrange interpolation polinomial
        l = y[i]
        for j in range(n):
            if i == j:
                continue
            else:
                l *= (x - t[j])/(t[i] - t[j])
        L += l

    return sp.simplify(L)


if __name__ == '__main__':
    # the interpolation points(degrees)
    t = [11, 12, 13]
    # the interpolation points(radians)
    t = list(map(math.radians, t))
    y = [0.190809, 0.207912, 0.224951] 
    L = lagrange_interpolation(t, y)
    print(f"The Lagrange interpolation polinomial is L = {L}")
    # calculate the value of sin11.5 by Lagrange interpolation
    x0_deg = 11.5
    x0_rad = math.radians(x0_deg)
    true_value = math.sin(x0_rad)
    x = sp.Symbol('x')
    pre_value = L.subs(x, x0_rad)
    print(f"The predict value of sin{x0_deg} is {pre_value:.7f}")
    print(f"The true value of sin{x0_deg} is {true_value:.7f}")
    print(f"The error is {math.fabs(true_value - pre_value):.7f}")

