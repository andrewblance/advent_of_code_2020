#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from typing import List, Tuple
from dataclasses import dataclass


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


@dataclass
class password:
    lower: int
    upper: int
    rule: str
    password: str


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


if __name__ == '__main__':
    main()
