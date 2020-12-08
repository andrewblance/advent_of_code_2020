#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from typing import List, Dict
from src.utils import bcolors


class Passport:
    def __init__(self, byr, iyr, eyr,
                 hgt, hcl, ecl,
                 pid, cid=0) -> None:
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def byr(self) -> int:
        return self._byr

    @byr.setter
    def byr(self, value) -> None:
        if int(value) < 1920 or int(value) > 2002:
            raise Exception("Birth year must be between 1920 and 2002")
        self._byr = int(value)

    @property
    def iyr(self) -> int:
        return self._iyr

    @iyr.setter
    def iyr(self, value) -> None:
        if int(value) < 2010 or int(value) > 2020:
            raise Exception("Issue year must be between 2010 and 2020")
        self._iyr = int(value)

    @property
    def eyr(self) -> int:
        return self._eyr

    @eyr.setter
    def eyr(self, value) -> None:
        if int(value) < 2020 or int(value) > 2030:
            raise Exception("expiration must be between 2020 and 2030 ")
        self._eyr = int(value)

    @property
    def hgt(self) -> str:
        return self._hgt

    @hgt.setter
    def hgt(self, value) -> None:
        height = int(''.join(filter(str.isdigit, value)))
        in_cm = str(''.join(filter(str.isalpha, value)))
        if in_cm == "cm":
            if (height < 150) or (height > 193):
                raise Exception("height must be between 150cm and 193cm")
        elif in_cm == "in":
            if (height < 59) or (height > 76):
                raise Exception("height must be between 59in and 76in")
        elif in_cm not in ["cm", "in"]:
            raise Exception("You have to specify in or cm")
        self._hgt = value

    @property
    def hcl(self) -> str:
        return self._hcl

    @hcl.setter
    def hcl(self, value) -> None:
        if (len(value) != 7) or (value[0] != "#"):
            raise Exception("password is wrong length/ doesnt start with # ")
        if not re.match("^[A-Fa-f0-9_-]*$", value[-6:]):
            raise Exception("password contains more than letters+numbers")
        self._hcl = value

    @property
    def ecl(self) -> str:
        return self._ecl

    @ecl.setter
    def ecl(self, value) -> None:
        eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value not in eye_colours:
            raise Exception("not a appropriate eye colour")
        self._ecl = value

    @property
    def pid(self) -> int:
        return self._pid

    @pid.setter
    def pid(self, value) -> None:
        if len(str(value)) != 9:
            raise Exception("wrong amount of nums in pid")
        self._pid = int(value)


class DayFour:
    def import_passports(self, loc: str) -> List[Dict]:
        d = []
        data = open(loc).read().split("\n\n")
        for x in data:
            _d = {}  # type: Dict
            pp = x.split()
            for p in pp:
                key, val = p.split(":")
                _d[key] = val
            d.append(_d)
        return d

    def passport_check_one(self, passports: List[Dict]) -> int:
        valid = 0
        requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for p in passports:
            if all(a in list(p.keys()) for a in requirements):
                valid += 1
        return valid

    def thorough_check_batch(self, passports: List[Dict]) -> int:
        valid = 0
        for x in passports:
            try:
                Passport(**x)
                valid += 1
            except Exception:
                continue
        return valid

    def answers(self, pps: List[Dict]):
        num_valid = self.passport_check_one(pps)
        very_valid = self.thorough_check_batch(pps)
        print(f"{bcolors.OKCYAN}Day Four.{bcolors.ENDC}")
        print("The number of valid passports if {}".format(str(num_valid)))
        print("The number of very valid passports if {}"
              .format(str(very_valid)))
