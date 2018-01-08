#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import re
import subprocess
import shutil
import sys


'''To be used with wav dir in argument.
Looks for repete's name in begining of folder name: "r43b - 12 juin" => name : "r43b"
Keeps wav files in wav/ subdir
'''


LAME_OPTIONS = "-V2 --abr 96"
# V2: good VBR qual
# --abr : average bitrate : 96Kb/s

LAME_ID3_OPTIONS = '--tt "{title}" --tl "{album}"'

# File with ID3 artist name tag (searched on folder upon given folder)
ID3_ARTIST_TAG_FILENAME = "id3_artist_tag"


if len(sys.argv) < 2:
    print "Working folder needed"
    sys.exit(-1)

files_dir = sys.argv[1]
print("files_dir: {}".format(files_dir))
file_dirname = os.path.basename(files_dir)  # '/a/b/r1 - 12 jan' => 'r1 - 12 jan'
re_result = re.search(r'^(\S+) ', file_dirname)
assert re_result, "{!r} doesn't seems to be a repete folder.".format(file_dirname)
repete_name = re_result.group(1)
assert repete_name
wav_subfolder = os.path.join(files_dir, "{} - wav".format(repete_name))
if not os.path.exists(wav_subfolder):
    os.mkdir(wav_subfolder)

# Look for ID3 artist file
id3_filename = os.path.abspath(os.path.join(files_dir, '..', ID3_ARTIST_TAG_FILENAME))
artist_lame_option = ''
if os.path.exists(id3_filename):
    print "=> Found id3 filename; using it"
    artist_name = open(id3_filename, 'r').readline().strip()
    artist_lame_option = '--ta "{}"'.format(artist_name)

wav_files = glob.glob(os.path.join(files_dir, "*.wav")) + glob.glob(os.path.join(files_dir, "*.WAV"))
assert wav_files, "No wav files found in {!r}".format(files_dir)
for wav_file in sorted(wav_files):
    filename = os.path.basename(wav_file)
    print "-> {}".format(filename)
    song_name = filename[:-4]
    song_name_with_repete = "{} - {}".format(song_name, repete_name)
    mp3_filename = song_name_with_repete + '.mp3'
    mp3_path = os.path.join(files_dir, mp3_filename)
    options = "{} {} {}".format(LAME_OPTIONS, LAME_ID3_OPTIONS.format(title=song_name_with_repete, album=repete_name), artist_lame_option)
    command = 'lame {options} "{wav_file}" "{mp3_path}"'.format(options=options, wav_file=wav_file, mp3_path=mp3_path)
    subprocess.call(command, shell=True)
    shutil.move(wav_file, wav_subfolder)
