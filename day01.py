from collections import Counter
from pathlib import Path

text = Path('./data/01.txt').read_text()

def get_data(text):
    a, b = [], []
    for row in text.split('\n'):
        ai, bi = map(int, row.split())
        a.append(ai)
        b.append(bi)
    return a, b

def total_dist(a: list, b: list) -> int:
    """Sum the abs diffs between sorted a & b."""
    dist = lambda ai, bi: abs(ai - bi)
    pairs = zip(sorted(a), sorted(b))
    return sum(dist(ai, bi) for ai, bi in pairs)

# Part 1.
print(total_dist(*get_data(text)))

def similarity(a: list, b: list) -> int:
    """Sum the products of a_i and the count of a_i in b."""
    count = Counter(b)
    return sum(ai * count[ai] for ai in a)

# Part 2.
print(similarity(*get_data(text)))
