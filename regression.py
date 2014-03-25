import numpy as np

class Regression(object):
    def __init__(self, x, y):
        """
        @param x Array with x values
        @param y Array with y values
        """
        self.x = x
        self.y = y

    def analyze(self, steps=list(range(1, 10, 1))):
        """
        Perform series of regression changing the number of data samples used.

        @param steps List with number of samples to use
        @return X, Y, Z matrices with n_samples/x_data/gradient
        """
        Z = np.zeros((len(self.x)), len(steps))
        X = np.zeros_like(Z)
        Y = np.zeros_like(Z)

        for step in steps:
            subs_x = self.x.sub
            subs_y = self.y.subs
            for sub_x in subs:
