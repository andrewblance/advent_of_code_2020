#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:58:55 2020

@author: andrewblance
"""

import advent_of_code.dayone as one

class TestDayOne:
    def test_one_adder_actually_adds(self):
        x = 1
        y = 2
        assert one.adder(x,y) == 6
