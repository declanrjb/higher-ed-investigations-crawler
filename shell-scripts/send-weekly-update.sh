#!/bin/bash
cd /Users/declanbradley/Documents/Work/Journalism/Chronicle/higher-ed-investigations-crawler/shell-scripts/
cd ../notebooks
pip3 install jupytext
pip3 install requests
jupytext --to py update-and-send.ipynb
python3 update-and-send.py
cd ..
git add *
git commit -m 'latest data'
git push origin main