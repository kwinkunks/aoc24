from collections import defaultdict
from pathlib import Path

text = Path('./data/04.txt').read_text()

# Build locations dict.
locs = defaultdict(list)
for i, row in enumerate(text.split('\n')):
    for j, char in enumerate(row):
        locs[char].append(complex(i, j))

# Make check grids geometrically (x = 0, x = y, etc).
# There are 8 grids for a given location.
grids = defaultdict(list)
for i in range(-3, 4):  # NB Grid will be 'backwards' for SAMX.
    for j in range(-3, 4):
        if (i == 0) or (j == 0) or (i == j) or (-i == j):
            grids[(i==0, j==0, i<0, j<0)].append(complex(i, j))
_ = grids.pop((1, 1, 0, 0)) # Origin not needed.

# For every X, check its grid.
total = 0
for x in locs['X']:
    # Check all the grids at this location.
    this_count = 0
    for _, grid in grids.items():
        # For each grid, check its coords, one per M, A, S.
        for char, loc in zip('MAS', sorted(grid, key=abs)):

            # If the location is not in that letter's locs, then skip the rest.
            if x + loc not in locs[char]:
                break

            # If we got to S, count it.
            if char == 'S':
                this_count += 1
        
    total += this_count

# Part 1.
print(total)

# Part 2.
grids = [(-1-1j, 1+1j), (-1+1j, 1-1j), (1-1j, -1+1j), (1+1j, -1-1j)]

# Sigh, can't easily re-use the code above...
# Don't sort coords this time because I fixed it in the grids.
total = 0
for a in locs['A']:
    this_count = 0
    for grid in grids:
        for char, loc in zip('MS', grid):
            if a + loc not in locs[char]:
                break
            if char == 'S':
                this_count += 1
    if this_count == 2:
        total += 1

print(total)
