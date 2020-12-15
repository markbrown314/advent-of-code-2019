"""
🎅
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to
minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each
intersection; choose the intersection where the sum of both wires' steps is
lowest. If a wire visits a position on the grid multiple times, use the steps
value from the first time it visits that position when calculating the total
value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire
has entered to get to that location, including the intersection being
considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached
after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second
wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only
8+5+2 = 15 and the second wire takes only 7+6+2 = 15,
a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""

def manhattan_distance_from_origin(coord):
    return abs(coord[0])+abs(coord[1])

path_list = []
with open("puzzle_input.txt") as input_file:
    for input_data in input_file:
        input_data = input_data.rstrip("\n")
        path_list.extend(input_data.split(","))
        path_list.append("*0")
pos_dict = {}
pos = (0,0)
total_distance_wire0 = 0
total_distance_wire1 = 0
least_wire_distance = -1

wire = 0

for path in path_list:
    direction = path[0]
    distance = int(path[1:])
    x_off = 0
    y_off = 0
    #print(direction, ":", distance, pos)

    if direction == "R":
        x_off = 1
        y_off = 0
    if direction == "L":
        x_off = -1
        y_off = 0
    if direction == "U":
        x_off = 0
        y_off = 1
    if direction == "D":
        x_off = 0
        y_off = -1
    if direction == "*":
        pos = (0,0)
        wire = 1
        continue

    for i in range(1, distance+1):
        pos = (pos[0]+x_off, pos[1]+y_off)
        #print(i,":", pos)
        if wire == 0:
            total_distance_wire0 += 1
            pos_dict[pos] = total_distance_wire0
        if wire == 1:
            total_distance_wire1 += 1

        if pos in pos_dict and wire == 1:
            distance = manhattan_distance_from_origin(pos)
            if least_wire_distance == -1 or least_wire_distance > pos_dict[pos] + total_distance_wire1:
                least_wire_distance = pos_dict[pos] + total_distance_wire1
            #print("hit:", distance, pos, "best so far", least_wire_distance)

print(least_wire_distance)
