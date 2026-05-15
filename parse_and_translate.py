import re

with open("game/capitulos/capitulo1.rpy", "r", encoding="utf-8") as f:
    lines = f.readlines()

blocks = []
block_idx = 1
for i, line in enumerate(lines):
    # Match character string: e.g. mc "text" or narrator "text"
    match_dialogue = re.match(r'^(\s+)(\w+)\s+"(.*)"', line)
    if match_dialogue:
        indent, char, text = match_dialogue.groups()
        blocks.append((char, text))
    else:
        # Match menu option: e.g. "Option":
        match_menu = re.match(r'^(\s+)"(.*)":', line)
        if match_menu:
            indent, text = match_menu.groups()
            blocks.append((None, text)) # None indicates menu/no-char

for char, text in blocks:
    print(f"translate english capitulo1_{block_idx:04d}:")
    if char:
        print(f"    # {char} \"{text}\"")
        print(f"    {char} \"\"")
    else:
        print(f"    # \"{text}\":")
        print(f"    \"\":")
    print()
    block_idx += 1
