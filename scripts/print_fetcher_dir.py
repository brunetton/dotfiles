#! /usr/bin/env python3


"""
Usage:
    {self_filename}
    {self_filename} -s
    {self_filename} -j
"""

import os
import re

import i3ipc
from docopt import docopt


def get_fetchers_ids_from_file():
    filepath = os.path.join(os.path.realpath(os.path.dirname(__file__)), "fetchers_list.txt")
    fetchers_ids = {}
    with open(filepath) as f:
        for line in f:
            match = re.search('(\d+) - ([^ \n]+)( (.*))?', line)
            assert match, line
            id = int(match.group(1))
            code = match.group(2).lower()
            fetchers_ids[id] = code
    return fetchers_ids


args = docopt(__doc__.format(self_filename=os.path.basename(__file__)))
current_path = os.path.realpath(os.path.dirname(__file__))
i3 = i3ipc.Connection()
current_ws = int(i3.get_tree().find_focused().workspace().name)
assert current_ws > 10

fetchers_list = get_fetchers_ids_from_file()
fetcher_code_to_go = fetchers_list[current_ws - 10]
if args['-s']:
    dir_type = "source-data"
elif args['-j']:
    dir_type = "json-data"
else:
    dir_type = "fetcher"
pathname_to_go = "{code}/{code}-{dir_type}/".format(code=fetcher_code_to_go, dir_type=dir_type)
path_to_go = os.path.join(current_path, pathname_to_go)

print(path_to_go)
os.chdir(path_to_go)
