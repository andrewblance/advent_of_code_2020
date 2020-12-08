#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from typing import List
from dataclasses import dataclass
from src.utils import bcolors


@dataclass
class password:
    lower: int
    upper: int
    rule: str
    password: str


class DayTwo:
    def import_passwords(self, loc: str) -> List['password']:
        data = open(loc).read()
        stripped = data.rstrip().split("\n")
        clean = [self.regex_clean(x) for x in stripped]
        pw = [password(int(x[0]), int(x[1]), x[2], x[3]) for x in clean]
        return pw

    def regex_clean(self, data: str) -> List[str]:
        """
        got a disgusting string. lets fix it.
        """
        split_data = re.split(r"[, \-:]+", data)
        return split_data

    def password_check(self, data: List['password']) -> int:
        """
        does the password follow the rule?
        """
        real = 0
        for x in data:
            pw = x.password
            rl = x.rule
            occurences = pw.count(rl)
            if (x.upper >= occurences) & (x.lower <= occurences):
                real += 1
        return real

    def password_check_toboggan(self, data: List['password']) -> int:
        """
        well, the original password checker was "wrong"
        this is the one with new rules
        """
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

    def answers(self, data: List['password']):
        correct_pw = self.password_check(data)
        toboggan_pw = self.password_check_toboggan(data)
        print(f"{bcolors.OKGREEN}Day Two.{bcolors.ENDC}")
        print("The number of 'correct' passwords is {}"
              .format(str(correct_pw)))
        print("...well actually, the correct answer is {}"
              .format(str(toboggan_pw)))
