import numpy as np
import matplotlib.pyplot as plt


def f1(x, y):
    """ Bottom boundary
    """
    return 0


def f2(x, y):
    """ Left boundary
    """
    return 0


def f3(x, y):
    """ Right boundary
    """
    return 0


def f4(x, y):
    """ Top boundary
    """
    return 10 * np.sin(np.pi * x)


def save_fig(x, y, U, file_name):
    """ Save the figure of the approximate solution.

    Args: 
        x: ndarray, the split of x interval
        y: ndarray, the split of y interval
        U: ndarray, the value of the coordiantes
        file_name: string, the picture name to be saved
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, U)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title("Approximate solution of Laplace equation by five-points")
    plt.savefig(file_name)


def five_point_difference_scheme(x_inte, y_inte, M, N, func1, func2, func3, func4):
    """ Solve Laplace equation by five point difference scheme.

    Args:
        x_inte: list/ndarray, the boundary of x
        y_inte: list/ndarray, the boundary of y
        M: int, number of endpoints
        N: int, number of endpoints
        func1: function, bottom boundary
        func2: function object, left boundary
        func3: function object, right boundary
        func4: function object, top boundary
    """
    # cofficients matrix
    B = np.diag(4*np.ones(N-1)) + np.diag(-np.ones(N-2), 1) + np.diag(-np.ones(N-2), -1)
    I = - np.eye(N-1)
    A = np.kron(np.diag(np.ones(M-2), -1), I) + np.kron(np.diag(np.ones(M-2), 1), I) + np.kron(np.diag(np.ones(M-1)), B)

    x = np.linspace(x_inte[0], x_inte[1], M+1)
    y = np.linspace(y_inte[0], y_inte[1], N+1)
    # boundary condition
    b = np.zeros((M-1, N-1))
    for i in range(M-1):
        for j in range(N-1):
            if i == 0:
                if j == 0:
                    b[i, j] = func1(x[i], y[j]) + func2(x[i], y[j+1])
                elif j == N-2:
                    b[i, j] = func4(x[i+1], y[j+2])  + func2(x[i], y[j+1])
                else:
                    b[i, j] = func2(x[i], y[j+1])
            elif i == N-2:
                if j == 0:
                    b[i, j] = func1(x[i+1], y[j]) + func3(x[i+2], y[j+1])
                elif j == N-2:
                    b[i, j] = func4(x[i+1], y[j+2]) + func3(x[i+2], y[j+1])
                else:
                    b[i, j] = func3(x[i+2], y[j+1])
            else:
                if j == 0:
                    b[i, j] = func1(x[i+1], y[j])
                elif j == N-2:
                    b[i, j] = func4(x[i+1], y[j+2])
                else:
                    b[i, j] = 0

    U = (np.linalg.inv(A) @ b.T.reshape(-1, 1)).reshape(M-1, N-1)

    # show the approximate solution
    x1 = np.arange(x_inte[0]+(x_inte[1]-x_inte[0])/M, x_inte[1], (x_inte[1]-x_inte[0])/M)
    y1 = np.arange(y_inte[0]+(y_inte[1]-y_inte[0])/N, y_inte[1], (y_inte[1]-y_inte[0])/N)
    save_fig(x1, y1, U, 'figure_five_points.png')


if __name__ == '__main__':
    M = N = 100
    x_inte = y_inte = [0, 1]
    five_point_difference_scheme(x_inte, y_inte, M, N, f1, f2, f3, f4)

