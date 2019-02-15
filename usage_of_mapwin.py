#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mapwin as mw

layers = []
laydict = {1:"1.raw", 2:"2.raw", 3:"3.raw", 4:"4.raw", 5:"5.raw"}
num_of_layers = len(laydict)

for i in range(num_of_layers):
    layers.append(mw.Regi())

for i in range(num_of_layers):
    layers[i].load_data(laydict[i + 1])

mw.multiplot(df=layers, scale=10)
mw.multiplot(df=[layer.applycoef(order=1) for layer in layers], scale=10)
mw.multiplot(df=[layer.applycoef(order=3) for layer in layers], scale=10)


