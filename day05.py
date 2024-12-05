from pathlib import Path
from collections import defaultdict


rules_text, batches_text = Path('./data/05.txt').read_text().split('\n\n')

RULES = defaultdict(list)
for rule in rules_text.split():
    a, b = rule.split('|')
    RULES[int(a)].append(int(b))

batches = []
for batch in batches_text.split():
    batches.append(list(map(int, batch.split(','))))

def is_correct(batch) -> bool:
    correct = True
    for i, page in enumerate(batch):
        if not all(p in RULES.get(page, []) for p in batch[i+1:]):
            correct = False
            break
    return correct


# Part 1.
corrects, incorrects = [], []
for batch in batches:
    if is_correct(batch):
        corrects.append(batch[len(batch) // 2])
    else:
        incorrects.append(batch)  # For Part 2.

print(sum(corrects))

# Part 2.
# Correcting seems like overkill. Also hard.
count = 0
for batch in incorrects:
    midpoint = len(batch) // 2
    # Find member with this many "afters" in this batch.
    for n in batch:
        afters = [m for m in RULES.get(n, []) if m in batch]
        if len(afters) == midpoint:
            count += n
            break

print(count)
