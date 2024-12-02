from pathlib import Path

text = Path('./data/02.txt').read_text()
data = [list(map(int, row.split())) for row in text.split('\n')]

def is_safe(report):
    """Just need the discrete derivative."""
    diffs = [v - u for u, v in zip(report, report[1:])]
    has_small_steps = max(abs(d) for d in diffs) <= 3
    is_monotonic = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    return has_small_steps and is_monotonic

# Part 1.
print(sum(is_safe(r) for r in data))

def is_tolerated(report):
    """Small enough to brute force."""
    for i in range(len(report)):
        report_ = report[:i] + report[i+1:]
        if is_safe(report_):
            return True
    return False

# Part 2.
print(sum(is_tolerated(r) for r in data))
