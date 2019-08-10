#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/kakehi/work/git/python_example/mbm')

from mbm_imagelib import Image

import numpy as np
from scipy import optimize
import netpbmfile
import matplotlib.pyplot as plt
from skimage import io, color, measure, draw, img_as_bool


def load(fname):
    img = Image()
    img.load_file(fname)
    img.apply_gaussian_filter()
    img.binarize()
    img.get_property(remove_touching=False)
    return img#, regions

def get_center_minimum_enclosing_circle(img):
    x, y = img.regions[0].weighted_centroid
    r = img.regions[0].major_axis_length / 2.

    def cost(params):
        x, y, r = params
        coords = draw.circle(y, x, r, shape=img.img.shape)
        print(coords)
        template = np.zeros_like(img.bimg)
        template[coords] = 1
        return -np.sum(template == img.bimg)

    x0, y0, r0 = optimize.fmin(cost, (x, y, r))

    f, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3,
                                      figsize=(9, 3.5),sharey=True)
    circle = plt.Circle((x0, y0), r, alpha=0.5)
    ax0.imshow(img.img, cmap='gray')
    ax1.imshow(img.bimg, cmap='gray')
    ax2.imshow(img.img, cmap='gray')
    ax2.add_artist(circle)
    ax2.plot(x0, y0, marker='o', ms=10, color='red')
    plt.show()

def main(fname):
    img = load(fname)
    get_center_minimum_enclosing_circle(img)


if __name__ == '__main__':
    main(sys.argv[1])



