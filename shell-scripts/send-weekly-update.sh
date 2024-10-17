cd ../notebooks
jupyter nbconvert --to python update-and-send.ipynb
python3 update-and-send.py
rm update-and-send.py
cd ..
git add *
git commit -m 'latest data'
git push origin main