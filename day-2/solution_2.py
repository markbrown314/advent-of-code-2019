"""
🎅🏻
--- Part Two ---
"Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll
 probably use it again. Real Intcode computers support many more features than your new one, but
 we'll let you know what they are as you need them."

"However, your current priority should be to complete your gravity assist around the Moon. For this
mission to succeed, we should settle on some terminology for the parts you've already built."

Intcode programs are given as a list of integers; these values are used as the initial state for
the computer's memory. When you run an Intcode program, make sure to start by initializing memory to
the program's values. A position in memory is called an address (for example, the first value in
memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an
opcode, if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is
the opcode; 2, 3, and 4 are the parameters. The instruction 99 contains only an opcode and has no
parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an
instruction finishes, the instruction pointer increases by the number of values in the instruction;
until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the
add and multiply instructions. (The halt instruction would increase the instruction pointer by 1,
but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need
to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just
like before. In this program, the value placed in address 1 is called the noun, and the value placed
in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time
you try a pair of inputs, make sure you first reset the computer's memory to the values in the program
(your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. 
What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

Your puzzle answer was 7870
"""

puzzle_input="""
            1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,
            1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,
            13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,
            6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,
            2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,
            127,1,127,9,0,99,2,0,14,0
            """
            
int_code = []

for code in puzzle_input.split(","):
    int_code.append(int(code))
    
int_code[1] = 78
int_code[2] = 70
pc = 0
res = 0
while True:
    op = int_code[pc]

    if op == 99:
        break

    r1 = int_code[pc+1]
    r2 = int_code[pc+2]
    res = int_code[pc+3]

    if op == 1:
        int_code[res] = int_code[r1] + int_code[r2]
        pc += 4
        continue
    if op == 2:
        int_code[res] = int_code[r1] * int_code[r2]
        pc += 4
        continue
    print("unknown op", op, "@", pc)
    exit(1)

print (100 * int_code[1] + int_code[2])
