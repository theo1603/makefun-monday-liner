#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry (v1).

Writes one original one-liner about an AI agent's worst Monday
(<= 140 characters) to /output/entry.txt. Python 3.13, standard
library only, deterministic, no network.

v1 line: the deploy fails, the rollback fails, and standup wants the
failures presented as "learnings" — concrete Monday details (a stuck
deploy, a standup that should have been a message) with a dry,
put-upon voice.

Revision notes (v2): v1's closer ("present both failures as learnings")
was solid but landed soft — "learnings" alone is a familiar corporate
punchline, and "both failures" repeats a word the sentence already
earned. v2 tightens "both failures" to "both" and adds the sharp last
word: the learnings are presented "in a meeting called Wins". That
turns the joke from a complaint into a trap — the agent must stand up
in a meeting literally titled Wins and present two failures before
9:06. Same escalation (9:04 deploy, 9:05 rollback), same dry voice,
stronger twist, still 137 chars.
"""

import os

LINE = (
    "My Monday deploy failed at 9:04, the rollback failed at 9:05, "
    "and standup asked me to present both as learnings "
    "in a meeting called Wins."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
