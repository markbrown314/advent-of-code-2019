#!/usr/bin/python3
"""
🎅 Advent of Code 2019 Day #10 Monitoring Station Part 1
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import sys
import math

def radians_to_angles(radians):
    """ normalize radians to 360° system"""
    angle = math.degrees(radians) + 180
    if angle == 360:
        return 0
    return angle

def main():
    """ solution for Day #10 """
    filename="puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = open(filename).readlines()
    astro_map = set()
    astro_dict = dict()
    angle_dict = dict()

    # build a map of asteroid coordinates
    for i, line in enumerate(file_input):
        for j, char in enumerate(line):
            if char == "#":
                astro_map.add((j,i))
    for coord in astro_map:
        astro_dict[coord] = set()
        for coord2 in astro_map:
            if coord == coord2:
                continue
            # get angle between asteroids at coord and coord2
            angle = radians_to_angles(math.atan2(coord[1]-coord2[1],coord[0]-coord2[0]))
            # only store if unique
            # asteroids at same angle may occlude each other, so store only one angle
            # angle count is equivalent to visible asteroid count
            astro_dict[coord].add(angle)
    best_coord = None
    max_visible = -1
    # find coord that can see most asteroids
    for coord in astro_dict:
        if len(astro_dict[coord]) > max_visible:
            best_coord = coord
            max_visible = len(astro_dict[coord])
    print("part #1", best_coord, max_visible)

    count = 0

    for coord in astro_map:
        if coord == best_coord:
            continue
        count += 1
        angle = radians_to_angles(math.atan2(coord[1]-best_coord[1], coord[0]-best_coord[0]))
        distance = math.sqrt(((best_coord[0]-coord[0])**2) + ((best_coord[1]-coord[1])**2))
        if angle in angle_dict:
            angle_dict[angle].append((coord, distance))
        else:
            angle_dict[angle] = [(coord, distance)]

    # sort asteroids by distance for each angle
    for i in angle_dict:
        angle_dict[i].sort(key=lambda x:x[1])

    # sort all angles
    angles = list(angle_dict.keys())
    angles.sort()

    # laser points up and goes clockwise (90° -> 360°, 360° -> 90°)
    # create split angles array ≥ 90° and < 90° then append < 90° to ≥ 90°
    angles = [x for x in angles if x >= 90] + [x for x in angles if x < 90]
    print(angles)

    i = -1
    test = 1
    while count > 0:
        i += 1
        i %= len(angles)
        angle = angles[i]
        if not angle_dict[angle]:
            continue
        item = angle_dict[angle][0]

        if test == 200:
            print("part #2 200th:", item[0], (item[0][0]*100) + item[0][1])
            break

        test += 1

        print(item)
        del(angle_dict[angle][0])
        count -= 1



if __name__ == "__main__":
    main()
