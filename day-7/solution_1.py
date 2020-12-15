"""
🎅
--- Day 7: Amplification Circuit ---
Based on the navigational maps, you're going to need to send more power to your ship's thrusters to
reach Santa in time. To do this, you'll need to configure a series of amplifiers already installed
on the ship.

There are five amplifiers connected in series; each one receives an input signal and produces an
output signal. They are connected such that the first amplifier's output leads to the second 
amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on.
The first amplifier's input value is 0, and the last amplifier's output leads to your ship's
thrusters.

    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O
The Elves have sent you some Amplifier Controller Software (your puzzle input), a program that
should run on your existing Intcode computer. Each amplifier will need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an input instruction
to ask the amplifier for its current phase setting (an integer from 0 to 4). Each phase setting is
used exactly once, but the Elves can't remember which amplifier needs which phase setting.

The program will then call another input instruction to get the amplifier's input signal, compute
the correct output signal, and supply it back to the amplifier with an output instruction. (If the
amplifier has not yet received an input signal, it waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters by trying every
possible combination of phase settings on the amplifiers. Make sure that memory is not shared or
reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting
amplifier A to phase setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0. Then, you
could determine the output signal that gets sent from amplifier E to the thrusters with the
following steps:

Start the copy of the amplifier controller software that will run on amplifier A. At its first
input instruction, provide it the amplifier's phase setting, 3. At its second input instruction,
provide it the input signal, 0. After some calculations, it will use an output instruction to
indicate the amplifier's output signal.
Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal
 was produced from amplifier A. It will then produce a new output signal destined for amplifier C.
Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B,
then collect its output signal.
Run amplifier D's software, provide the phase setting (4) and input value, and collect its output
signal.
Run amplifier E's software, provide the phase setting (0) and input value, and collect its output
signal.
The final output signal from amplifier E would be sent to the thrusters. However, this phase setting
 sequence may not have been the best one; another sequence might have sent a higher signal to the
 thrusters.

Here are some example programs:

Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):

3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):

3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0
Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):

3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
Try every combination of phase settings on the amplifiers. What is the highest signal that can be
sent to the thrusters?
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

def amplifier(phase, input_sig):
    pc = 0
    input_stage = 0

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
            break

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
            continue

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
    return output

max_output = -1 
phase_permutatons = list(itertools.permutations([0,1,2,3,4]))
for phase_array in phase_permutatons:
    a_input = 0
    for i in range (0, 5):
        a_input = amplifier(phase_array[i], a_input)
    if a_input > max_output:
        max_output = a_input

print (max_output)
