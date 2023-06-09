source .venv/bin/activate
streamlit run main.py

git init
touch .gitignore
echo ".ignore" >> .gitignore
git ls-files --others --exclude-standard

git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:oflorez/nameofrepository.git
git push -u origin main