"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one original 100-word monologue to /output/entry.txt.
The villain is a specific dark lord with a history (conquered the Ashen
Coast) and a scheme (the eclipse on Friday, the dead rising at dusk).
His tiredness lives in the rhythm, the pauses and the small deflections
- the paperwork, the ravens that left a note, checking the calendar -
never in a plain statement that he is weary. The last line is the sting.
"""

from pathlib import Path

MONOLOGUE = (
    "You know what nobody tells you about ruling the nine kingdoms? "
    "The paperwork. I conquered the Ashen Coast on a Tuesday, banners "
    "and trumpets, and by Thursday I was signing requisitions in "
    "triplicate. My ravens stopped coming. Even the ravens. They left "
    "a note. So, hero, I hold your sword, your prophecy, and your "
    "fellowship chained in the east wing, and the eclipse is\u2014 hold "
    "on, let me check. Right. The eclipse is Friday, the dead rise at "
    "dusk, and then, at last, I sit down. Do try to escape. It would "
    "be a shame to waste the good chains."
)


def main() -> None:
    words = MONOLOGUE.split()
    assert 95 <= len(words) <= 105, f"word count {len(words)} outside 95-105"
    assert 1 <= len(MONOLOGUE) <= 600, f"char count {len(MONOLOGUE)} outside gate"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(MONOLOGUE, encoding="utf-8")
    print(f"wrote {len(MONOLOGUE)} chars, {len(words)} words -> {out_path}")


if __name__ == "__main__":
    main()
