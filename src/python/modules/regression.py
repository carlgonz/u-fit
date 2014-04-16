import numpy as np
from scipy import stats

class Regression(object):
    def __init__(self, x, y):
        """
        @param x Array with x values
        @param y Array with y values
        """
        self.x = x
        self.y = y
        self.len = len(self.x)

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

    def __regression(self, x, y):
        # a = np.vstack([x, np.ones(len(x))]).T
        # [m, c], rr = np.linalg.lstsq(a, y)[0]

        m, c, r, p, std = stats.linregress(x,y)
        return m, c, r**2

    def analyze(self, steps=list(range(1, 10, 1))):
        """
        Perform series of regression changing the number of data samples used.

        @param steps List with number of samples to use
        @return Z matrix with gradient(n_samples, x_data)
        """
        Z = np.ones((len(steps), self.len))*np.nan

        for i, step in enumerate(steps):
            subs_x, subs_y = self.__get_slices(step)
            for j, (sub_x, sub_y) in enumerate(zip(subs_x, subs_y)):
                m, c, r = self.__regression(sub_x, sub_y)
                Z[i, j] = m

        return Z

    def regression(self, percentil):
        step = int(self.len*percentil/100)
        subs_x, subs_y = self.__get_slices(step)
        list_m = []
        list_c = []
        list_r = []

        for (sub_x, sub_y) in zip(subs_x, subs_y):
            m, c, r = self.__regression(sub_x, sub_y)
            list_m.append(m)
            list_c.append(c)
            list_r.append(r)

        i = np.argmin(list_m)
        c_value = list_c[i]
        m_value = list_m[i]
        r_value = list_r[i]

        return [m_value, c_value, r_value, i, step]

