#!/bin/bash

tmux new-session -d -s tdv

tmux send-keys -t tdv './main.py' C-m

tmux split-window -h -t tdv

# switch users for correct write permissions
tmux send-keys -t tdv 'su - tdv' C-m
tmux send-keys -t tdv 'cd /app' C-m # switch back to /app directory where all the code is
tmux send-keys -t tdv './server.py' C-m

tail -f /dev/null