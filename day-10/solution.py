#!/usr/bin/python3
"""
🎅 Advent of Code 2019 Day #10 Monitoring Station Part 1
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import sys
import math

def main():
    filename="puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = open(filename).readlines()
    astro_map = set()
    astro_dict = dict()
    for i in range(0, len(file_input)):
        for j in range(0, len(file_input[i])):
            if file_input[i][j] == "#":
                astro_map.add((j,i))
    for c in astro_map:
        astro_dict[c] = set()
        for c2 in astro_map:
            if c == c2:
                continue
            slope = math.atan2(c2[1]-c[1],c2[0]-c[0])
            astro_dict[c].add(slope)
    max_c = None
    max_items = -1
    for c in astro_dict:
        if len(astro_dict[c]) > max_items:
            max_c = c
            max_items = len(astro_dict[c])
    print("part #1", max_c, max_items)

if __name__ == "__main__":
    main()
