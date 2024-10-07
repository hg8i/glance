#!/bin/bash
script_dir=$(dirname "$(realpath "$0")")
python3 $script_dir/generate.py
vimb --title-override glanceview -c $script_dir/vimbrc $script_dir/index.html
