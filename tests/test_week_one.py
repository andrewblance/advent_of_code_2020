#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:58:55 2020

@author: andrewblance
"""

import src.weekone as w1


class TestDaySeven:
    def test_gold_serch(self):
        rules = ["light red bags contain 2 muted yellow bags.",
                 "dark orange bags contain 3 bright white bags.",
                 "bright white bags contain 1 shiny gold bag.",
                 "muted yellow bags contain 2 shiny gold bags.",
                 "shiny gold bags contain 2 vibrant plum bags.",
                 "dark olive bags contain 3 faded blue bags.",
                 "vibrant plum bags contain 5 faded blue bags.",
                 "faded blue bags contain no other bags.",
                 "dotted black bags contain no other bags."]
        D = w1.DaySeven().dict_maker(rules)
        total = w1.DaySeven().gold_recurs(D, "shiny gold")
        assert total == 4

    def test_count_serch(self):
        rules = ["shiny gold bags contain 2 dark red bags.",
                 "dark red bags contain 2 dark orange bags.",
                 "dark orange bags contain 2 dark yellow bags.",
                 "dark yellow bags contain 2 dark green bags.",
                 "dark green bags contain 2 dark blue bags.",
                 "dark blue bags contain 2 dark violet bags.",
                 "dark violet bags contain no other bags."]
        D = w1.DaySeven().dict_maker(rules)
        total = w1.DaySeven().count_recurs(D, "shiny gold")
        assert total == 126


class TestDaySix:
    def test_group_count(self):
        answers = ["abc", "a\nb\nc", "ab\nac", "a\na\naa", "b"]
        total = w1.DaySix().count_uni(answers)
        assert total == 11

    def test_group_int(self):
        answers = ["abc", "a\nb\nc", "ab\nac", "a\na\naa", "b"]
        total = w1.DaySix().count_int(answers)
        assert total == 6


class TestDayFive:
    def test_search(self):
        upper = 127
        lower = 0
        case_1 = w1.DayFive().search(upper, lower, "BFFFBBF")
        case_2 = w1.DayFive().search(upper, lower, "FFFBBBF")
        upper = 7
        case_3 = w1.DayFive().search(upper, lower, "RLL")
        assert (case_1 == 70) & (case_2 == 14) & (case_3 == 4)

    def test_missing(self):
        L = w1.DayThree().import_map("src/data/boaring_passes.txt")
        miss = w1.DayFive().find_missing(L)
        assert miss == 659


class TestDayFour:
    def test_passport_checker(self):
        passports = w1.DayFour().import_passports("tests/passports.txt")
        valid = w1.DayFour().passport_check_one(passports)
        assert valid == 2

    def test_very_passport_checker(self):
        passports = w1.DayFour().import_passports("tests/passports2.txt")
        valid = w1.DayFour().thorough_check_batch(passports)
        assert valid == 4


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
