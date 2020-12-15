"""
🎅
--- Day 9: Sensor Boost ---
You've just said goodbye to the rebooted rover and left Mars when you receive a
faint distress signal coming from the asteroid belt. It must be the Ceres
monitoring station!

In order to lock on to the signal, you'll need to boost your sensors. The Elves
send up the latest BOOST program - Basic Operation Of System Test.

While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous
safety reasons, it refuses to do so until the computer it runs on passes some
checks to demonstrate it is a complete Intcode computer.

Your existing Intcode computer is missing one key feature: it needs support for
parameters in relative mode.

Parameters in mode 2, relative mode, behave very similarly to parameters in
position mode: the parameter is interpreted as a position. Like position mode,
parameters in relative mode can be read from or written to.

The important difference is that relative mode parameters don't count from
address 0. Instead, they count from a value called the relative base. The
relative base starts at 0.

The address a relative mode parameter refers to is itself plus the current
relative base. When the relative base is 0, relative mode parameters and
position mode parameters with the same value refer to the same address.

For example, given a relative base of 50, a relative mode parameter of -7
refers to memory address 50 + -7 = 43.

The relative base is modified with the relative base offset instruction:

Opcode 9 adjusts the relative base by the value of its only parameter. The
relative base increases (or decreases, if the value is negative) by the value
of the parameter.
For example, if the relative base is 2000, then after the instruction 109,19,
the relative base would be 2019. If the next instruction were 204,-34, then
the value at address 1985 would be output.

Your Intcode computer will also need a few other capabilities:

The computer's available memory should be much larger than the initial program.
Memory beyond the initial program starts with the value 0 and can be read or
written like any other memory. (It is invalid to try to access memory at a
negative address, though.)
The computer should have support for large numbers. Some instructions near
the beginning of the BOOST program will verify this capability.
Here are some example programs that use these features:

109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and
produces a copy of itself as output.
1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
104,1125899906842624,99 should output the large number in the middle.
The BOOST program will ask for a single input; run it in test mode by providing
it the value 1. It will perform a series of checks on each opcode, output any
opcodes (and the associated parameter modes) that seem to be functioning
incorrectly, and finally output a BOOST keycode.

Once your Intcode computer is fully functional, the BOOST program should report
no malfunctioning opcodes when run in test mode; it should only output a single
value, the BOOST keycode. What BOOST keycode does it produce?
"""

import itertools
puzzle_input = ""

with open("puzzle_input.txt") as file_input:
    for line in file_input:
        puzzle_input += line

int_code = {}

for i, code in enumerate(puzzle_input.split(",")):
    int_code[i] = int(code)

pc = 0
rel_base = 0

def handle(reg, mode):
    if mode == 0:
        if reg in int_code:
            return int_code[reg]
        else:
            int_code[reg] = 0
            return 0
    if mode == 1:
        return reg
    if mode == 2:
        reg = reg + rel_base
        if reg in int_code:
            return int_code[reg]
        else:
            int_code[reg] = 0
            return 0
    print("invalid mode", mode)
    exit(1)

while True:
    op_in = str(int_code[pc])

    # pad the opcode to fit 5 digits
    if len(op_in) > 5:
        print("opcode too large", op_in)
    extended_op = ["0" for i in range (0, 5 - len(op_in))]
    extended_op += list(op_in)
    # op is last two digits to form opcode
    op = int("".join(extended_op[3] + extended_op[4]))

    #mode = [bool(int(extended_op[0])), bool(int(extended_op[1])), bool(int(extended_op[2]))]
    mode = [int(extended_op[0]), int(extended_op[1]), int(extended_op[2])]
    #print("op", op, "mode", mode, "pc", pc)

    if op == 99:
        break

    if op == 1 or op == 2:
        p1 = int_code[pc+1]
        p2 = int_code[pc+2]

        r1 = handle(p1, mode[2]) 
        r2 = handle(p2, mode[1])
        if mode[0] == 2:
            res = int_code[pc+3] + rel_base
        else:
            res = int_code[pc+3]
            
        if op == 1: int_code[res] = r1 + r2
        if op == 2: int_code[res] = r1 * r2

        pc += 4
        continue

    if op == 3:
        p1 = int_code[pc+1]
        if mode[2] == 2:
            r1 = rel_base + p1
        else:
            r1 = p1
        int_code[r1] = int(input("input:"))
        pc += 2
        continue

    if op == 4:
        p1 = int_code[pc+1]
        r1 = handle(p1, mode[2])
        #print("op", op, "p1", p1, "mode", mode, "pc", pc)
        print(r1)
        pc += 2
        continue

    if op == 5 or op == 6:
        p1 = int_code[pc+1]
        p2 = int_code[pc+2]
        r1 = handle(p1, mode[2])
        r2 = handle(p2, mode[1])
        pc += 3
        if op == 5 and r1:
            pc = r2
        if op == 6 and not r1:
            pc = r2
        continue

    if op == 7 or op == 8:
        p1 = int_code[pc+1]
        p2 = int_code[pc+2]
        r1 = handle(p1, mode[2])
        r2 = handle(p2, mode[1])
        if mode[0] == 2:
            res = int_code[pc+3] + rel_base
        else:
            res = int_code[pc+3]
        int_code[res] = 0

        if op == 7 and r1 < r2:
            int_code[res] = 1
        if op == 8 and r1 == r2:
            int_code[res] = 1
        pc += 4
        continue

    if op == 9:
        p1 = int_code[pc+1]
        r1 = handle(p1, mode[2])
        rel_base += r1
        pc += 2
        continue

    print("unknown op", op, "@", pc)
    exit(1)
