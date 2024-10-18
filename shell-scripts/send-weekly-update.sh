#!/bin/bash
cd /Users/declanbradley/Documents/Work/Journalism/Chronicle/higher-ed-investigations-crawler/shell-scripts/
cd ../notebooks
update-and-send.ipynb -m jupyter nbconvert --to python --output update-and-send.py
python3 update-and-send.py
cd ..
git add *
git commit -m 'latest data'
git push origin main