__author__ = 'cgonzalez'

import sys
import numpy as np
import scipy
import scipy.fftpack
import matplotlib.pyplot as plt
from os.path import basename, join

def main(datapath, test):

    filename = "test_{0}s_run{1}.csv".format(test, 1)
    filename = join(datapath, filename)
    data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(1, 2))
    ydata_r1 = data[:, 1]
    xdata_r1 = data[:, 0]
    fft_r1 = abs(scipy.fftpack.fft(ydata_r1))
    fft_r1 = fft_r1[0:len(fft_r1)/2]
    #fft_r1 = 20*scipy.log10(fft_r1[0:len(fft_r1)/2])
    freq_r1 = scipy.fftpack.fftfreq(ydata_r1.size, 1)
    freq_r1 = freq_r1[0:len(freq_r1)/2]

    filename = "test_{0}s_run{1}.csv".format(test, 2)
    filename = join(datapath, filename)
    data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(1, 2))
    ydata_r2 = data[:, 1]
    xdata_r2 = data[:, 0]
    fft_r2 = abs(scipy.fftpack.fft(ydata_r2))
    fft_r2 = fft_r2[0:len(fft_r2)/2]
    #fft_r2 = 20*scipy.log10(fft_r2[0:len(fft_r2)/2])
    freq_r2 = scipy.fftpack.fftfreq(ydata_r2.size, 1)
    freq_r2 = freq_r2[0:len(freq_r2)/2]

    filename = "test_{0}s_run{1}.csv".format(test, 3)
    filename = join(datapath, filename)
    data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(1, 2))
    ydata_r3 = data[:, 1]
    xdata_r3 = data[:, 0]
    fft_r3 = abs(scipy.fftpack.fft(ydata_r3))
    fft_r3 = fft_r3[0:len(fft_r3)/2]
    #fft_r3 = 20*scipy.log10(fft_r3[0:len(fft_r3)/2])
    freq_r3 = scipy.fftpack.fftfreq(ydata_r3.size, 1)
    freq_r3 = freq_r3[0:len(freq_r3)/2]

    # Plot FFT
    ax = plt.subplot(1, 2, 2)
    ax.plot(freq_r1, fft_r1, "-+", label="Run 1")
    ax.plot(freq_r2, fft_r2, "-+", label="Run 2")
    ax.plot(freq_r3, fft_r3, "-+", label="Run 3")

    ax.set_title("Test {}s".format(test))
    ax.set_xlabel("Freq")
    ax.set_ylabel("dB")

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=0)

    # Plot Data
    ax2 = plt.subplot(1, 2, 1)
    ax2.plot(xdata_r1, ydata_r1, "-o", label="Run 1")
    ax2.plot(xdata_r2, ydata_r2, "-o", label="Run 2")
    ax2.plot(xdata_r3, ydata_r3, "-o", label="Run 3")

    ax2.set_title("Test {}s".format(test))
    ax2.set_xlabel("Shear rate")
    ax2.set_ylabel("Shear stress")

    handles, labels = ax2.get_legend_handles_labels()
    ax2.legend(handles, labels, loc=0)

    plt.show()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
