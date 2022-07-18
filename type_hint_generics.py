#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Generic, TypeVar, List

T = TypeVar('T')

# Familiy[User]やFamily[Dog]型になる
class Family(Generic[T]):
    children: List[T]

    def __init__(self, children: List[T]):
        self.children = children


# 関数にも使える
def double_list(li: List[T]) -> List[T]:
    return li * 2
