from pathlib import Path
from collections import defaultdict
from itertools import combinations, chain


text = Path('./data/08.txt').read_text()

antennas = defaultdict(list)
for j, row in enumerate(text.split()):
    for i, char in enumerate(row):
        if char == '.':
            continue
        antennas[char].append(complex(i, j))

def get_antinodes(antennas: dict, n: int=1) -> dict:
    """Visit all pairs, compute antinodes."""
    antinodes = defaultdict(list)
    for freq, locs in antennas.items():
        for p, q in list(combinations(locs, 2)):
            diff = q - p
            antinodes[freq].extend(p - n*diff for n in range(n))
            antinodes[freq].extend(q + n*diff for n in range(n))
    return antinodes

def in_bounds(p: complex) -> bool:
    """Recycle i and j from earlier."""
    global i, j
    return (0 <= p.real <= j) and (0 <= p.imag <= i)

antinodes = get_antinodes(antennas)
on_map = set(a for a in chain(*antinodes.values()) if in_bounds(a))
print(len(on_map))


# Part 2.
antinodes = get_antinodes(antennas, n=50)
on_map = set(a for a in chain(*antinodes.values()) if in_bounds(a))
print(len(on_map))
