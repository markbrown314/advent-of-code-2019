"""
🎅
--- Day 8: Space Image Format ---
The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars
rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near
the rover.

When you reach the rover, you discover that it's already in the process of rebooting! It's just
waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of
the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding;
instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why
this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel. The digits
fill each row of the image left-to-right, then move downward to the next row, filling rows
top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way.
So, the first digit corresponds to the top-left pixel of the first layer, the second digit
corresponds to the pixel to the right of that on the same layer, and so on until the last digit,
which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds
 to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the
layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied
by the number of 2 digits?
"""
import re
puzzle_input = ""

with open("puzzle_input.txt") as file_input:
    for line in file_input:
        puzzle_input += line

layer_array = []
dimensions = (25,6)
layer = []

for pixel in puzzle_input:
    if re.match('[0-9]', pixel) is None:
        continue
    layer.append(int(pixel))
    if len(layer) == dimensions[0] * dimensions[1]:
        layer_array.append(layer)
        layer = []

def count_pixel_by_value(layer, value):
    count = 0
    for pixel in layer:
        if pixel == value:
            count += 1
    return count

min_zero_count = (dimensions[0] * dimensions[1], 0) # count and layer
for i, layer in enumerate(layer_array):
    count = count_pixel_by_value(layer, 0)
    if count < min_zero_count[0]:
        min_zero_count = (count, i)

i = min_zero_count[1]
ones = count_pixel_by_value(layer_array[i], 1)
twos = count_pixel_by_value(layer_array[i], 2)

print(ones * twos)
