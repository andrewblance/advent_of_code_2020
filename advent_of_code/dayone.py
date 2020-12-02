#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:33:54 2020

@author: andrewblance
"""


import re
from typing import Iterable
from dataclasses import dataclass


def import_expense_report(loc):
    data = open(loc).read().split()
    data = [int(x) for x in data]
    return data


class DayTwo:
    def import_passwords(self, loc):
        data = open(loc).read()
        data = data.rstrip().split("\n")
        data = [self.regex_clean(x) for x in data]
        data = [password(int(x[0]), int(x[1]), x[2], x[3]) for x in data]
        return data

    def regex_clean(self, data: str) -> Iterable[str]:
        split_data = re.split(r"[, \-:]+", data)
        return split_data

    def password_check(self, data: Iterable) -> int:
        real = 0
        for x in data:
            pw = x.password
            rl = x.rule
            occurences = pw.count(rl)
            if (x.upper >= occurences) & (x.lower <= occurences):
                real += 1
        return real

    def password_check_toboggan(self, data: Iterable) -> int:
        real = 0
        for x in data:
            pw = x.password
            rl = x.rule
            upper_char = pw[x.upper - 1]
            lower_char = pw[x.lower - 1]
            if (upper_char == rl) & (lower_char == rl):
                continue
            if (upper_char == rl) or (lower_char == rl):
                real += 1
        return real

    def answers(self, data):
        correct_pw = self.password_check(data)
        toboggan_pw = self.password_check_toboggan(data)
        print("The number of 'correct' passwords is: " + str(correct_pw) +
              "...well actually, the correct answer is " + str(toboggan_pw))


@dataclass
class password:
    lower: int
    upper: int
    rule: str
    password: str


class DayOne:
    def find_two_factors(self, L: Iterable) -> float:
        """
        given a list, find the two nums that sum to 2020
        what is their product?
        """
        list_shift = [2020-x for x in L]
        factors = list(set(L) & set(list_shift))
        product = factors[0] * factors[1]
        return product

    def find_three_factors(self, L: Iterable) -> float:
        """
        given a list, find the three nums that sum to 2020
        what is their product?
        """
        list_shift = [2020-x for x in L]
        twice_shift = [[x-y for y in L] for x in list_shift]
        flat_list = [item for sublist in twice_shift for item in sublist]
        factors = list(set(flat_list) & set(L))
        product = factors[0] * factors[1] * factors[2]
        return product

    def answers(self, L):
        two_factors = self.find_two_factors(L)
        three_factors = self.find_three_factors(L)
        print("The answers for day one are: " +
              str(two_factors) + " and " + str(three_factors))


def main():
    expenses = import_expense_report("advent_of_code/data/input.txt")
    DayOne().answers(expenses)

    passwords = DayTwo().import_passwords("advent_of_code/data/passwords.txt")
    DayTwo().answers(passwords)


if __name__ == '__main__':
    main()
