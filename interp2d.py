#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

def main():

    x = np.arange(-5.01, 5.01, 0.25)
    y = np.arange(-5.01, 5.01, 0.25)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(xx**2 + yy**2)
    f_linear = interpolate.interp2d(x, y, z, kind='linear')
    f_cubic  = interpolate.interp2d(x, y, z, kind='cubic')

    xnew = np.arange(-5.01, 5.01, 1e-2)
    ynew = np.arange(-5.01, 5.01, 1e-2)
    znew_linear = f_linear(xnew, ynew)
    znew_cubic  = f_cubic(xnew, ynew)

    print(np.shape(znew_linear), np.shape(znew_cubic))
    plt.plot(x,    z[0, :],           'ro-',
             xnew, znew_linear[0, :], 'b-',
             xnew, znew_cubic[0, :],  'g--')
    plt.show()

    return z, znew_linear, znew_cubic

if __name__ == '__main__':
    main()

