#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List
from src.utils import bcolors


class DaySix:
    def import_answers(self, loc: str) -> List[str]:
        data = open(loc).read().split("\n\n")
        return data

    def count_uni(self, questions: List[str]) -> int:
        total = 0
        for x in questions:
            split = x.split("\n")
            str_list = list(filter(None, split))
            joint = [set(t) for t in str_list]
            value = set.union(*joint)
            total += len(value)
        return total

    def count_int(self, questions: List[str]) -> int:
        total = 0
        for x in questions:
            split = x.split("\n")
            str_list = list(filter(None, split))
            sets = [set(t) for t in str_list]
            intersect = set.intersection(*sets)
            total += len(intersect)
        return total

    def answers(self, L: List[str]) -> None:
        total = self.count_uni(L)
        inter = self.count_int(L)
        print(f"{bcolors.BOLD}Day Six.{bcolors.ENDC}")
        print("The combined number of unique answers is {}"
              .format(str(total)))
        print("The combined number of intersected answers is {}"
              .format(str(inter)))
