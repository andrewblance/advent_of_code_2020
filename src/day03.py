#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Tuple
from src.utils import bcolors


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
