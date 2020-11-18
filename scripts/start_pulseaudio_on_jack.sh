#!/bin/sh
pulseaudio -k; sleep 2; pulseaudio -L module-jack-sink -L module-jack-source