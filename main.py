import os
import sys
import numpy as np
from mayavi.mlab import surf, show, figure, axes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sys.path.append("src/python/modules")
from regression import *


def list_datafiles(path):
    """
    Return a list of files with experimental data

    @param path Directory to search for files
    @return List with file names
    """
    files = os.listdir(path)
    return [os.path.join(path, f) for f in files if ".csv" in f]


def plot_3d_mayavi(X, Y, Z):
    f = figure(bgcolor=(1, 1, 1))
    surf(X.T, Y.T, Z, figure=f)
    axes(xlabel='N Samples', ylabel='Sample', zlabel='Gradient',
         nb_labels=5, line_width=1)

    show()

def plot_3d_mplot(X, Y, Z, title=""):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(X.T, Y.T, Z, rstride=1, cstride=1, linewidth=0.5, antialiased=True)
    plt.xlabel("N Samples")
    plt.ylabel("Sample")
    plt.title(title)
    # ax.zlabel("Gradient")
    plt.show()

def main():
    test = 11
    test_list = list_datafiles("data/")
    data = np.loadtxt(test_list[test], delimiter=',', skiprows=1, usecols=(0, 1, 2))
    slices = list(range(5, len(data[:, 0]), 1))
    reg = Regression(data[:, 1], data[:, 2])

    Z = reg.analyze(slices)
    X, Y = np.meshgrid(slices, data[:, 0])
    # plot_3d_mayavi(X, Y, Z)
    plot_3d_mplot(X, Y, Z, title=test_list[test])


if __name__ == "__main__":
    main()