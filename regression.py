import numpy as np

class Regression(object):
    def __init__(self, x, y):
        """
        @param x Array with x values
        @param y Array with y values
        """
        self.x = x
        self.y = y
        self.len = len(self.y)

    def __get_slices(self, step):
        """
        Return data samples of len @step
        @param step Sample length
        """
        subs_x = []
        subs_y = []

        for i in range(self.len):
            if i+step < self.len:
                sub_x = self.x[i:i+step]
                sub_y = self.y[i:i+step]
                subs_x.append(sub_x)
                subs_y.append(sub_y)

        return subs_x, subs_y

    def analyze(self, steps=list(range(1, 10, 1))):
        """
        Perform series of regression changing the number of data samples used.

        @param steps List with number of samples to use
        @return Z matrix with gradient(n_samples, x_data)
        """
        Z = np.zeros((len(steps), self.len))

        for i, step in enumerate(steps):
            subs_x, subs_y = self.__get_slices(step)
            for j, (sub_x, sub_y) in enumerate(zip(subs_x, subs_y)):
                a = np.vstack([sub_x, np.ones(len(sub_x))]).T
                m, c = np.linalg.lstsq(a, sub_y)[0]
                Z[i, j] = m

        return Z
