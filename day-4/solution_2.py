"""
🎅🏻
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits
are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following
are now true:

112233 meets these criteria because the digits never decrease and all repeated
digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice,
it still contains a double 22).
How many different passwords within the range given in your puzzle input
meet all of the criteria?

Your puzzle answer was 677.
"""

def password_count(start, end):

    candidates = [i for i in range(start, end+1)]
    valid_count = 0
    for password in candidates:
        run_list = []

        # validator
        prev = -1
        digit_count = 0
        holds_invariant = True
        run = ""

        for digit in str(password):
            digit_count += 1
            if prev > int(digit):
                holds_invariant = False

            if prev != int(digit):
                if run != "":
                    run_list.append(run)
                    run = ""
        
            prev = int(digit)
            run = run + digit

        run_list.append(run)
        if digit_count == 6 and holds_invariant:
            for double_check in run_list:
                if len(double_check) == 2:
                    valid_count += 1
                    break

    return valid_count

if __name__ == '__main__':
    print(password_count(246515, 739105))