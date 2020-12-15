"""
🎅
--- Part Two ---
It's no good - in this configuration, the amplifiers can't generate a large enough output signal to
produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a
feedback loop:

      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
Most of the amplifiers are connected as they were before; amplifier A's output is connected to
amplifier B's input, and so on. However, the output from amplifier E is now connected into amplifier
 A's input. This creates the feedback loop: the signal will be sent through the amplifiers many
 times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9,
again each used exactly once. These settings will cause the Amplifier Controller Software to
repeatedly take input and produce output many times before halting. Provide each amplifier its phase
 setting at its first input instruction; all further input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one
should continue receiving and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very
first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's
input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When
this happens, the last output signal from amplifier E is sent to the thrusters. Your job is to find
the largest output signal that can be sent to the thrusters using the new phase settings and
feedback loop arrangement.

Here are some example programs:

Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
Try every combination of the new phase settings on the amplifier feedback loop. What is the highest
signal that can be sent to the thrusters?
"""

puzzle_input="""
            3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,
            9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,
            9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,
            9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,
            4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,
            9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,
            3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,
            9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,
            9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,
            9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,
            2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,
            9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,
            9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,
            1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,
            9,1002,9,2,9,4,9,99
            """
import itertools

int_code = []

for code in puzzle_input.split(","):
    int_code.append(int(code))

def amplifier(state, phase, input_sig):
    pc = state[0]
    input_stage = state[1]
    output = state[2]

    while True:
        op_in = str(int_code[pc])

        # pad the opcode to fit 5 digits
        if len(op_in) > 5:
            print("opcode too large", op_in)
        extended_op = ["0" for i in range (0, 5 - len(op_in))]
        extended_op += list(op_in)
        # op is last two digits to form opcode
        op = int("".join(extended_op[3] + extended_op[4]))

        mode = [bool(int(extended_op[0])), bool(int(extended_op[1])), bool(int(extended_op[2]))]
    
        if op == 99:
            return ((pc, -1, output))

        if op == 1 or op == 2:
            p1 = int_code[pc+1]
            p2 = int_code[pc+2]
            r1 = p1 if mode[2] else int_code[p1] 
            r2 = p2 if mode[1] else int_code[p2] 
            res = int_code[pc+3]

            if op == 1: int_code[res] = r1 + r2
            if op == 2: int_code[res] = r1 * r2

            pc += 4
            continue

        if op == 3:
            res = int_code[pc+1]
            if input_stage == 0:
                int_code[res] = phase

            if input_stage == 1:
                int_code[res] = input_sig


            input_stage += 1
            pc += 2
            continue

        if op == 4:
            p1 = int_code[pc+1]
            r1 = p1 if mode[2] else int_code[p1]
            output = r1
            pc += 2
            return (pc, 1, output)

        if op == 5 or op == 6:
            p1 = int_code[pc+1]
            p2 = int_code[pc+2]
            r1 = p1 if mode[2] else int_code[p1]
            r2 = p2 if mode[1] else int_code[p2]
            pc += 3
            if op == 5 and r1:
                pc = r2
            if op == 6 and not r1:
                pc = r2
            continue

        if op == 7 or op == 8:
            p1 = int_code[pc+1]
            p2 = int_code[pc+2]
            r1 = p1 if mode[2] else int_code[p1] 
            r2 = p2 if mode[1] else int_code[p2] 
            res = int_code[pc+3]
            int_code[res] = 0

            if op == 7 and r1 < r2:
                int_code[res] = 1
            if op == 8 and r1 == r2:
                int_code[res] = 1
            pc += 4
            continue

        print("unknown op", op, "@", pc)
        exit(1)

max_output = -1 

phase_permutatons = list(itertools.permutations([5,6,7,8,9]))

for phase_array in phase_permutatons:
    output = 0
    stable = False
    state = [(0,0,0)] * 5
    while not stable:
        stable = True

        for i in range (0, 5):
            state[i] = amplifier(state[i], phase_array[i], output)
            output = state[i][2]
            stable &= (state[i][1] == -1)

        if  output > max_output:
            max_output = output

print (max_output)
