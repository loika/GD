import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import meshgrid


def graph2D(X, U):
    plt.plot(X, U, color="seagreen")
    plt.show()
    return None


def graph3D(X, U):
    fig = plt.figure()

    ax = Axes3D(fig)

    xi, xj = meshgrid(X, X)

    y = U.reshape((X.shape[0], X.shape[0]))

    ax.plot_surface(xi, xj, y, cmap="ocean")

    plt.show()
    return None


def graph(X, U, string):
    if string == "2D":
        graph2D(X, U)
    elif string == "3D":
        graph3D(X, U)
    else:
        print("string is not define")
        exit()
