#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import NewType

class Car:
    id: int

    def __init__(self):
        self.id = 1

class User:
    id: int

    def __init__(self):
        self.id = 10


if __name__ == "__main__":
    car = Car()
    user = User()

    car.id = user.id

