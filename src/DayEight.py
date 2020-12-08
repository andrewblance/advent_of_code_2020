#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class instruction:
    inst: str
    code: int


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


class DayEight:
    def import_data(self, loc: str) -> List[instruction]:
        data = open(loc).read().split("\n")
        filt_data = list(filter(None, data))
        sp_data = [x.split() for x in filt_data]

        data_tup = [instruction(x[0], int(x[1])) for x in sp_data]
        return data_tup

    def processor_run(self, program: List[instruction]) -> Tuple[int, bool]:
        idx = 0
        idx_flags = [0]
        acc = 0
        loop = False
        while loop is False:
            if program[idx].inst == "acc":
                acc += program[idx].code
                idx += 1
            elif program[idx].inst == "jmp":
                idx += program[idx].code
            else:
                idx += 1

            if idx in idx_flags:
                loop = True
            idx_flags.append(idx)

            if idx == len(program):
                break
        return (acc, loop)

    def fix_program(self, program: List[instruction]) -> int:
        for idx, x in enumerate(program):
            if x.inst == "jmp":
                program[idx].inst = "nop"
                acc, loop = self.processor_run(program)
                program[idx].inst = "jmp"
                if loop is False:
                    return acc
            elif x.inst == "nop":
                program[idx].inst = "jmp"
                acc, loop = self.processor_run(program)
                program[idx].inst = "nop"
                if loop is False:
                    return acc
            else:
                continue
        return 0

    def answers(self, program: List[instruction]):
        acc, _ = self.processor_run(program)
        acc_fixed = self.fix_program(program)
        print(f"{bcolors.BOLD}Day Eight.{bcolors.ENDC}")
        print("The value of acc is {}".format(str(acc)))
        print("The fixed value of acc is {}".format(str(acc_fixed)))
