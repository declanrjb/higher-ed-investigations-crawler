cd ../notebooks
jupyter nbconvert --to python update-and-send.ipynb
python3 update-and-send.py
rm update-and-send.ipynb