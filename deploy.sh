source /.virualenv/bin/activate
git pull
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
