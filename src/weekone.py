#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from typing import List, Tuple, Dict
from dataclasses import dataclass
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
        print(f"{bcolors.UNDERLINE}Day Six.{bcolors.ENDC}")
        print("The number of bags is {}"
              .format(str(total)))
        print("The number of bags i have to carry is {}"
              .format(str(beeg_total)))


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


class DayFive:
    def search(self, upper: int, lower: int,
               row: str) -> int:
        """
        basically a binary nums?
        """
        for x in row:
            df = math.ceil((upper-lower)/2)
            split = lower + df
            if x in ["F", "L"]:
                lower = lower
                upper = split
            elif x in ["B", "R"]:
                lower = split
                upper = upper
        return lower

    def pass_parser(self, id: str) -> int:
        """
        turn id into int
        BFFFBBFRRR -> 567
        """
        row = id[:7]
        col = id[-3:]
        seat_id = self.search(127, 0, row) * 8 + self.search(7, 0, col)
        return seat_id

    def pass_checker(self, ids: List[str]) -> int:
        biggest_seat = 0
        for x in ids:
            seat_id = self.pass_parser(x)
            if seat_id > biggest_seat:
                biggest_seat = seat_id
        return biggest_seat

    def find_missing(self, ids: List[str]) -> int:
        """
        thats the missing one in list
        """
        seats = [self.pass_parser(x) for x in ids]
        sorted_list = sorted(seats)
        missing = [x for x in range(sorted_list[0], sorted_list[-1]+1)
                   if x not in sorted_list]
        return missing[0]

    def answers(self, ids: List[str]) -> None:
        biggest_seat = self.pass_checker(ids)
        your_seat = self.find_missing(ids)
        print(f"{bcolors.FAIL}Day Four.{bcolors.ENDC}")
        print("The largest seat id is {}".format(str(biggest_seat)))
        print("Your seat id is {}".format(str(your_seat)))


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


@dataclass
class password:
    lower: int
    upper: int
    rule: str
    password: str


class DayThree:
    """
    Advent of Code Day Three

    The challenge is to traverse a map. The map is given as a list
    of strings, containing "." and "#". The maps loops back on itself. Ie,
    once we get to the end of a string we start back at the
    beginning of it again
    """
    def import_map(self, loc: str) -> List[str]:
        data = open(loc).read()
        maps = data.rstrip().split("\n")
        return maps

    def stepper(self, x_init: int, y_init: int,
                x_step: int, y_step: int,
                map_width: int) -> Tuple[int, int]:
        """
        Given a set of coordinates,
        move your way across a repeating gridspace

        Parameters
        ----------
        x_init:
            initial x coord
        y_init:
            initial y coord
        x_step:
            step size in x. Will move you from maps[0][0] to maps[1][0]
        y_step:
            step size in x. Will move you from maps[0][0] to maps[0][1]
        map_width:
            you map has a width, this is it. Used to correct y
            as we loop around the map

        Returns
        -------
        [x_new, y_new]:
            our new coordinate set

        Examples
        --------
        >>> x, y = stepper(0, 0, 1, 3, 10)
        >>> print(x, y)
            (1, 3)

        """
        x_new = x_init + x_step
        y_new = (y_init + y_step) % map_width
        return (x_new, y_new)

    def traverse(self, x: int, y: int,
                 x_step: int, y_step: int,
                 maps: List[str]) -> int:
        """
        Given a set of coordinates, and steps,
        traverse the map and count all the trees you hit

        Parameters
        ----------
        x_init:
            initial x coord
        y_init:
            initial y coord
        x_step:
            step size in x. Will move you from maps[0][0] to maps[1][0]
        y_step:
            step size in x. Will move you from maps[0][0] to maps[0][1]
        maps:
            this is your map, its a list of strings

        Returns
        -------
        trees:
            number of trees youve smashed into

        Examples
        --------
        >>> map = DayThree().import_map("src/data/map.txt")
        >>> trees = stepper(0, 0, 1, 3, maps)
        >>> print(trees)
            225

        """
        depth = len(maps)
        trees = 0
        while x < depth:
            if maps[x][y] == "#":
                trees += 1
            x, y = self.stepper(x, y, x_step, y_step, len(maps[0]))
        return trees

    def traverse_multple(self, coords: List[Tuple[int, int]],
                         maps: List[str]) -> int:
        """
        You have your maps, but also a set of maths you want
        to traverse.

        hmm... I wonder if we found all the trees we'd hit in each path
        then multiply them what we would get????

        Parameters
        ----------
        coords:
            A list of all the paths you will take
        maps:
            this is your map

        Returns
        -------
        trees:
            number of trees youve smashed into

        Examples
        --------
        >>> map = DayThree().import_map("src/data/map.txt")
        >>> slope_set = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
        >>> product_trees = self.traverse_multple(slope_set, maps)
        >>> print(product_trees)
            1115775000

        """
        trees = 1
        for x in coords:
            _tree = self.traverse(0, 0, x[0], x[1], maps)
            trees *= _tree
        return trees

    def answers(self, maps: List[str]):
        num_trees = self.traverse(0, 0, 1, 3, maps)
        slope_set = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
        product_trees = self.traverse_multple(slope_set, maps)
        print(f"{bcolors.WARNING}Day Three.{bcolors.ENDC}")
        print("The number of trees we see is {}".format(str(num_trees)))
        print("The product of all the slopes is {}".format(str(product_trees)))


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


def main():
    expenses = DayOne().import_expense_report("src/data/input.txt")
    DayOne().answers(expenses)

    passwords = DayTwo().import_passwords("src/data/passwords.txt")
    DayTwo().answers(passwords)

    maps = DayThree().import_map("src/data/map.txt")
    DayThree().answers(maps)

    passports = DayFour().import_passports("src/data/passports.txt")
    DayFour().answers(passports)

    boarding = DayThree().import_map("src/data/boaring_passes.txt")
    DayFive().answers(boarding)

    answers = DaySix().import_answers("src/data/questions.txt")
    DaySix().answers(answers)

    bags = DaySeven().import_bags("src/data/bags.txt")
    DaySeven().answers(bags)


if __name__ == '__main__':
    main()
