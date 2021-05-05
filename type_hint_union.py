#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Union

def half(num: int | float) -> float: # Python 3.10
#def half(num: Union[int, float]) -> float: # Python 3.9
    return num / 2.0

if __name__ == "__main__":
    half(10)
