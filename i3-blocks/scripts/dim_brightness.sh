#!/bin/bash
max_brightness=$(cat /sys/class/backlight/intel_backlight/max_brightness)
brightness=$(cat /sys/class/backlight/intel_backlight/brightness)
percent=$(echo "scale=3;${brightness} / ${max_brightness} * 100" | bc -l | sed 's/[\.,][0-9]*//g')


if (($percent > 2)); then
  let brightness=$brightness-10
  echo "echo $brightness > /sys/class/backlight/intel_backlight/brightness" | bash
fi
