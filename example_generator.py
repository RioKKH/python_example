#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
紙を何回折ると月まで行けるかな？
紙の厚さを0.1mmとして、1回折ると0.2mm, 2回折ると0.4mmになります。
地球と月の距離は384400kmとします。
"""

def total_thickness(thickness=0.1E-3):
    i = 0
    while True:
        yield thickness * 2 ** i
        i += 1

def main():
    thickness = total_thickness()
    limit = 384400 * 1E3 # [km] --> [m]
    for i, thick in enumerate(thickness):
        if thick < limit:
            print("{0:d} : {1:.8f}".format(i, thick))
        elif thick >= limit:
            print("{0:d} : {1:.8f}".format(i, thick))
            break


if __name__ == '__main__':
    main()
        

