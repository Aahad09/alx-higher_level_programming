#!/usr/bin/python3
"""Prints numbers from 0 to 98 in decimal and hexadecimal"""
i = 0
while i <= 98:
    print("{0:d} = {0:#x}".format(i))
    i += 1
