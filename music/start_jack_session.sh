#!/bin/sh
sleep 1
a2jmidid -e &
sleep 2
jack-matchmaker -p ~/dev/dotfiles/music/jackmatchmaker.conf &
