#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def test():

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [-0.5, 0.0, 0.5]

    """
    (a \times v)_{n} = \sum_{-\inf}^{+\inf}a_{m}v_{n-m}
    コンボリューションは上式で定義されているので、
    bを逆にしないとこちらが想定した結果とならない
    """
    grad_full  = np.convolve(a, b[::-1], 'full')
    grad_same  = np.convolve(a, b[::-1], 'same')
    grad_valid = np.convolve(a, b[::-1], 'valid')

    print(grad_full)
    print(grad_same)
    print(grad_valid)


if __name__ == '__main__':
    test()

