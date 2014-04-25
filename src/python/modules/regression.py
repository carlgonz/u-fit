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
        self.list_m = []
        self.list_c = []
        self.list_r = []
        self.list_dr = []
        self.list_i = []
        self.len = len(self.x)
        self.last = "none"
        self.alpha = None
        self.steps = None
        self.window = None

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

    def analyze(self, steps=list(range(2, 10, 1))):
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

    def optimization(self, alpha=0.5, steps=list(range(2, 10, 1))):
        if (self.last != "opt") or (self.steps != steps):
            self.steps = steps
            self.alpha = alpha
            self.list_m = []
            self.list_c = []
            self.list_r = []
            self.list_dr = []
            self.list_i = []

            for i, step in enumerate(steps):
                _list_r = []
                subs_x, subs_y = self.__get_slices(step)

                for j, (sub_x, sub_y) in enumerate(zip(subs_x, subs_y)):
                    m, c, r = self.__regression(sub_x, sub_y)
                    self.list_m.append(m)
                    self.list_c.append(c)
                    self.list_r.append(r)
                    self.list_i.append((j, step))
                    _list_r.append(r)

                self.list_dr.extend(np.gradient(_list_r).tolist())

            self.list_dr = np.absolute(np.array(self.list_dr))
            self.list_m = np.where(np.array(self.list_m) >= 0,
                                   np.array(self.list_m), 10**10)

            self.last = "opt"

        f_obj = alpha*self.list_m + (1-alpha)*self.list_dr
        i_op = np.argmin(f_obj)
        # print(len(f_obj), i_op)
        m_op = self.list_m[i_op]
        c_op = self.list_c[i_op]
        r_op = self.list_r[i_op]
        i, step = self.list_i[i_op]
        # f_op = self.f_obj[i_op]

        # print("Params:", i_op, f_op, m_op, c_op, r_op, list_dr[i_op])
        # print("Obj: ", len(f_obj.tolist()), f_obj.tolist())
        # print("R : ", len(list_r), list_r)
        # print("dR: ", len(list_dr), list_dr)
        # print("M : ", len(list_m), list_m)
        #
        # X = np.vstack((f_obj.tolist(), list_m, list_r, list_dr)).T
        # np.savetxt("fit.csv", X, delimiter=',')

        return [m_op, c_op, r_op, i, step]

    def regression(self, percentil, alpha=1.0):
        if (self.last != "reg") or (self.window != percentil):
            self.window = percentil
            self.alpha = alpha

            step = int(self.len*percentil/100)
            subs_x, subs_y = self.__get_slices(step)
            self.list_m = []
            self.list_c = []
            self.list_r = []

            for (sub_x, sub_y) in zip(subs_x, subs_y):
                m, c, r = self.__regression(sub_x, sub_y)
                self.list_m.append(m)
                self.list_c.append(c)
                self.list_r.append(r)

            self.list_dr = np.gradient(self.list_r)
            self.list_dr = np.absolute(np.array(self.list_dr))
            self.list_m = np.where(np.array(self.list_m) >= 0,
                                   np.array(self.list_m), 10**3)

            self.last = "reg"

        f_obj = alpha*self.list_m + (1-alpha)*self.list_dr
        i = np.argmin(f_obj)
        c_value = self.list_c[i]
        m_value = self.list_m[i]
        r_value = self.list_r[i]
        step = int(self.len*self.window/100)

        return [m_value, c_value, r_value, i, step]

