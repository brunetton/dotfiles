#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Simple script to get current activity name

import os
import sqlite3
import sys
from pathlib import Path

from dotenv import load_dotenv



if __name__ == '__main__':
    load_dotenv()
    HAMSTER_DB_FILE_PATH = os.getenv("HAMSTER_DB_FILE_PATH")
    if not HAMSTER_DB_FILE_PATH:
        print("HAMSTER_DB_FILE_PATH environment variable must be defined")
        sys.exit(-1)
    db_path = Path(HAMSTER_DB_FILE_PATH).expanduser()
    if not db_path.exists():
        print(f"Can't find DB path: {db_path!r}")
        sys.exit(-1)
    # Get name
    connection = sqlite3.connect(db_path)
    dbCursor = connection.cursor()
    dbCursor.execute("SELECT name from activities WHERE id = (SELECT activity_id FROM facts WHERE end_time IS NULL)")
    connection.commit()
    r = dbCursor.fetchone()
    connection.close()
    if r:
        print(r[0])
