#!/usr/bin/env python
#-*- coding: utf-8 -*-

import ctypes


class Pointer:
    def __init__(self, address):
        self._address = address

    def __invert__(self):
        return ctypes.cast(self._address, ctypes.py_object).value

    def __repr__(self):
        return str(self._address)

    def __iand__(self, right):
        self._address = id(right)
        return self
