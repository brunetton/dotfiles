#!/bin/bash

# Click and kill window
id=`xprop _NET_WM_PID | awk '/PID/ {print $3}'`; kill -9 $id

