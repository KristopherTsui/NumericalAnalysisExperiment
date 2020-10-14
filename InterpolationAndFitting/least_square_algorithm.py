import numpy as np
import matplotlib.pyplot as plt


def least_square_algorithm(t, y, n):
    """ Least square algorithm

    Args:
        t: list/ndarray, the list of points
        y: list/ndarray, the list of function value
        n: int, the order of the fitting curve

    Returns:
        c: ndarray, the cofficients of the fitting curve
    """
    # the number of the points
    leng = len(t)
    # the cofficient matrix
    A = np.ones(leng)
    for i in range(n):
        A = np.c_[A, t**(i+1)]
    # the solution of the normal equations
    c = np.linalg.solve(A.T.dot(A), A.T.dot(y))
    
    return c


def calculate_square_error(y, func):
    """ Calculate the square error

    Args:
        y: ndarray, the list of prediction value
        func: ndarray, the list of original value

    Returns:
        sq_err: double, the square error
    """
    return np.sum(np.square(y - func))


def draw_curve(x, y, func, file_name):
    """ Draw the fitting curve

    Args:
        x: ndarray, the data of independent variable
        y: ndarray, the original value
        func: ndarray, the prediction function
        file_name: string, the name of the saved figure file

    """
    fig = plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'ro', label='data set')
    t = np.arange(x[0], x[-1], 0.1)
    plt.plot(t, func(t), 'g-', label='fitting curve')
    plt.title('Least Square Algorithm')
    plt.legend()
    plt.savefig(file_name)    


def linear_fitting():
    """ Fitting experiment 1

    """
    # data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([4, 4.5, 6, 8, 8.5])
    # get the cofficients
    a, b = least_square_algorithm(x, y, 1)
    # define the fitting curve using the cofficients
    f = lambda x: a + b * x
    # get the square error
    print(f"The linear fitting's square error is {calculate_square_error(f(x), y)}")
    # visualization
    draw_curve(x, y, f, 'linear_fitting.png')


def non_linear_fitting():
    """ two order polinomial fitting

    """
    # data
    x = np.array([2, 3, 4, 7, 8, 10, 11, 14, 16, 18, 19])
    y = np.array([106.42, 108.2, 109.5, 110, 109.93, 110.49, 110.59, 110.6, 110.76, 111, 111.2])
    # get the cofficients
    a, b, c = least_square_algorithm(x, y, 2)
    # define the fitting curve
    f = lambda x: a + b * x + c * x**2
    # get the square error
    print(f"The 2-order polinomial fitting's square error is {calculate_square_error(f(x), y)}")
    # visualization
    draw_curve(x, y, f, 'polinomial_fitting.png')

    """ exponential fitting

    """
    # data preprocessing
    t = 1 / x
    z = np.log(y)
    # get the cofficients
    a0, b0 = least_square_algorithm(t, z, 1)
    a1, b1 = np.exp(a0), b0
    # define the fitting curve
    g = lambda x: a1 * np.exp(b1 / x)
    print(f"The exponential fitting's square error is {calculate_square_error(g(x), y)}")
    # visualization
    draw_curve(x, y, g, 'exponential_fitting.png')


if __name__ == '__main__':
    linear_fitting() 
    non_linear_fitting()

