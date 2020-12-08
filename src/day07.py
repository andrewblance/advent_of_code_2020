#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Dict
from src.utils import bcolors


class DaySeven:
    def import_bags(self, loc: str) -> List[str]:
        data = open(loc).read().split("\n")
        return data

    def dict_maker(self, data: List[str]) -> Dict:
        rules = {}
        for x in data:
            if x == "":
                continue
            bag_split = x.split(" contain ")
            bag = bag_split[0].replace(" bags", "")
            rule = bag_split[1].strip('.').split(', ')
            rules[bag] = [x.replace(' bags', '')
                          .replace(' bag', '') for x in rule]
        return rules

    def gold_recurs(self, rules: Dict, search: str) -> int:
        total = 0
        for x in list(rules):
            if any(search in bag for bag in rules[x]) and not\
               any("flag" in bag for bag in rules[x]):
                rules[x].append("flag")
                total += 1 + self.gold_recurs(rules, x)
        return total

    def count_recurs(self, rules: Dict, search: str) -> int:
        total = 0
        for x in rules[search]:
            if x != "no other":
                total += int(x[0]) * (1 + self.count_recurs(rules, x[2:]))
        return total

    def answers(self, L: List[str]) -> None:
        D = self.dict_maker(L)
        total = self.gold_recurs(D, "shiny gold")
        beeg_total = self.count_recurs(D, "shiny gold")
        print(f"{bcolors.UNDERLINE}Day Seven.{bcolors.ENDC}")
        print("The number of bags is {}"
              .format(str(total)))
        print("The number of bags i have to carry is {}"
              .format(str(beeg_total)))
