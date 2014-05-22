__author__ = 'cgonzalez'

import numpy as np
import scipy
import scipy.fftpack


def main(filename):

    data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(1, 2))
    data_x = data[:, 1]
    fft = abs(scipy.fftpack.fft(data_x))
    freq = scipy.fftpack.fftfreq(data_x.size, data_x[1]-data_x[0])
