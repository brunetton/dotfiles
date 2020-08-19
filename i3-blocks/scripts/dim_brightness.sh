#!/bin/bash
max_brightness=$(cat /sys/class/backlight/intel_backlight/max_brightness)
brightness=$(cat /sys/class/backlight/intel_backlight/brightness)
percent=$(echo "scale=3;${brightness} / ${max_brightness} * 100" | bc -l | sed 's/[\.,][0-9]*//g')
increment=40

if (($percent > 2)); then
    let brightness=$brightness-$increment
  echo "echo $brightness > /sys/class/backlight/intel_backlight/brightness" | bash
fi
