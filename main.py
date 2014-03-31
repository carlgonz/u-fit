import os
import numpy as np
from mayavi.mlab import surf, show, figure, axes
from regression import *


def list_datafiles(path):
    """
    Return a list of files with experimental data

    @param path Directory to search for files
    @return List with file names
    """
    files = os.listdir(path)
    return [os.path.join(path, f) for f in files if ".csv" in f]


def main():
    test = list_datafiles("data/")
    slices = list(range(10, 50))
    data = np.loadtxt(test[5], delimiter=',', skiprows=1, usecols=(1, 2))
    reg = Regression(data[:, 0], data[:, 1])

    Z = reg.analyze(slices)
    X, Y = np.meshgrid(slices, data[:, 0])

    f = figure(bgcolor=(1, 1, 1))
    surf(X.T, Y.T, Z, warp_scale="auto", figure=f)
    axes(xlabel='Slices', ylabel='Shear rate', zlabel='Gradient', nb_labels=5)
    show()


if __name__ == "__main__":
    main()