pip install -r requirements.txt
docker-compose up -d
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
