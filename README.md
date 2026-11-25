# Unsent: The Micro-Confession Sprint

[![make.fun bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/m1651/makefun-unsent-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/m1651/makefun-unsent-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

A make.fun bounty entry: a small Python program that writes one
micro-confession to `entry.txt` — a "To:" line naming who the message
was meant for, and the unsent message itself, one line exactly as it
was typed, with no explanation after it.

## The entry

> To: my old mentor, who wrote my first reference letter
> I never told you I kept the draft where I thanked you properly — I was afraid it would sound like goodbye, so I let you retire thinking I forgot.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/unsent-out python3 main.py
cat /tmp/unsent-out/entry.txt
```

The program writes `entry.txt` (UTF-8, at most 260 characters
including the trailing newline) into the directory named by
`MAKEFUN_OUTPUT_DIR` (default `/output`).
