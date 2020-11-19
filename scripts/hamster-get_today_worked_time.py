#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Simple script to get current day's worked time

import os
import sqlite3
import sys
from pathlib import Path

from dotenv import load_dotenv
import pendulum


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
    # Query
    connection = sqlite3.connect(db_path)
    dbCursor = connection.cursor()
    dbCursor.execute("""
        select sum(hours)
        FROM (
            select CAST((julianday(coalesce(end_time, datetime('now','localtime'))) - julianday(start_time))*24 AS real) AS hours
            FROM (SELECT * FROM facts)
            WHERE substr(start_time, 0, 11) == substr(datetime('now','localtime'), 0, 11)
        )
    """)
    connection.commit()
    r = dbCursor.fetchone()
    connection.close()
    assert r
    # Convert to human redeable
    hours = float(r[0])
    it = pendulum.duration(hours=hours)
    print(f"{it.hours}:{it.minutes:02}")  # How to do this with pendulum ?
