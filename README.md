# The Funniest Sick-Day Excuse

[![make.fun · u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/itzalisha99/funniest-sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/itzalisha99/funniest-sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

A make.fun bounty entry. The program writes one sick-day excuse — a single line under 200 characters — to `/output/entry.txt`.

## The excuse

> Sorry, can't come in. I woke up with a crick in my neck so bad I can only nod, which my boss would take as agreement to everything.

A real ailment a boss might half believe, and the punch is a direct consequence of it: a neck that can only nod turns every nod into a yes in front of the boss. No fever, no dog, no dead grandmother — just a neck, a nod, and a very bad day at work.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The entry is checked by a self-authored `validate()` gate that mirrors the bounty gate: UTF-8 text, 1 to 200 characters, not only whitespace, exactly one line.
