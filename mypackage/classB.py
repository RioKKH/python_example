#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import classA

class B():

    def __init__(self):
        print("class B")

    def importA(self):
        classA.A()
