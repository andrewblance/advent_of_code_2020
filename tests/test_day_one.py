#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:58:55 2020

@author: andrewblance
"""

from advent_of_code.dayone import DayOne


class TestDayOne:
    def test_two_factors(self):
        L = [1, 5, 20000, 1009, 1011, 2]
        factors = DayOne().find_two_factors(L)
        assert factors == 1020099
