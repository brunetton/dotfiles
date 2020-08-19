#!/bin/bash
# => SUDO

max_brightness=$(cat /sys/class/backlight/intel_backlight/max_brightness)
brightness=$(cat /sys/class/backlight/intel_backlight/brightness)
increment=40

if (($brightness < $max_brightness)); then
  let brightness=$brightness+$increment
  echo "echo $brightness > /sys/class/backlight/intel_backlight/brightness" | bash
fi
