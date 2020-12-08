#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from typing import List
from src.utils import bcolors


class DayFive:
    def import_map(self, loc: str) -> List[str]:
        data = open(loc).read()
        maps = data.rstrip().split("\n")
        return maps

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
        print(f"{bcolors.FAIL}Day Five.{bcolors.ENDC}")
        print("The largest seat id is {}".format(str(biggest_seat)))
        print("Your seat id is {}".format(str(your_seat)))
