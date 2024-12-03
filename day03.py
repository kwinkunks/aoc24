import re
from pathlib import Path

text = Path('./data/03.txt').read_text()

# Part 1.
def summult(text):
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    valid_pairs = pattern.findall(text)
    total = 0
    for a, b in valid_pairs:
        total += int(a) * int(b)
    return(total)

print(summult(text))

# Part 2.
# First get the do() blocks, then process as above.
# Let's just be dumb.
parsed, valid = "", ""
recording = True
for c in text:
    parsed += c
    if recording:
        valid += c
    if parsed[-4:] == "do()":
        recording = True
    if parsed[-7:] == "don't()":
        recording = False

print(summult(valid))
