from operator import mul, add
from itertools import product
from pathlib import Path
from tqdm import tqdm

text = Path('./data/07.txt').read_text()

expressions = []
for line in text.split('\n'):
    k, v = line.split(': ')
    expressions.append([int(k), list(map(int, v.split()))])

def run(expressions, op_list):
    operations = {N+1: list(product(op_list, repeat=N)) for N in range(2,12)}
    results = []
    for n, operands in tqdm(expressions):
        for ops_list in operations[len(operands)]:
            this = operands[0]
            for op, m in zip(ops_list, operands[1:]):
                this = op(this, m)
                if this > n: break
            if this == n:
                break
        results.append(this == n)
    return results

# Part 1.
results = run(expressions, [add, mul])
p1 = sum([r*n for r, (n,_) in zip(results, expressions)])
print(p1)

# Part 2.
broken = [e for e, r in zip(expressions, results) if not r]
cat = lambda x, y: int(str(x) + str(y))
results = run(broken, [add, mul, cat])
p2 = sum([r*n for r, (n,_) in zip(results, broken)])
print(p1 + p2)