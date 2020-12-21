#!/usr/bin/python3
"""
🎅 Advent of Code 2019 Day #10 Monitoring Station Part 1
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import sys
import math

def main():
    """ solution for Day #10 """
    filename="puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = open(filename).readlines()
    astro_map = set()
    astro_dict = dict()

    # build a map of asteroids coordinates
    for i, line in enumerate(file_input):
        for j, char in enumerate(line):
            if char == "#":
                astro_map.add((j,i))
    for coord in astro_map:
        astro_dict[coord] = set()
        for coord2 in astro_map:
            if coord == coord2:
                continue
            # get angle between asteroid at coord and coord2
            slope = math.atan2(coord2[1]-coord[1],coord2[0]-coord[0])
            # only store if unique
            # asteroids at same angle may occlude each other, so store only one angle
            # angle count is equivalent to visible asteroid count
            astro_dict[coord].add(slope)
    best_coord = None
    max_visible = -1
    # find coord that can see most asteroids
    for coord in astro_dict:
        if len(astro_dict[coord]) > max_visible:
            best_coord = coord
            max_visible = len(astro_dict[coord])
    print("part #1", best_coord, max_visible)

if __name__ == "__main__":
    main()
