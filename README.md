# aoc24

No frills Python again this year.

> [!CAUTION]
> Descriptions contain spoilers!


## Week 1

- **Day 1: Historian Hysteria** — The 'hard to parse' style of 2023 is back, presumably to keep the chatbots away. Too bad because ChatGPT solves both parts correctly with no instruction (see [chatgpt/day01.py](./chatgpt/day01.py)). Much easier than last year's Day 1, this felt more like earlier years. SLOC: 19.
- **Day 2: Red-Nosed Reports** — Fun little problem with the derivative of an integer series. Part 2 can probably be done in a clever way (something something second derivative) but brute force suffices. SLOC: 16.
- **Day 3: Mull It Over** — Regex to the rescue! Sort of: Part 1 was very fast, tried to write a cunning pattern for Part 2, went as expected, ended up parsing it myself, turned out to be much easier. SLOC: 22.
- **Day 4: Ceres Search** — Fun word-search puzzle... or it would have been fun if I had found my bug a bit sooner: I needed to reverse the coordinates for 'backwards' XMAS's. Otherwise fairly happy with the algorithm, although it needed a structural change for Part 2 (so I couldn't easily it into a function). SLOC: 37.
- **Day 5: Print Queue** — Part 1 seemed ominously easy but of course was not really required at all for Part 2, which tries to tempt you into the sort. I wrote down how to do that, then realized what could be done to avoid it. (When spidey senses tingle while reading things like "For some reason, the elves want the midpoint..." you should pay attention!). SLOC: 38.
- **Day 6: Guard Gallivant** — Traveling today, did Part 1 on the train out but very late to Part 2... tried to be clever but brute force did it 😬 Too distracted to get into the task really, but I do like the grid navigation problems. SLOC: 35.
- **Day 7: Bridge Repair** — Totally fine... except for the fact that I rashly decided to use a `dict` for the storage of the problems :man-facepalming: Part 2 was sped up a bit by (a) only processing entries not passing Part 1 and (b) early stopping when solutions are found or `n` is exceeded, but it still takes 15 s. SLOC: 30.

When counting SLOC, I don't include blank or comment lines.
