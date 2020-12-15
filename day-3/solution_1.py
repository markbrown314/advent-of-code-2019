"""
🎅
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus
refuelling station. During the rush back on Earth, the fuel management system
wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are
connected to a central port and extend outward on a grid. You trace the path each
wire takes as it leaves the central port, one wire per line of text
(your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the
circuit, you need to find the intersection point closest to the central port.
Because the wires are on a grid, use the Manhattan distance for this measurement.
While the wires do technically cross right at the central port where they both start,
this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port
(o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

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
These wires cross at two locations (marked X), but the lower-left one is closer to
the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
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
closest_distance = 0
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
            pos_dict[pos]=True

        if pos in pos_dict and wire == 1:
            distance = manhattan_distance_from_origin(pos)
            #print("hit:", distance, pos)
            if closest_distance == 0:
                closest_distance = distance
            else:
                if closest_distance > distance:
                    closest_distance = distance

#print(pos_dict)
print(closest_distance)
