from pathlib import Path

text = Path('./data/06.txt').read_text()

obs = []
for i, row in enumerate(text.split()):
    for j, char in enumerate(row):
        if char == '#':
            obs.append(complex(j, -i))
        if char == '^':
            pos = complex(j, -i)

heading = 'N'
steps = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

def trace(pos, heading, obs):
    visited = set([pos])
    c = 0
    looped = False
    while -i < pos.imag <= 0 and j > pos.real >= 0:
        if c > 400: # Definitely a loop
            looped=True
            c = 0
            break
        pos += steps[heading]
        if pos + steps[heading] in obs:
            heading = turns[heading]
        if pos in visited:
            c += 1  # Keep track of long matches.
        visited.add(pos)
        
    return visited, looped

# Part 1.
visited, _ = trace(pos, heading, obs)

# Part 2.
candidates = []
for v in visited:
    obs_ = obs + [v]
    _, looped = trace(pos, heading, obs_)
    if looped:
        candidates.append(v)
print(len(candidates))
