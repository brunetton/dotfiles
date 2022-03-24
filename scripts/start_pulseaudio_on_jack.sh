#!/bin/sh
pactl load-module module-jack-sink
echo "set-default-sink jack_out" | pacmd
