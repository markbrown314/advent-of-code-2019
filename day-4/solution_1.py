"""
🎅🏻
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected
by a password. The Elves had written the password on a sticky note,
but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever
increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle
input meet these criteria?

Your puzzle answer was 1048.
"""

def password_count(start, end):

    candidates = [i for i in range(start, end+1)]

    valid_count = 0
    for password in candidates:
        # validator
        prev = -1
        adjecency_count = 0
        digit_count = 0
        holds_invariant = True

        for digit in str(password):
            digit_count += 1
            if prev > int(digit):
                holds_invariant = False
            if prev == int(digit):
              adjecency_count += 1
            prev = int(digit)

        if digit_count == 6 and adjecency_count >= 1 and holds_invariant:
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    print(password_count(246515, 739105))