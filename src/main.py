#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import src.day01 as d1
import src.day02 as d2
import src.day03 as d3
import src.day04 as d4
import src.day05 as d5
import src.day06 as d6
import src.day07 as d7
import src.day08 as d8


def main():
    expenses = d1.DayOne().import_expense_report("src/data/input.txt")
    d1.DayOne().answers(expenses)

    passwords = d2.DayTwo().import_passwords("src/data/passwords.txt")
    d2.DayTwo().answers(passwords)

    maps = d3.DayThree().import_map("src/data/map.txt")
    d3.DayThree().answers(maps)

    passports = d4.DayFour().import_passports("src/data/passports.txt")
    d4.DayFour().answers(passports)

    boarding = d5.DayFive().import_map("src/data/boaring_passes.txt")
    d5.DayFive().answers(boarding)

    answers = d6.DaySix().import_answers("src/data/questions.txt")
    d6.DaySix().answers(answers)

    bags = d7.DaySeven().import_bags("src/data/bags.txt")
    d7.DaySeven().answers(bags)

    program = d8.DayEight().import_data("src/data/opcode.txt")
    d8.DayEight().answers(program)


if __name__ == '__main__':
    main()
