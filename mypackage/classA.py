#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import classB

class A():

    def __init__(self):
        print("Class A")

    def importB(self):
        classB.B()
