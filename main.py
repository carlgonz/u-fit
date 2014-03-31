import os
import numpy as np
from mayavi.mlab import *
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
    surf(X.T, Y.T, Z, warp_scale="auto")
    show()


if __name__ == "__main__":
    main()