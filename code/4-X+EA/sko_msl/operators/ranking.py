import numpy as np


def ranking(self):
    self.FitV = -self.Y


def ranking_linear(self):
    '''
    For more details see [Baker1985]_.

    :param self:
    :return:

    .. [Baker1985] Baker J E, "Adaptive selection methods for genetic
    algorithms, 1985.
    '''
    self.FitV = np.argsort(np.argsort(-self.Y))
    return self.FitV
