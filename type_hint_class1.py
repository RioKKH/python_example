#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def is_around_30(user: User):
    return user.age >= 27 and user.age <= 30


user = User("Batman", 29)
is_around_30(user)
#is_around_30("xxx")
