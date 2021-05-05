#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name: str
    age: int


class Dog(Animal):
    pass


class Tomato:
    pass


animal: Animal = Animal()
dog: Animal = Dog
tomato_is_not_animal: Animal = Tomato()
