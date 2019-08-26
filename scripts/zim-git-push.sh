#!/bin/bash
# https://github.com/jaap-karssenberg/zim-wiki/wiki/Git-Pusher

if [ -f ~/.ssh/agent.env ] ; then
   . ~/.ssh/agent.env > /dev/null
   if ! kill -0 $SSH_AGENT_PID > /dev/null 2>&1; then
       echo "Stale agent file found. Spawning new agent… "
       eval `ssh-agent | tee ~/.ssh/agent.env`
   fi
    cd ~/zim-notes/
    git commit -m 'new version'
    git push && zenity --info --text "Pushed !" || zenity --error --text "Something went wrong :s"
else
    zenity --error --text "Can't find ssh agent :s"
fi

