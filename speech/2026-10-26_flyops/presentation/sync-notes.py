"""Copy the speech from ../Речь.md into the speaker notes of index.html.

Each "### N. Title (time)" section of the speech fills <aside class="notes" data-n="N">.
Run after editing the speech: python3 sync-notes.py
"""
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEECH = HERE.parent / "Речь.md"
DECK = HERE / "index.html"

HEADING = re.compile(r"^### (\d+)\. (.+?) \(([\d.]+-[\d.]+)\)\s*$")
ASIDE = re.compile(r'<aside class="notes" data-n="(\d+)"[^>]*>.*?</aside>', re.S)


def parse_speech(text: str) -> dict[int, tuple[str, str, list[str]]]:
    sections: dict[int, tuple[str, str, list[str]]] = {}
    current = None
    for line in text.splitlines():
        match = HEADING.match(line)
        if match:
            current = int(match.group(1))
            sections[current] = (match.group(2), match.group(3), [])
        elif line.startswith("#"):
            current = None
        elif current is not None and line.strip():
            sections[current][2].append(line.strip())
    return sections


def main() -> int:
    sections = parse_speech(SPEECH.read_text(encoding="utf-8"))
    deck = DECK.read_text(encoding="utf-8")
    found = [int(number) for number in ASIDE.findall(deck)]
    missing = sorted(set(found) ^ set(sections))
    if missing:
        print(f"Speech sections and slide notes differ: {missing}", file=sys.stderr)
        return 1

    def fill(match: re.Match) -> str:
        title, time, paragraphs = sections[int(match.group(1))]
        body = "".join(f"<p>{html.escape(paragraph, quote=False)}</p>" for paragraph in paragraphs)
        return (f'<aside class="notes" data-n="{match.group(1)}" data-title="{html.escape(title)}"'
                f' data-time="{time}">{body}</aside>')

    DECK.write_text(ASIDE.sub(fill, deck), encoding="utf-8")
    print(f"Synced {len(found)} slide notes from {SPEECH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
