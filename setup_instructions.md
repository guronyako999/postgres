# PostgreSQL 15
sudo apt-get install -y postgresql postgresql-client libpq-dev

# Запуск кластера и создание БД (выполнено при развёртывании)
sudo pg_ctlcluster 15 main start
sudo -u postgres psql -c "CREATE USER django_user WITH PASSWORD 'django_pass' CREATEDB;"
sudo -u postgres psql -c "CREATE DATABASE django_db OWNER django_user;"

# Python-зависимости
pip install django djangorestframework psycopg2-binary

# Миграции и запуск
python manage.py makemigrations catalog
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
