#!/bin/bash
python3 generate.py
script_dir=$(dirname "$(realpath "$0")")
vimb --title-override glanceview -c $script_dir/vimbrc $script_dir/index.html
