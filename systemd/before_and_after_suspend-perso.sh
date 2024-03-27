#!/bin/sh
case $1 in
  pre)
    # Umount Google drive
    umount -l '/home/bruno/Google drive'
    killall google-drive-ocamlfuse -9
    killall kioslave5 -9
    umount /home/bruno/sshfs/naq
  ;;
  post)
    # # Restart xbanish
    # killall xbanish
    # xbanish &
  ;;
esac
