#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def make_data():
    #A = np.array([[3,2], [2,4], [-1,1]])
    A = np.array([[3, 4], [4, 14]])
    b = np.array([7, 13])

    return A, b

def print_coef(A, b):
    print(A)
    print(np.shape(A))
    print(b)
    print(np.shape(b))



def svd(A, b):
    u, s, v = np.linalg.svd(A)
    print(u)
    print(s)
    print(v)
    return u, s, v




