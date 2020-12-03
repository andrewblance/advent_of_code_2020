#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:58:55 2020

@author: andrewblance
"""

import src.weekone as w1


class TestDayThree:
    def test_stepper(self):
        x_init = 4
        y_init = 10
        x_step = 1
        y_step = 5
        map_width = 11
        coords = w1.DayThree().stepper(x_init, y_init,
                                       x_step, y_step, map_width)
        assert (coords[0] == 5) & (coords[1] == 4)

    def test_traverse(self):
        maps = ['....#', '..#..', '....#', '.#...']
        x = 0
        y = 0
        x_step = 1
        y_step = 2
        trees = w1.DayThree().traverse(x, y, x_step, y_step, maps)
        assert trees == 3


class TestDayOne:
    def test_two_factors(self):
        L = [1, 5, 20000, 1009, 1011, 2]
        factors = w1.DayOne().find_two_factors(L)
        assert factors == 1020099

    def test_three_factors(self):
        L = [1, 5, 20000, 1009, 1010]
        factors = w1.DayOne().find_three_factors(L)
        assert factors == 1019090


class TestDayTwo:
    def test_regex(self):
        L = '1-44 d: asdwer'
        bits = w1.DayTwo().regex_clean(L)
        assert (bits[0] == "1") & \
               (bits[1] == "44") & \
               (bits[2] == "d") & \
               (bits[3] == "asdwer")

    def test_password_check(self):
        L = [w1.password(1, 10, "a", "aadd"), w1.password(5, 6, "c", "cca")]
        bits = w1.DayTwo().password_check(L)
        assert bits == 1

    def test_toboggan_password_check(self):
        L = [w1.password(1, 4, "a", "aadd"), w1.password(1, 2, "c", "cca")]
        bits = w1.DayTwo().password_check_toboggan(L)
        assert bits == 1
