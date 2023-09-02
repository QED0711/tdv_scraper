#!/bin/bash

tmux new-session -d -s tdv

tmux send-keys -t tdv './main.py' C-m

tmux split-window -h -t tdv

tmux send-keys -t tdv './server.py' C-m

tail -f /dev/null