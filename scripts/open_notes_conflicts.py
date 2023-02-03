#!/usr/bin/python3
import os
import re
from pathlib import Path

NOTES_PATH = "/home/bruno/Notes/"

notes_path = Path(NOTES_PATH)

# List conflicts
conflicts_paths = list(notes_path.glob('**/*sync-conflict*.md'))

if len(conflicts_paths) == 0:
    print('NONO')
    os.system("zenity --notification --text 'No conflicts !' ")
    exit(0)

for conflict_path in conflicts_paths:
    print(f"-> {conflict_path}")

    # remove ".sync-conflict-20230120-155918-UPE55MT" from path
    match = re.search(r'(.*)\.sync-conflict.*\.md', str(conflict_path))
    assert(match)
    original_path = Path(match.group(1) + '.md') # ex: /home/bruno/Notes/Divers/poker.md

    # open in Meld
    os.system(f"meld \"{original_path}\" \"{conflict_path}\"")

    # Move to trash
    os.system(f"trash-put \"{conflict_path}\"")  # apt install trash-cli

# print("END")
if len(conflicts_paths) != 0:
    os.system("zenity --notification --text 'END' ")
