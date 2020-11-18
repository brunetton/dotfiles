#!/bin/sh
pkill -ef jack-matchmaker
jack-matchmaker -p ~/dev/dotfiles/music/jackmatchmaker.conf &
