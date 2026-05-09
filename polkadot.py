from pathlib import Path


def computePolkadotScore(ascii_art: str) -> int:
    lines = ascii_art.splitlines()

    polkadot_char = "O"
    pupil_char = "•"

    eye_line_index = None

    for i, line in enumerate(lines):
        if "•" in line and ";" in line:
            eye_line_index = i
            break

    if eye_line_index is None:
        raise ValueError("Could not find Angelica's eye line.")

    pupil_count = lines[eye_line_index].count(pupil_char)

    lips_line = lines[eye_line_index + 1]

    lip_positions = [
        i for i, ch in enumerate(lips_line)
        if ch == ";"
    ]

    if len(lip_positions) < 2:
        raise ValueError("Could not find Angelica's lips.")

    lip_start_x = lip_positions[0]
    lip_end_x = lip_positions[1]

    inside = 0
    outside = 0

    for line in lines:
        for x, ch in enumerate(line):
            if ch == polkadot_char:
                if lip_start_x <= x <= lip_end_x:
                    inside += 1
                else:
                    outside += 1

    return outside + (inside * pupil_count)


ascii_art_path = Path(r"C:\Users\shubh\OneDrive\Desktop\angelica.txt")
ascii_art = ascii_art_path.read_text(encoding="utf-8")

print(computePolkadotScore(ascii_art))