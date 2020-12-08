#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
from src.utils import bcolors


class DayOne:
    def import_expense_report(self, loc: str) -> List[int]:
        data = open(loc).read().split()
        expense = [int(x) for x in data]
        return expense

    def find_two_factors(self, L: List[int]) -> float:
        """
        given a list, find the two nums that sum to 2020
        what is their product?
        """
        list_shift = [2020-x for x in L]
        factors = list(set(L) & set(list_shift))
        product = factors[0] * factors[1]
        return product

    def find_three_factors(self, L: List[int]) -> float:
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

    def answers(self, L: List[int]):
        two_factors = self.find_two_factors(L)
        three_factors = self.find_three_factors(L)
        print(f"{bcolors.OKBLUE}Day One.{bcolors.ENDC}")
        print("The two numbers together are {}".format(str(two_factors)))
        print("The three numbers together are {}".format(str(three_factors)))
