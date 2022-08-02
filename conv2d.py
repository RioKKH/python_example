#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from scipy import misc


def test_con2d():
    ascent = misc.ascent()
    scharr = np.array([[ -3 -3j, 0 -10j,  +3 -3j],
                       [-10 +0j, 0 + 0j, +10 +0j],
                       [ -3 +3j, 0 +10j,  +3 +3j]]) 

    xgrad = np.array([[ +0.0 + 0j, 0 + 0j, +0.0 + 0j],
                      [ -0.5 + 0j, 0 + 0j, +0.5 + 0j],
                      [ +0.0 + 0j, 0 + 0j, +0.0 + 0j]])

    #grad = signal.convolve2d(ascent, scharr, boundary='symm', mode='same')
    grad = signal.convolve2d(ascent, xgrad, boundary='symm', mode='same')

    fig, (ax_orig, ax_mag, ax_ang) = plt.subplots(3, 1, figsize=(6, 15))

    ax_orig.imshow(ascent, cmap='gray')
    ax_orig.set_title('Original')
    ax_orig.set_axis_off()
    
    ax_mag.imshow(np.absolute(grad), cmap='gray')
    ax_mag.set_title('Gradient magnitude')
    ax_mag.set_axis_off()

    ax_ang.imshow(np.angle(grad), cmap='hsv')
    ax_ang.set_title('Gradient orientation')
    ax_ang.set_axis_off()

    fig.show()

    return grad


def main():
    test_con2d()


if __name__ == '__main__':
    main()

