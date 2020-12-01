#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:33:54 2020

@author: andrewblance
"""


def import_expense_report(loc):
    data = open(loc).read().split()
    data = [int(x) for x in data]
    return data


class DayOne:
    def find_two_factors(self, L):
        """
        given a list, find the two nums that sum to 2020
        what is their product?
        """
        list_shift = [2020-x for x in L]
        factors = list(set(L) & set(list_shift))
        product = factors[0] * factors[1]
        return product

    def find_three_factors(self, L):
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
    data = import_expense_report("advent_of_code/data/input.txt")
    DayOne().answers(data)


if __name__ == '__main__':
    main()
